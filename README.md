# FearPrime_03

**Aktuel framework-version: v0.28 · 2026-09-20**

FearPrime er et forskningsframework om PTSD/CPTSD, threat/safety learning, extinction, reconsolidation, kontekst, interoception og biologisk augmentation.

Kerneprincippet er funktionelt: defensive reaktioner kan være beskyttende i én kontekst og samtidig blive for brede, stive eller omkostningsfulde i en anden. Målet er bedre kalibrering, fleksibilitet, generalisering og funktion — ikke “nul frygt”.

> Repoet er et forsknings- og hypoteseframework. Mekanistisk plausibilitet, laboratorielæring og klinisk effekt holdes adskilt.

## Start her

1. [Manifest og formål](00_MANIFESTO.md)
2. [Adaptiv PTSD-model](05_MODELS/ADAPTIVE_PTSD_MODEL.md)
3. [Eksponering og ny læring](03_EXTINCTION/EXTINCTION_ENGINE.md)
4. [ViolEx 2.0 — expectation update vs. maintenance](05_MODELS/VIOLEX_2_EXPECTATION_UPDATE_MODEL.md)
5. [Fear Circuit Master Map](02_MECHANISMS/FEAR_CIRCUIT_MASTER_MAP.md)
6. [Kandidatmatrix](04_CANDIDATES/CANDIDATE_MATRIX.md)
7. [Måleplan](06_MEASUREMENT/MEASUREMENT_PLAN.md)
8. [Studieregister](07_STUDIES/STUDY_LEDGER.md)
9. [Evidensregler](01_EVIDENCE_RULES.md)

## Repo-struktur

| Mappe | Ansvar |
|---|---|
| `00_MANIFESTO/` | Grundmodel og projektfilosofi |
| `02_MECHANISMS/` | Kredsløb, signalveje og biologiske mekanismer |
| `03_EXTINCTION/` | Learning, extinction, reconsolidation, generalization og søvn/nightmares |
| `04_CANDIDATES/` | Interventioner/præparater og kandidatdossiers |
| `05_MODELS/` | Samlede modeller og eksplorative hypoteser |
| `06_MEASUREMENT/` | Outcomes, metrics og observations-/målerammer |
| `07_STUDIES/` | Primær evidens, reviews, teori og kildekort |
| `08_RESOURCES/` | Læringsressourcer, bøger, podcasts, videoer og kategorier |
| `09_DEBUG/` | Metode, søgelogs, audits, certainty, roadmap og arkiv |
| `data/` | Maskinlæsbare studie-, effekt-, RoB-, certainty- og måleschemas |

Se [REPO_MAP.md](REPO_MAP.md) for det detaljerede kort.

## Centrale faglige indgange

### Modeller
- [Funktionel PTSD-model](00_MANIFESTO/FEARPRIME_MODEL.md)
- [Adaptiv PTSD-model](05_MODELS/ADAPTIVE_PTSD_MODEL.md)
- [CPTSD-model](05_MODELS/CPTSD_MODEL.md)
- [ViolEx 2.0 — expectation update vs. maintenance](05_MODELS/VIOLEX_2_EXPECTATION_UPDATE_MODEL.md)
- [Plasticity Window Engine](05_MODELS/PLASTICITY_WINDOW_ENGINE.md)

### Learning
- [Extinction Engine](03_EXTINCTION/EXTINCTION_ENGINE.md)
- [Generalization & Safety Learning Engine](03_EXTINCTION/GENERALIZATION_AND_SAFETY_LEARNING_ENGINE.md)
- [Reconsolidation boundary conditions](03_EXTINCTION/RECONSOLIDATION_BOUNDARY_CONDITIONS.md)
- [Nightmare/sleep dossier](03_EXTINCTION/PTSD_NIGHTMARE_SLEEP_DOSSIER.md)

### Mekanismer
- [Fear Circuit Master Map](02_MECHANISMS/FEAR_CIRCUIT_MASTER_MAP.md)
- [Hippocampus/context discrimination](02_MECHANISMS/HIPPOCAMPUS_CONTEXT_DISCRIMINATION.md)
- [Insula/interoception](02_MECHANISMS/INSULA_INTEROCEPTION.md)
- [HPA/stress-memory](02_MECHANISMS/HPA_STRESS_MEMORY.md)
- [NMDA/AMPA/glutamaterg plasticitet](02_MECHANISMS/NMDA_AMPA_GLUTAMATE_PLASTICITY.md)
- [HDAC/BDNF/5-HT7/dopamin](02_MECHANISMS/HDAC_BDNF_5HT7_DOPAMINE.md)
- [PNN/critical-period reopening](02_MECHANISMS/PNN_CRITICAL_PERIOD_REOPENING.md)

### Kandidater
- [Kandidatmatrix](04_CANDIDATES/CANDIDATE_MATRIX.md)
- [Butyrat](04_CANDIDATES/BUTYRATE_DOSSIER.md)
- [D-cycloserin](04_CANDIDATES/DCS_DOSSIER.md)
- [FAAH/CB1/endocannabinoid](04_CANDIDATES/ENDOCANNABINOID_FAAH_CB1_DOSSIER.md)
- [L-DOPA](04_CANDIDATES/LDOPA_DOSSIER.md)
- [Lurasidon](04_CANDIDATES/LURASIDONE_DOSSIER.md)
- [Oxytocin](04_CANDIDATES/OXYTOCIN_DOSSIER.md)
- [Propranolol](04_CANDIDATES/PROPRANOLOL_DOSSIER.md)

### Måling og metode
- [Måleplan](06_MEASUREMENT/MEASUREMENT_PLAN.md)
- [Learning metrics](06_MEASUREMENT/LEARNING_METRICS.md)
- [Nightmare Measurement Engine](06_MEASUREMENT/NIGHTMARE_MEASUREMENT_ENGINE.md)
- [Risk of Bias template](09_DEBUG/RISK_OF_BIAS_TEMPLATE.md)
- [Effect-size standard](09_DEBUG/EFFECT_SIZE_EXTRACTION_STANDARD.md)
- [Systematic search protocol](09_DEBUG/SYSTEMATIC_SEARCH_PROTOCOL.md)
- [Certainty framework](09_DEBUG/CERTAINTY_FRAMEWORK.md)

## Aktuel status

- P0/P1 er dækket på framework-/dossierniveau.
- P2 har maskinlæsbar dataarkitektur, RoB, effect-size/CI, participant-overlap, search logs og claim-level certainty.
- Reconsolidation-sporet har et verificeret PubMed-indexeret screening/export-set, men ikke komplet native PubMed/PRISMA-flow.
- Nightmare- og interoception-sporene har operationelle measurement/preregistration-lag.
- ViolEx 2.0 er integreret som et valgfrit lag til analyse af expectation update vs. maintenance efter expectation violations.
- Ingen claim behandles som stærkere end det direkte evidensniveau tillader.

Se:
- [Coverage Plan](09_DEBUG/COVERAGE_PLAN.md) — hvad der er dækket, og hvad der mangler.
- [v1.0 Gap Audit](09_DEBUG/FEARPRIME_V1_GAP_AUDIT.md) — readiness mod v1.0.
- [CHANGELOG.md](CHANGELOG.md) — versionshistorik fremadrettet.

## Historik

Den tidligere v0.26-README med alle gamle versionssektioner er bevaret ordret i:
[README v0.26 snapshot](09_DEBUG/ARCHIVE/README_v0.26_SNAPSHOT.md).

Fra v0.27 ligger versionshistorik i [CHANGELOG.md](CHANGELOG.md), ikke på forsiden.

## Ressourcer

- [Ressourceindeks](08_RESOURCES/README.md)
- [Danske fagbegreber](DANSK_ORDBOG.md)
- [Data layer](data/README.md)

Repoet er offentligt; personlige helbredsregistreringer skal opbevares privat.
