# FearPrime — repo map

Version 0.30 · 2026-09-20

## Princip

Hver filtype har ét primært ansvar. Krydslinks er ønskede; parallelle “master summaries” er ikke.

```text
manifest/model
   ↓
mechanism + learning
   ↓
measurement
   ↓
machine-readable data
   ↓
computational tools / model comparison
   ↓
audit / certainty / roadmap
```

## Kanoniske indgange

| Emne | Kanonisk indgang | Specialfiler |
|---|---|---|
| Projektets grundidé | `00_MANIFESTO.md` | `00_MANIFESTO/FEARPRIME_MODEL.md`, `05_MODELS/ADAPTIVE_PTSD_MODEL.md` |
| Fear/extinction | `03_EXTINCTION/EXTINCTION_ENGINE.md` | generalization, reconsolidation, return-of-fear |
| Predictive/ViolEx | `05_MODELS/PREDICTIVE_PROCESSING_ACTIVE_INFERENCE_MODEL.md` | ViolEx + computational comparison |
| Computational comparison | `05_MODELS/COMPUTATIONAL_MODEL_COMPARISON.md` | `tools/fearprime_model_compare.py` |
| Måling | `06_MEASUREMENT/MEASUREMENT_PLAN.md` | learning metrics, ViolEx, CPTSD, nightmares |
| Studier | `07_STUDIES/STUDY_LEDGER.md` | underkategorier + individuelle kort |
| Maskinlæsbare data | `data/README.md` | CSV/YAML + synthetic demo |
| Computational tools | `tools/README.md` | calculator + model comparison |
| Tests | `tests/test_fearprime_tools.py` | GitHub Actions workflow |
| Versionering | `CHANGELOG.md` | historiske snapshots i `09_DEBUG/ARCHIVE/` |

## Computational arkitektur

```text
violex_exposure_template.csv
        ↓
fearprime_bayesian_calculator.py
        ↓
derived session metrics

ordered trial/session rows
        ↓
fearprime_model_compare.py
        ↓
same-target predictions
        ↓
AIC / BIC / RMSE comparison
```

HGF-like modellen er stateful og afhænger af rækkefølgen. Flere deltagere må ikke blandes i samme sekvens uden participant-level segmentering.

## Legacy/kompakte filer

- `models/FEAR_EXTINCTION_MODEL.md` → kompakt ældre extinction-model.
- `02_MECHANISMS/MECHANISM_MAP.md` → kompakt ældre mekanismeoversigt.
- `07_STUDIES/VERIFIED/2014_Berceli_TRE_Caregivers.md` → alias for samme studie som det mere komplette Pilot-kort.

De må ikke tælles som ekstra evidens.

## Studiearkitektur

`07_STUDIES/` er opdelt efter evidenstype/rolle:
- `VERIFIED/`
- `PRECLINICAL/`
- `MECHANISTIC/`
- `REVIEWS/`
- `THEORY/`
- `QUALITATIVE/`
- `PROTOCOLS/`

## Dataarkitektur

Markdown forklarer evidensen; `data/` gør centrale felter analyserbare. Synthetic demo-data er kun til softwaretest og må ikke indgå i evidenssyntese.
