# FearPrime computational tools

Version 0.2 · repo v0.30

Dependency-free Python utilities for the public FearPrime framework. They use only the Python standard library.

## 1. Bayesian Calculator v0.1

Input: a CSV using the fields in `data/violex_exposure_template.csv`.

Run:

```bash
python tools/fearprime_bayesian_calculator.py data/computational_demo.csv -o out/violex_calculated.csv
```

It adds project-descriptive fields for:

- signed/absolute prediction error,
- expectancy update,
- update efficiency,
- accommodation-like score,
- immunization-like score,
- generalized-belief update,
- next-day retention,
- generalization update.

The accommodation/immunization scores are **heuristics for research exploration**, not validated clinical scales.

## 2. Computational model comparison v0.1

Run:

```bash
python tools/fearprime_model_compare.py data/computational_demo.csv \
  -o out/model_comparison.csv \
  --predictions out/model_predictions.csv
```

All models predict the same target: `post_threat_expectancy`.

Implemented:

| Model | Parameters | Status |
|---|---:|---|
| No-update baseline | 0 | baseline |
| Rescorla–Wagner | 1 | standard delta-rule comparator |
| Soft-evidence Bayesian | 1 | simplified Bayesian comparator |
| HGF-like adaptive volatility | 3 | approximation, **not canonical HGF** |
| Active-inference-inspired precision/policy | 3 | approximation, **not canonical active inference/POMDP** |

The script reports SSE, MAE, RMSE, Gaussian NLL, AIC, BIC and ΔBIC. Ranking is in-sample and exploratory.

## 3. Repository QA audit v0.1

`fearprime_repo_audit.py` checks framework integrity without changing files.

Run:

```bash
python tools/fearprime_repo_audit.py .
```

Strict mode returns a non-zero exit code when hard errors are found:

```bash
python tools/fearprime_repo_audit.py . --strict
```

Current checks:

- missing internal Markdown link targets,
- `VERSION` consistency against root README, repo-map and latest released changelog entry,
- CSV readability and header integrity in `data/`,
- Markdown files with no detected inbound link as **warnings**,
- duplicate PMID/DOI appearances across study-card files as **warnings for manual review**.

Warnings are intentionally non-destructive. A repeated PMID/DOI can represent an alias, reanalysis or deliberate cross-reference and is therefore not automatically treated as duplicate evidence.

YAML schema validation and personal-data detection are not claimed by this tool yet; those remain explicit release-check items until a reliable validator is added.

## Tests

```bash
python -m unittest discover -s tests -v
```

GitHub Actions runs unit tests, calculator/model smoke tests and the repository QA report.

## Method rule

Do not interpret any fitted parameter as a neural biomarker. A model that fits these behavioral/session data well is not thereby proven to be the brain's mechanism.

See [Computational Model Comparison](../05_MODELS/COMPUTATIONAL_MODEL_COMPARISON.md).
