#!/usr/bin/env python3
"""FearPrime computational model comparison v0.1.

Compares project-level belief-update models on the same target:
post_threat_expectancy.

Implemented:
- no-update baseline
- Rescorla-Wagner / delta rule
- soft-evidence Bayesian update
- HGF-like adaptive-volatility approximation (NOT canonical HGF)
- active-inference-inspired precision/policy update (NOT canonical POMDP/FEP)

Dependency-free: Python standard library only.
"""
from __future__ import annotations

import argparse
import csv
import itertools
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Callable, Dict, Iterable, List, Optional, Sequence, Tuple

EPS = 1e-9


@dataclass
class Trial:
    pre: float
    observed: float
    post: float
    credibility: float = 100.0
    relevance: float = 100.0
    safety: float = 0.0


@dataclass
class FitResult:
    model: str
    params: Dict[str, float]
    predictions: List[float]
    k: int


def clamp(x: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, x))


def logistic(x: float) -> float:
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)


def logit(p: float) -> float:
    p = max(1e-6, min(1.0 - 1e-6, p))
    return math.log(p / (1.0 - p))


def num(row: Dict[str, str], key: str, default: Optional[float] = None) -> Optional[float]:
    value = (row.get(key) or "").strip()
    if not value:
        return default
    try:
        return float(value)
    except ValueError:
        return default


def load_trials(path: Path) -> List[Trial]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("Input CSV has no header.")
        required = {"pre_threat_expectancy", "observed_severity", "post_threat_expectancy"}
        missing = sorted(required - set(reader.fieldnames))
        if missing:
            raise ValueError("Missing required columns: " + ", ".join(missing))

        trials: List[Trial] = []
        for row in reader:
            pre = num(row, "pre_threat_expectancy")
            obs = num(row, "observed_severity")
            post = num(row, "post_threat_expectancy")
            if pre is None or obs is None or post is None:
                continue
            trials.append(
                Trial(
                    pre=clamp(pre),
                    observed=clamp(obs),
                    post=clamp(post),
                    credibility=clamp(num(row, "evidence_credibility", 100.0) or 100.0),
                    relevance=clamp(num(row, "evidence_relevance", 100.0) or 100.0),
                    safety=clamp(num(row, "safety_behavior_intensity", 0.0) or 0.0),
                )
            )
    if len(trials) < 3:
        raise ValueError("Need at least 3 complete rows for model comparison.")
    return trials


def sse(trials: Sequence[Trial], preds: Sequence[float]) -> float:
    return sum((t.post - p) ** 2 for t, p in zip(trials, preds))


def grid_best(
    trials: Sequence[Trial],
    model_name: str,
    k: int,
    candidates: Iterable[Dict[str, float]],
    predict: Callable[[Sequence[Trial], Dict[str, float]], List[float]],
) -> FitResult:
    best: Optional[FitResult] = None
    best_sse = float("inf")
    for params in candidates:
        preds = predict(trials, params)
        score = sse(trials, preds)
        if score < best_sse:
            best_sse = score
            best = FitResult(model_name, dict(params), preds, k)
    assert best is not None
    return best


def fit_no_update(trials: Sequence[Trial]) -> FitResult:
    return FitResult("no_update_baseline", {}, [t.pre for t in trials], 0)


def predict_rw(trials: Sequence[Trial], params: Dict[str, float]) -> List[float]:
    alpha = params["alpha"]
    return [clamp(t.pre + alpha * (t.observed - t.pre)) for t in trials]


def fit_rw(trials: Sequence[Trial]) -> FitResult:
    candidates = ({"alpha": i / 100.0} for i in range(0, 101))
    return grid_best(trials, "rescorla_wagner", 1, candidates, predict_rw)


def predict_bayes(trials: Sequence[Trial], params: Dict[str, float]) -> List[float]:
    kappa = params["prior_concentration"]
    out: List[float] = []
    for t in trials:
        prior = t.pre / 100.0
        obs = t.observed / 100.0
        evidence_w = max(
            0.05,
            math.sqrt((t.credibility / 100.0) * (t.relevance / 100.0)),
        )
        posterior = (prior * kappa + obs * evidence_w) / (kappa + evidence_w)
        out.append(clamp(posterior * 100.0))
    return out


def fit_bayes(trials: Sequence[Trial]) -> FitResult:
    grid = [0.05, 0.1, 0.2, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0]
    candidates = ({"prior_concentration": x} for x in grid)
    return grid_best(trials, "bayesian_soft_evidence", 1, candidates, predict_bayes)


def predict_hgf_like(trials: Sequence[Trial], params: Dict[str, float]) -> List[float]:
    """HGF-inspired adaptive-volatility approximation; not canonical HGF."""
    base_alpha = params["base_alpha"]
    vol_gain = params["volatility_gain"]
    decay = params["volatility_decay"]
    volatility = 0.0
    preds: List[float] = []
    for t in trials:
        lr = logistic(logit(base_alpha) + vol_gain * math.sqrt(max(volatility, 0.0)))
        preds.append(clamp(t.pre + lr * (t.observed - t.pre)))
        pe = (t.observed - t.pre) / 100.0
        volatility = decay * volatility + (1.0 - decay) * (pe * pe)
    return preds


def fit_hgf_like(trials: Sequence[Trial]) -> FitResult:
    base = [0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.9]
    gain = [0.0, 0.5, 1.0, 2.0, 4.0]
    decay = [0.2, 0.5, 0.8, 0.95]
    candidates = (
        {"base_alpha": a, "volatility_gain": g, "volatility_decay": d}
        for a, g, d in itertools.product(base, gain, decay)
    )
    return grid_best(trials, "hgf_like_adaptive_volatility", 3, candidates, predict_hgf_like)


def predict_active_like(trials: Sequence[Trial], params: Dict[str, float]) -> List[float]:
    """Active-inference-inspired precision/policy update; not canonical FEP/POMDP."""
    base_alpha = params["base_alpha"]
    evidence_gain = params["evidence_gain"]
    safety_gain = params["safety_gain"]
    preds: List[float] = []
    for t in trials:
        evidence = math.sqrt((t.credibility / 100.0) * (t.relevance / 100.0))
        safety = t.safety / 100.0
        lr = logistic(
            logit(base_alpha)
            + evidence_gain * (evidence - 0.5)
            - safety_gain * safety
        )
        preds.append(clamp(t.pre + lr * (t.observed - t.pre)))
    return preds


def fit_active_like(trials: Sequence[Trial]) -> FitResult:
    base = [0.05, 0.1, 0.2, 0.35, 0.5, 0.7, 0.9]
    egain = [0.0, 0.5, 1.0, 2.0, 4.0]
    sgain = [0.0, 0.5, 1.0, 2.0, 4.0]
    candidates = (
        {"base_alpha": a, "evidence_gain": e, "safety_gain": s}
        for a, e, s in itertools.product(base, egain, sgain)
    )
    return grid_best(
        trials,
        "active_inference_inspired_precision_policy",
        3,
        candidates,
        predict_active_like,
    )


def metrics(trials: Sequence[Trial], fit: FitResult) -> Dict[str, float]:
    n = len(trials)
    residuals = [t.post - p for t, p in zip(trials, fit.predictions)]
    score_sse = sum(r * r for r in residuals)
    mae = sum(abs(r) for r in residuals) / n
    rmse = math.sqrt(score_sse / n)
    variance = max(score_sse / n, EPS)
    nll = 0.5 * n * (math.log(2.0 * math.pi * variance) + 1.0)
    return {
        "n": float(n),
        "sse": score_sse,
        "mae": mae,
        "rmse": rmse,
        "nll_gaussian": nll,
        "aic": 2.0 * fit.k + 2.0 * nll,
        "bic": fit.k * math.log(n) + 2.0 * nll,
    }


def fit_all(trials: Sequence[Trial]) -> List[Tuple[FitResult, Dict[str, float]]]:
    fits = [
        fit_no_update(trials),
        fit_rw(trials),
        fit_bayes(trials),
        fit_hgf_like(trials),
        fit_active_like(trials),
    ]
    scored = [(fit, metrics(trials, fit)) for fit in fits]
    scored.sort(key=lambda pair: pair[1]["bic"])
    best_bic = scored[0][1]["bic"]
    for _, metric in scored:
        metric["delta_bic"] = metric["bic"] - best_bic
    return scored


def params_text(params: Dict[str, float]) -> str:
    return ";".join(f"{k}={v:.6g}" for k, v in sorted(params.items()))


def write_summary(
    output_path: Path, scored: Sequence[Tuple[FitResult, Dict[str, float]]]
) -> None:
    fields = [
        "rank",
        "model",
        "parameters",
        "n",
        "sse",
        "mae",
        "rmse",
        "nll_gaussian",
        "aic",
        "bic",
        "delta_bic",
    ]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for rank, (fit, metric) in enumerate(scored, start=1):
            writer.writerow(
                {
                    "rank": rank,
                    "model": fit.model,
                    "parameters": params_text(fit.params),
                    **{k: f"{metric[k]:.6g}" for k in fields if k in metric},
                }
            )


def write_predictions(
    output_path: Path,
    trials: Sequence[Trial],
    scored: Sequence[Tuple[FitResult, Dict[str, float]]],
) -> None:
    fields = ["row", "pre", "observed", "post_observed"] + [
        fit.model for fit, _ in scored
    ]
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for i, trial in enumerate(trials, start=1):
            row: Dict[str, object] = {
                "row": i,
                "pre": f"{trial.pre:.6g}",
                "observed": f"{trial.observed:.6g}",
                "post_observed": f"{trial.post:.6g}",
            }
            for fit, _ in scored:
                row[fit.model] = f"{fit.predictions[i - 1]:.6g}"
            writer.writerow(row)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compare FearPrime belief-update models on post-threat expectancy."
    )
    parser.add_argument("input_csv", type=Path)
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("model_comparison.csv"),
        help="Model-comparison summary CSV.",
    )
    parser.add_argument(
        "--predictions",
        type=Path,
        default=Path("model_predictions.csv"),
        help="Per-row model predictions CSV.",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        trials = load_trials(args.input_csv)
        scored = fit_all(trials)
        write_summary(args.output, scored)
        write_predictions(args.predictions, trials, scored)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    print(f"Wrote comparison to {args.output}")
    print(f"Wrote predictions to {args.predictions}")
    print("Best in-sample BIC:", scored[0][0].model)
    print(
        "Caution: HGF-like and active-inference-inspired models are approximations, "
        "not canonical implementations."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
