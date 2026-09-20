#!/usr/bin/env python3
"""FearPrime Bayesian Calculator v0.1.

Dependency-free calculator for FearPrime ViolEx exposure CSV files.

This is a project-descriptive research utility. It does not estimate neural
prediction errors, synaptic learning rates, Bayesian precision, or
reconsolidation.
"""
from __future__ import annotations

import argparse
import csv
import math
import sys
from pathlib import Path
from typing import Dict, List, Optional

EPSILON = 1e-9

REQUIRED_COLUMNS = (
    "pre_threat_expectancy",
    "observed_severity",
    "post_threat_expectancy",
)


def _num(row: Dict[str, str], key: str) -> Optional[float]:
    value = (row.get(key) or "").strip()
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def _clamp(value: float, lo: float = 0.0, hi: float = 100.0) -> float:
    return max(lo, min(hi, value))


def _fmt(value: Optional[float]) -> str:
    if value is None or not math.isfinite(value):
        return ""
    return f"{value:.6g}"


def _directional_alignment(pe: float, update: float) -> float:
    """0..1: did belief move in the same signed direction as the mismatch?"""
    if abs(pe) < EPSILON or pe * update <= 0:
        return 0.0
    return min(abs(update) / max(abs(pe), EPSILON), 1.0)


def derive_row(row: Dict[str, str]) -> Dict[str, str]:
    out = dict(row)
    pre = _num(row, "pre_threat_expectancy")
    observed = _num(row, "observed_severity")
    post = _num(row, "post_threat_expectancy")

    pe_signed = observed - pre if pre is not None and observed is not None else None
    pe_absolute = abs(pe_signed) if pe_signed is not None else None
    expectancy_update = post - pre if pre is not None and post is not None else None

    update_efficiency = None
    accommodation_score = None
    immunization_score = None
    inferred = ""

    if pe_absolute is not None and expectancy_update is not None:
        update_efficiency = abs(expectancy_update) / max(pe_absolute, 1.0)

        credibility = _num(row, "evidence_credibility")
        relevance = _num(row, "evidence_relevance")
        credibility_w = _clamp(credibility if credibility is not None else 100.0) / 100.0
        relevance_w = _clamp(relevance if relevance is not None else 100.0) / 100.0
        evidence_w = math.sqrt(credibility_w * relevance_w)

        alignment = _directional_alignment(pe_signed or 0.0, expectancy_update)
        violation_w = min(pe_absolute / 100.0, 1.0)

        accommodation_score = 100.0 * alignment * evidence_w
        immunization_score = 100.0 * violation_w * evidence_w * (1.0 - alignment)

        if pe_absolute < 5.0:
            inferred = "no_meaningful_violation"
        elif alignment >= 0.50:
            inferred = "accommodation_like"
        elif evidence_w >= 0.50 and pe_absolute >= 20.0:
            inferred = "immunization_like"
        else:
            inferred = "mixed_or_unclear"

    pre_gen = _num(row, "pre_generalized_belief")
    post_gen = _num(row, "post_generalized_belief")
    generalized_update = (
        post_gen - pre_gen if pre_gen is not None and post_gen is not None else None
    )

    next_day = _num(row, "next_day_threat_expectancy")
    delayed_delta_from_post = (
        next_day - post if next_day is not None and post is not None else None
    )
    retained_update = (
        next_day - pre if next_day is not None and pre is not None else None
    )
    retention_fraction = None
    if (
        retained_update is not None
        and expectancy_update is not None
        and abs(expectancy_update) >= 1.0
    ):
        retention_fraction = retained_update / expectancy_update

    gen_pre = _num(row, "generalization_pre_expectancy")
    gen_post = _num(row, "generalization_post_expectancy")
    generalization_update = (
        gen_post - gen_pre if gen_pre is not None and gen_post is not None else None
    )

    out.update(
        {
            "calc_pe_signed": _fmt(pe_signed),
            "calc_pe_absolute": _fmt(pe_absolute),
            "calc_expectancy_update": _fmt(expectancy_update),
            "calc_update_efficiency": _fmt(update_efficiency),
            "calc_accommodation_score": _fmt(accommodation_score),
            "calc_immunization_score": _fmt(immunization_score),
            "calc_inferred_violex_response": inferred,
            "calc_generalized_update": _fmt(generalized_update),
            "calc_next_day_delta_from_post": _fmt(delayed_delta_from_post),
            "calc_retained_update": _fmt(retained_update),
            "calc_retention_fraction": _fmt(retention_fraction),
            "calc_generalization_update": _fmt(generalization_update),
        }
    )
    return out


DERIVED_COLUMNS = [
    "calc_pe_signed",
    "calc_pe_absolute",
    "calc_expectancy_update",
    "calc_update_efficiency",
    "calc_accommodation_score",
    "calc_immunization_score",
    "calc_inferred_violex_response",
    "calc_generalized_update",
    "calc_next_day_delta_from_post",
    "calc_retained_update",
    "calc_retention_fraction",
    "calc_generalization_update",
]


def process(input_path: Path, output_path: Path) -> int:
    with input_path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        if not reader.fieldnames:
            raise ValueError("Input CSV has no header.")
        missing = [c for c in REQUIRED_COLUMNS if c not in reader.fieldnames]
        if missing:
            raise ValueError("Missing required columns: " + ", ".join(missing))
        rows = [derive_row(row) for row in reader]
        fields = list(reader.fieldnames)
        for col in DERIVED_COLUMNS:
            if col not in fields:
                fields.append(col)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)
    return len(rows)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Compute descriptive FearPrime ViolEx learning metrics."
    )
    parser.add_argument("input_csv", type=Path)
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("violex_calculated.csv"),
        help="Output CSV (default: violex_calculated.csv)",
    )
    return parser


def main(argv: Optional[List[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        count = process(args.input_csv, args.output)
    except (OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(f"Wrote {count} row(s) to {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
