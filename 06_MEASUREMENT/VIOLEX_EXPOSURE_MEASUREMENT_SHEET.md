# FearPrime — ViolEx Exposure Measurement Sheet

Version 0.29 · 2026-09-20

## Formål

Konkret session-skabelon til:

~~~text
prediction
→ expectation violation
→ evidence credibility
→ accommodation / immunization
→ updated expectation
→ delayed retention
→ generalization
~~~

Bygger på [ViolEx 2.0](../05_MODELS/VIOLEX_2_EXPECTATION_UPDATE_MODEL.md) og kan kobles til [Predictive Processing / Active Inference](../05_MODELS/PREDICTIVE_PROCESSING_ACTIVE_INFERENCE_MODEL.md).

Scorerne er projektdeskriptive og ikke validerede kliniske scales.

## A. Metadata

- Session ID:
- Dato/tid:
- Kontekst/sted:
- Opgave:
- Søvn/stress/state:
- Samtidige ændringer:
- Reel objektiv risiko: lav / mellem / høj / uklar

## B. Hypoteser før session

### H1 — threat hypothesis

> Hvis __________, forventer jeg __________.

- Threat expectancy: ___ /100
- Confidence: ___ /100
- Expected cost/severity: ___ /100

### H2 — alternativ/safety hypothesis

> __________

- Alternativ expectancy: ___ /100
- Confidence: ___ /100

### Diagnostiske observationer

Evidens **for H1**:

> __________

Evidens **mod H1 / for H2**:

> __________

## C. Anticipatorisk respons og policy

- Distress/fear: ___ /10
- Kroppens aktivering: ___ /10
- Urge to avoid/escape: ___ /10
- Perceived controllability: ___ /100

Planlagt handling:

> __________

### Safety behavior / assimilation

- [ ] undgåelse
- [ ] escape-plan
- [ ] checking/kontrol
- [ ] reassurance
- [ ] scanning/hypervigilance
- [ ] distraktion
- [ ] person som safety cue
- [ ] andet: __________
- [ ] ingen relevant

Funktion:
- [ ] nødvendig pga. reel risiko
- [ ] beskyttende men gør testen mindre diagnostisk
- [ ] primært forventningsbeskyttende/assimilerende
- [ ] uklart

## D. Faktisk observation

Hvad skete observerbart?

> __________

- Frygtet outcome: ja / nej / delvist / uklart
- Observeret severity: ___ /100
- Distress peak: ___ /10
- Distress ved slut: ___ /10

### Prediction error / violation

~~~text
PE_signed = observed_outcome - expected_outcome
PE_absolute = |observed_outcome - expected_outcome|
~~~

- PE_signed: ___
- PE_absolute: ___
- Subjektiv violation magnitude: ___ /100

## E. Diagnostisk værdi

- Evidence credibility: ___ /100
- Evidence relevance for H1: ___ /100
- Safety behavior påvirkede outcome: ___ /100
- Alternativ forklaring styrke: ___ /100

Forklaring:

> __________

## F. Umiddelbar belief update

- Post threat expectancy: ___ /100
- Post threat confidence: ___ /100
- Post safety expectancy: ___ /100

~~~text
expectancy_update =
post_threat_expectancy - pre_threat_expectancy
~~~

### ViolEx response

- [ ] accommodation
- [ ] data-oriented immunization
- [ ] concept-oriented immunization
- [ ] mixed
- [ ] ingen reel violation
- [ ] uklart

Hvad blev opdateret eller immuniseret?

> __________

## G. Generaliseret belief

Generaliseret regel:

> __________

- Før: ___ /100
- Efter: ___ /100

~~~text
generalized_update =
post_generalized_belief - pre_generalized_belief
~~~

## H. Delayed retention

### Næste dag

- Threat expectancy: ___ /100
- Recall af ny information: ___ /100
- Return of fear/distress: ___ /10
- Fortolkning ændret? ja / nej / uklart

### Senere follow-up

- Dato:
- Threat expectancy: ___ /100
- Funktion/adfærd ændret: ja / nej / uklart
- Ny safety behavior: ja / nej / uklart
- Belief update bevaret: ja / delvist / nej / uklart

## I. Generalization test

Ny beslægtet kontekst:

> __________

- Pre threat expectancy: ___ /100
- Faktisk outcome:
- Post threat expectancy: ___ /100

- [ ] læring generaliserede
- [ ] kontekstspecifik
- [ ] immunization opstod igen
- [ ] utilstrækkelige data

## J. Research summary

- Pre threat expectancy:
- Post threat expectancy:
- Delayed threat expectancy:
- PE_absolute:
- Evidence credibility:
- Accommodation 0–100:
- Immunization 0–100:
- Safety behavior intensity 0–100:
- Generalized belief update:
- Functional approach/change:
- Adverse/unexpected event:

## Kritisk kontrol

1. Var prediction defineret før outcome?
2. Var outcome observerbart?
3. Kunne safety behavior have skabt udfaldet?
4. Blev absence of harm fejlagtigt lig med proof of safety?
5. Blev reel risiko overset?
6. Er ændringen akut state change eller delayed learning?
7. Blev én episode overgeneraliseret?
8. Er data bedre forklaret af en enklere mekanisme?

## Machine-readable parallel

- [CSV-template](../data/violex_exposure_template.csv)
- [YAML-schema](../data/violex_exposure_schema.yaml)
