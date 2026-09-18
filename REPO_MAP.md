# FearPrime — repo map

Version 0.27 · 2026-09-18

## Princip

Hver filtype har ét primært ansvar. Krydslinks er ønskede; parallelle “master summaries” er ikke.

```text
manifest/model
   ↓
mechanism + learning
   ↓
candidate dossier
   ↓
study cards
   ↓
measurement
   ↓
machine-readable data
   ↓
audit / certainty / roadmap
```

## Kanoniske indgange

| Emne | Kanonisk indgang | Specialfiler |
|---|---|---|
| Projektets grundidé | `00_MANIFESTO.md` | `00_MANIFESTO/FEARPRIME_MODEL.md`, `05_MODELS/ADAPTIVE_PTSD_MODEL.md` |
| Fear/extinction | `03_EXTINCTION/EXTINCTION_ENGINE.md` | generalization, reconsolidation, return-of-fear |
| Neurobiologi | `02_MECHANISMS/FEAR_CIRCUIT_MASTER_MAP.md` | hippocampus, insula, HPA, NMDA/AMPA, HDAC, PNN |
| Kandidater | `04_CANDIDATES/CANDIDATE_MATRIX.md` | ét dossier pr. kandidat + specialmoduler |
| Måling | `06_MEASUREMENT/MEASUREMENT_PLAN.md` | learning metrics, CPTSD, nightmares |
| Studier | `07_STUDIES/STUDY_LEDGER.md` | underkategorier + individuelle kort |
| Bibliografi | `07_STUDIES/SOURCE_REGISTER.md` | source indexes + study cards |
| Evidensmetode | `09_DEBUG/README.md` | RoB, search, certainty, audits |
| Maskinlæsbare data | `data/README.md` | CSV/YAML |
| Versionering | `CHANGELOG.md` | historiske snapshots i `09_DEBUG/ARCHIVE/` |

## Legacy/kompakte filer

Følgende filer bevares, men er ikke længere hovedindgange:

- `models/FEAR_EXTINCTION_MODEL.md` → kompakt ældre extinction-model.
- `02_MECHANISMS/MECHANISM_MAP.md` → kompakt ældre mekanismeoversigt.
- `07_STUDIES/VERIFIED/2014_Berceli_TRE_Caregivers.md` → alias for samme studie som det mere komplette Pilot-kort.

De må ikke tælles som ekstra evidens.

## Statusfiler må ikke konkurrere

- `COVERAGE_PLAN.md` = domænedækning og næste forskningsarbejde.
- `FEARPRIME_V1_GAP_AUDIT.md` = readiness mod en defineret v1.0.
- `CERTAINTY_FRAMEWORK.md` = metode for certainty.
- `*_CERTAINTY_PROFILE.md` = anvendelse på claims.
- `*_SEARCH_LOG.md` = historik over faktisk søgning.
- daterede search/export-filer = immutable snapshots af en bestemt søgning.

## Kandidatfiler

Et kandidatdossier er hovedfilen for evidensstatus.

Specialfiler skal kun svare på et snævrere spørgsmål, fx:
- butyrat-formulering/CNS,
- lurasidon-receptor/learning,
- HDAC2-selektivitet,
- critical-period translation.

De må ikke udvikle en separat samlet efficacy-konklusion, som konkurrerer med hoveddossieret.

## Studiearkitektur

`07_STUDIES/` er opdelt efter evidenstype/rolle:

- `VERIFIED/` — humane studiekort og samlekort.
- `PRECLINICAL/` — dyreforsøg.
- `MECHANISTIC/` — PK, receptor-, target- og mekanismekilder.
- `REVIEWS/` — reviews/meta-analyser.
- `THEORY/` — teorikilder.
- `QUALITATIVE/` — kvalitativ forskning.
- `PROTOCOLS/` — protokoller uden færdige outcomes.

Mappenavnet VERIFIED er historisk og betyder ikke automatisk høj evidenskvalitet.

## Dataarkitektur

Markdown forklarer evidensen; `data/` gør centrale felter analyserbare.

Kanoniske maskinlæsbare tabeller:
- `studies.csv`
- `effects.csv`
- `risk_of_bias.csv`
- `certainty.csv`
- `participant_overlap.csv`
- `search_log.csv`

Measurement schemas holdes adskilt fra evidence tables.
