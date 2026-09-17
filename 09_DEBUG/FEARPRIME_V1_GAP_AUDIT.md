# FearPrime v1.0 — gap-audit

Dato: 2026-09-17  
Status efter version 0.21

## Formål
Denne audit vurderer **framework-dækning**, ikke om en behandling virker. Den spørger:

> Hvilke dele skal være på plads, før FearPrime kan kaldes et sammenhængende v1.0-forskningsframework?

### Statussymboler
- ✅ = dækket på framework-niveau
- 🟡 = delvist dækket / kræver udbygning
- 🔴 = væsentligt hul
- 🔬 = aktiv hypotese eller mekanistisk forskningsspor
- 👤 = human evidens findes
- 🐀 = primært præklinisk
- 📊 = review/meta-analyse findes i eller bør kobles til sporet

## Executive status
FearPrime har nu en sammenhængende kerne:

```text
funktion/adaptation
      ↓
prediction + context
      ↓
threat/safety learning
      ↓
generalization / discrimination
      ↓
extinction / reconsolidation
      ↓
biologisk plasticitet
      ↓
retention + generalization + funktion
```

Efter v0.21 er de tidligere P0-huller og de definerede P1-moduler dækket på framework-/dossierniveau. Det største arbejde mod v1.0 er nu **study-level evidenskvalitet, reproducerbare søgninger, certainty, participant-overlap og maskinlæsbar datastruktur**.

---

# 1. Grundmodel og teori

| Del | Status | Filer | Hvad mangler før v1.0 |
|---|---|---|---|
| Funktionel/adaptiv PTSD-model | ✅ | `00_MANIFESTO/FEARPRIME_MODEL.md`, `05_MODELS/ADAPTIVE_PTSD_MODEL.md` | Flere direkte empiriske tests af adaptive vs rigide strategier |
| Klassiske PTSD-teorier | 🟡 | `05_MODELS/PTSD_THEORIES.md`, `07_STUDIES/THEORY/` | Nyere teori-reviews, prospektive tests, model-sammenligning |
| Predictive processing | 🟡 🔬 | adaptiv model + ressourcekategori | Dedikeret mekanisme-/teorifil og operationelle predictions |
| CPTSD | ✅/🟡 | `05_MODELS/CPTSD_MODEL.md`, `06_MEASUREMENT/CPTSD_MEASUREMENT.md` | Flere DSO-studiekort og longitudinelle mekanismedata |
| Selvmodel / identitet | 🟡 🔬 | CPTSD-model | Dedikeret spor for memory/identity og negativt selvkoncept |
| Social threat learning | 🟡 🔬 | CPTSD + generalization engine | Humane paradigmer og klinisk overførsel |

---

# 2. Fear / safety learning

| Del | Status | Filer | Hvad mangler |
|---|---|---|---|
| Fear acquisition | 🟡 | `EXTINCTION_ENGINE.md`, `LEARNING_METRICS.md` | Dedikeret acquisition/metodeoversigt |
| Extinction | ✅/🟡 | `EXTINCTION_ENGINE.md`, `LEARNING_METRICS.md` | Større paradigme-/metodebibliografi |
| Inhibitory learning | 🟡 | arbejdsmodeller + teorikort | Egen engine/strategikort |
| Expectancy violation | ✅/🟡 | arbejdsmodeller + learning metrics | Bedre paradigmestandardisering |
| Safety learning | ✅/🟡 | `GENERALIZATION_AND_SAFETY_LEARNING_ENGINE.md` | Flere PTSD-specifikke primærstudier |
| Threat/safety discrimination | ✅/🟡 | generalization engine + learning metrics + hippocampus/context | Populationsspecifik evidens |
| Generalization | ✅/🟡 | generalization engine + learning metrics | Perceptuel/social/interoceptiv evidens opdelt |
| Context learning | ✅/🟡 | `HIPPOCAMPUS_CONTEXT_DISCRIMINATION.md` | Flere study cards og kausale humane data |
| Extinction recall | ✅/🟡 | extinction/reconsolidation + learning metrics | Mere study-level standardisering |

FearPrime skelner eksplicit acquisition, extinction, delayed recall, generalization, renewal, reinstatement, spontaneous recovery og reacquisition.

---

# 3. Return of fear og reconsolidation

| Del | Status | Hvad mangler |
|---|---|---|
| Return of fear | ✅/🟡 | Mere samlet kvantitativ evidens |
| Retrieval | ✅ | Skal fortsat adskilles fra destabilisering |
| Reconsolidation | ✅/🟡 | Flere uafhængige humane replikationer |
| Boundary conditions | ✅/🟡 | Dedikeret modul + individuelle cards; systematisk meta-/RoB-niveau mangler |
| Klinisk PTSD-reconsolidation | ✅/🟡 | Flere fuldtekstudtræk, effect sizes og certainty |

[Reconsolidation boundary conditions](../03_EXTINCTION/RECONSOLIDATION_BOUNDARY_CONDITIONS.md) dækker prediction error, reminder duration, memory strength/age/type, context/state og timing.

**Skalaer:**
- M0–M4 = mekanistisk reconsolidation-inferens.
- R0–R4 = robusthed/replikation.

[Reconsolidation effect-size/RoB audit](RECONSOLIDATION_EFFECT_SIZE_ROB_AUDIT.md) er første P2-lag på dette domæne.

---

# 4. Neurocircuitry

| Del | Status | Hvad mangler |
|---|---|---|
| Masterkort | ✅ | `FEAR_CIRCUIT_MASTER_MAP.md` |
| Amygdala | 🟡 | Mere nuclei-/procesopdeling |
| vmPFC/mPFC | 🟡 | Extinction recall / valuation-dossier |
| Hippocampus/context | ✅/🟡 | Study cards, effect sizes, kausal human evidens |
| Insula/interoception | ✅/🟡 | Paradigmespecifik måling + study cards |
| dACC | 🟡 | Mere human task-evidens |
| BNST / sustained threat | 🔴/🟡 | Dedikeret litteraturspor |
| PAG / defensive output | 🟡 | Freeze/flight/fight-differentiering |
| HPA/stress-memory | ✅/🟡 | Fase-specifik human syntese + effect sizes |
| Netværksmodeller | 🟡 | SN/DMN/CEN og connectivity |

---

# 5. Molekylær plasticitet

| Del | Status | Hvad mangler |
|---|---|---|
| HDAC / epigenetik | ✅/🟡 🔬 | Human translation, isoform-specificitet |
| BDNF / TrkB | ✅/🟡 | Direkte human mekanismemåling |
| PNN / critical periods | ✅/🟡 🐀 | Human translation |
| Dopamin | ✅/🟡 | Fase- og dosisafhængighed |
| 5-HT7 / 5-HT1A | 🟡 🔬 | Direkte humane læringsdata |
| NMDA / AMPA | ✅/🟡 👤🐀📊 | `NMDA_AMPA_GLUTAMATE_PLASTICITY.md`; human AMPA-specifik fear-learning translation mangler |
| Endocannabinoider | ✅/🟡 👤🐀📊 | FAAH/CB1-dossier; uafhængig human replikation og klinisk PTSD-transfer mangler |
| Glucocorticoider | ✅/🟡 👤 | Timingmodul findes; effektstørrelser/CI mangler |
| GABA/glutamat-balance | 🔴/🟡 | Egen evidenssyntese uden “imbalance”-forenkling |
| Mitokondrier/metabolisme | 🟡 🔬 | Direkte kobling til fear learning mangler |

---

# 6. Farmakologisk / biologisk augmentation

## Dossiers på plads
- ✅ Butyrat
- ✅/🟡 Lurasidon
- 🟡 L-DOPA
- 🟡 Oxytocin
- ✅/🟡 HDAC2-selectivitet
- ✅/🟡 [D-cycloserin](../04_CANDIDATES/DCS_DOSSIER.md)
- ✅/🟡 [Propranolol](../04_CANDIDATES/PROPRANOLOL_DOSSIER.md)
- ✅/🟡 [Endocannabinoid/FAAH/CB1](../04_CANDIDATES/ENDOCANNABINOID_FAAH_CB1_DOSSIER.md)
- ✅/🟡 [NMDA/AMPA-mekanismesporet](../02_MECHANISMS/NMDA_AMPA_GLUTAMATE_PLASTICITY.md)

## Stadig delvist dækket
- 🟡 hydrokortison
- 🟡 mifepriston
- 🟡 ketamin
- 🟡 CBD
- 🟡 MDMA
- 🟡 psilocybin
- 🟡 hormoner
- 🟡 guanfacin
- 🟡 memantin
- 🟡/🔬 amisulprid

## V0.21-nøglefortolkninger
- DCS har stærk mekanistisk plausibilitet, men PTSD-RCT'er er blandede og større multisite data viser ingen stabil main effect.
- FAAH-hæmning har et direkte humant experimental-medicine signal for delayed extinction recall, men ikke etableret klinisk PTSD-efficacy.
- Propranolol har positive og negative kliniske trials samt modstridende meta-analyser; symptomændring må ikke bruges som direkte reconsolidation-bevis.

---

# 7. CPTSD, dissociation og defensive states

| Del | Status | Hvad mangler |
|---|---|---|
| CPTSD-definition/model | ✅ | v0.18-model |
| DSO measurement | ✅/🟡 | Flere interventions-/longitudinelle data |
| Dissociation | 🟡 | Eget målespor og state-dependent learning |
| Tonic immobility | 🟡/✅ | Review/meta findes; mekanismemodul mangler |
| Freeze / shutdown | 🟡 | Begrebs-/fysiologisk differentiering |
| Social threat | 🟡 🔬 | Eksperimentelle paradigmer |
| Attachment / relational safety | 🔴/🟡 | Skal adskilles fra generisk social støtte |

---

# 8. Somatiske og adfærdsmæssige moduler

| Del | Status | Hvad mangler |
|---|---|---|
| Exposure | ✅/🟡 | Udvidet engine og paradigmestandarder |
| TRE | ✅/🟡 | Begrænset evidenskvalitet; fortsat klare evidenslabels |
| Interoceptiv exposure | 🟡 | Integreret protokol-/målemodul |
| Motion | 🟡 | Timing omkring læring og retention |
| Søvn | 🟡 | Dedikeret sleep-memory consolidation-spor |
| Døgnrytme | 🟡 | Human fear-learning evidens |
| tVNS/autonom modulation | 🟡 🔬 | Replikation og klinisk translation |
| Åndedræt/autonom regulering | 🔴/🟡 | Adskil akut state regulation fra læring |

---

# 9. Measurement layer

## Eksisterer
- ✅ `MEASUREMENT_PLAN.md`
- ✅ `CPTSD_MEASUREMENT.md`
- ✅ `LEARNING_METRICS.md`
- ✅ `SESSION_TEMPLATE.md`
- ✅ `RETURN_OF_FEAR_TEMPLATE.md`
- ✅ `FP_BL_01_TEST_PLAN.md`
- ✅ `RISK_OF_BIAS_TEMPLATE.md`
- ✅/🟡 `RECONSOLIDATION_EFFECT_SIZE_ROB_AUDIT.md`

### Stadig åbent
- 🟡 fysiologi preprocessing/QC-standarder
- 🟡 dedikeret valideret funktionsinstrument-spor
- 🔴 maskinlæsbar session-schema

---

# 10. Evidensarkitektur

| Del | Status |
|---|---|
| Evidensregler | ✅ |
| Study ledger | ✅ |
| Source register | ✅ |
| Positive + negative fund | ✅ |
| Search logs | ✅ |
| Review/meta-kategori | ✅/🟡 |
| Claim-specific R0–R4 | ✅ |
| M0–M4 reconsolidation inference | ✅ |
| Risk-of-bias standard | ✅/🟡 template findes; study-level udfyldning mangler |
| Effektstørrelser systematisk | ✅/🟡 startet i reconsolidation-kernen |
| GRADE/certainty-lignende lag | 🔴 |
| Deltager-overlap-register | 🟡 |
| Preregistration-lignende hypothesis registry | 🔴/🟡 |

## V1.0-krav til centrale studiekort
```text
population
N
randomisering
blindning
kontrolgruppe
primært outcome
effektstørrelse + CI
frafald
preregistration
fund
modfund
FearPrime-relevans
certainty
```

---

# 11. Research reproducibility

## Mangler
🔴 maskinlæsbar study index (CSV/JSON/YAML)  
🔴 versionsnummer samlet ét sted  
🔴 changelog  
🟡 citation consistency check  
🟡 automatisk DOI/PMID-validering  
🟡 duplicate-publication kontrol  
🟡 automatisk link checker

## Forslag
```text
/data/studies.csv
/data/candidates.csv
/data/mechanisms.csv
/data/session_schema.yaml
CHANGELOG.md
VERSION
```

---

# 12. V1.0-prioriteret roadmap

## P0 — framework-kerne
1. ✅ CPTSD-model.
2. ✅ Fear Circuit Master Map.
3. ✅ Generalization & Safety Learning Engine.
4. ✅ Reconsolidation boundary conditions.
5. ✅ CPTSD measurement / ITQ-spor.
6. ✅ Learning metrics.

**P0 er afsluttet på framework-niveau.**

## P1 — høj værdi
7. ✅ Hippocampus/context discrimination.
8. ✅ Insula/interoception.
9. ✅ HPA/stress-memory timing.
10. ✅ NMDA/AMPA-mekanismemodul.
11. ✅ Endocannabinoid/FAAH/CB1-dossier.
12. ✅ DCS-dossier.
13. ✅ Propranolol-dossier.
14. ✅ Boundary-condition studiekort + negative replikationer + R0–R4 coding.

**De definerede P1-opgaver er nu dækket på framework-/dossierniveau.**

## P2 — evidensstyrke
15. ✅/🟡 Risk-of-bias template; udfyld study-level.
16. ✅/🟡 Effect sizes + CI startet for reconsolidation-kernen; udvid til DCS/FAAH/øvrige kandidater.
17. 🟡 Reproducerbare søgninger for hver P0/P1-domæne.
18. 🔴 Maskinlæsbar study database og session-schema.
19. 🔴 Certainty-lag.
20. 🟡 Participant-overlap register.

## P3 — v1.0-polering
21. samlet glossary-kontrol.
22. link-check.
23. changelog/version-fil.
24. README som komplet navigationskort.
25. særskilt `KNOWN_LIMITATIONS.md`.

---

# Definition af FearPrime v1.0
FearPrime bør først betegnes **v1.0**, når følgende er sandt:

- Kerneprocesserne threat, safety, context, generalization, extinction, reconsolidation og return of fear er særskilt dokumenteret.
- PTSD og CPTSD kan måles separat.
- Biologiske kandidater er mærket efter human/præklinisk/hypotetisk evidens.
- Negative studier og null-fund er integreret.
- Centrale påstande kan spores til primærkilder.
- Kerne-domænerne har reproducerbare litteratursøgninger.
- Learning outcomes og kliniske symptom-outcomes blandes ikke sammen.
- Frameworket har eksplicitte falsifikationskriterier.
- Centrale studier har RoB + effect sizes/CI eller eksplicit manglende data.
- Data- og versionsstrukturen kan læses både af mennesker og software.

## Samlet status
**FearPrime er efter v0.21 et sammenhængende pre-v1.0 framework med P0 og de definerede P1-moduler dækket.**

Det afgørende hul er nu **P2: evidensstyrke, reproducerbarhed og maskinlæsbar dataarkitektur** — ikke flere brede kernemodeller.
