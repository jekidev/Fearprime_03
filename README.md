# FearPrime_03

**Aktuel framework-version: v0.30 · 2026-09-20**

FearPrime er et forskningsframework om PTSD/CPTSD, threat/safety learning, extinction, reconsolidation, kontekst, interoception, predictive processing og biologisk augmentation.

Kerneprincippet er funktionelt: defensive reaktioner kan være beskyttende i én kontekst og samtidig blive for brede, stive eller omkostningsfulde i en anden. Målet er bedre kalibrering, fleksibilitet, generalisering og funktion — ikke “nul frygt”.

> Repoet er et forsknings- og hypoteseframework. Mekanistisk plausibilitet, laboratorielæring og klinisk effekt holdes adskilt.

## Start her

1. [Manifest og formål](00_MANIFESTO.md)
2. [Adaptiv PTSD-model](05_MODELS/ADAPTIVE_PTSD_MODEL.md)
3. [Eksponering og ny læring](03_EXTINCTION/EXTINCTION_ENGINE.md)
4. [ViolEx 2.0](05_MODELS/VIOLEX_2_EXPECTATION_UPDATE_MODEL.md)
5. [Predictive Processing / Bayesian / Active Inference](05_MODELS/PREDICTIVE_PROCESSING_ACTIVE_INFERENCE_MODEL.md)
6. [Computational Model Comparison](05_MODELS/COMPUTATIONAL_MODEL_COMPARISON.md)
7. [ViolEx Exposure Measurement Sheet](06_MEASUREMENT/VIOLEX_EXPOSURE_MEASUREMENT_SHEET.md)
8. [Computational tools](tools/README.md)
9. [Fear Circuit Master Map](02_MECHANISMS/FEAR_CIRCUIT_MASTER_MAP.md)
10. [Kandidatmatrix](04_CANDIDATES/CANDIDATE_MATRIX.md)
11. [Måleplan](06_MEASUREMENT/MEASUREMENT_PLAN.md)
12. [Studieregister](07_STUDIES/STUDY_LEDGER.md)
13. [Evidensregler](01_EVIDENCE_RULES.md)

## Repo-struktur

| Mappe | Ansvar |
|---|---|
| `00_MANIFESTO/` | Grundmodel og projektfilosofi |
| `02_MECHANISMS/` | Kredsløb, signalveje og biologiske mekanismer |
| `03_EXTINCTION/` | Learning, extinction, reconsolidation, generalization og søvn/nightmares |
| `04_CANDIDATES/` | Interventioner/præparater og kandidatdossiers |
| `05_MODELS/` | Samlede modeller og eksplorative computational models |
| `06_MEASUREMENT/` | Outcomes, metrics og observations-/målerammer |
| `07_STUDIES/` | Primær evidens, reviews, teori og kildekort |
| `08_RESOURCES/` | Læringsressourcer, bøger, podcasts, videoer og kategorier |
| `09_DEBUG/` | Metode, søgelogs, audits, certainty, roadmap og arkiv |
| `data/` | Maskinlæsbare studie- og måledata/schemaer |
| `tools/` | Dependency-free Python calculators/model comparison |
| `tests/` | Regression tests for computational tools |

Se [REPO_MAP.md](REPO_MAP.md) for det detaljerede kort.

## Centrale faglige indgange

### Modeller
- [Funktionel PTSD-model](00_MANIFESTO/FEARPRIME_MODEL.md)
- [Adaptiv PTSD-model](05_MODELS/ADAPTIVE_PTSD_MODEL.md)
- [CPTSD-model](05_MODELS/CPTSD_MODEL.md)
- [ViolEx 2.0](05_MODELS/VIOLEX_2_EXPECTATION_UPDATE_MODEL.md)
- [Predictive Processing / Bayesian / Active Inference](05_MODELS/PREDICTIVE_PROCESSING_ACTIVE_INFERENCE_MODEL.md)
- [Computational Model Comparison](05_MODELS/COMPUTATIONAL_MODEL_COMPARISON.md)
- [Plasticity Window Engine](05_MODELS/PLASTICITY_WINDOW_ENGINE.md)

### Måling og computational tools
- [Måleplan](06_MEASUREMENT/MEASUREMENT_PLAN.md)
- [Learning metrics](06_MEASUREMENT/LEARNING_METRICS.md)
- [ViolEx Exposure Measurement Sheet](06_MEASUREMENT/VIOLEX_EXPOSURE_MEASUREMENT_SHEET.md)
- [Bayesian Calculator + Model Compare](tools/README.md)
- [Synthetic computational demo](data/computational_demo.csv)

## Computational v0.1

`tools/fearprime_bayesian_calculator.py` beregner PE, expectancy update, descriptive accommodation/immunization, retention og generalization fra ViolEx CSV-data.

`tools/fearprime_model_compare.py` sammenligner på samme target:
- no-update baseline,
- Rescorla–Wagner,
- soft-evidence Bayesian,
- HGF-like adaptive volatility,
- active-inference-inspired precision/policy.

HGF-like og active-inference-inspired modellerne er **approximationsmodeller**, ikke canonical implementations. Model-fit er ikke bevis for en neuronal mekanisme.

## Aktuel status

- ViolEx 2.0 er integreret som lag til expectation update vs. maintenance.
- Predictive-processing/Bayesian/active-inference laget formaliserer priors, evidence weighting og action/policy selection.
- ViolEx exposure-måling findes som Markdown-template og CSV/YAML.
- Computational v0.1 kan beregne session metrics og lave model comparison med AIC/BIC/RMSE.
- Unit tests og GitHub Actions smoke-tests er tilføjet.
- Ingen claim behandles som stærkere end det direkte evidensniveau tillader.

Se:
- [Coverage Plan](09_DEBUG/COVERAGE_PLAN.md)
- [v1.0 Gap Audit](09_DEBUG/FEARPRIME_V1_GAP_AUDIT.md)
- [CHANGELOG.md](CHANGELOG.md)

## Historik

Den tidligere v0.26-README er bevaret i [README v0.26 snapshot](09_DEBUG/ARCHIVE/README_v0.26_SNAPSHOT.md).

## Ressourcer

- [Ressourceindeks](08_RESOURCES/README.md)
- [Danske fagbegreber](DANSK_ORDBOG.md)
- [Data layer](data/README.md)

Repoet er offentligt; personlige helbredsregistreringer skal opbevares privat.
