# FearPrime v1.0 — gap-audit

Dato: 2026-09-17  
Status efter version 0.19

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

Efter v0.19 er de tidligere seks P0-framework-huller dækket på dokument-/måleniveau. Det største arbejde mod v1.0 er nu **dybere evidensdækning, mekanismeopdeling, risk-of-bias og reproducerbar datastruktur**.

---

# 1. Grundmodel og teori

| Del | Status | Filer | Hvad mangler før v1.0 |
|---|---|---|---|
| Funktionel/adaptiv PTSD-model | ✅ | `00_MANIFESTO/FEARPRIME_MODEL.md`, `05_MODELS/ADAPTIVE_PTSD_MODEL.md` | Flere direkte empiriske tests af adaptive vs rigide strategier |
| Klassiske PTSD-teorier | 🟡 | `05_MODELS/PTSD_THEORIES.md`, `07_STUDIES/THEORY/` | Nyere teori-reviews, prospektive tests, bedre model-sammenligning |
| Predictive processing | 🟡 🔬 | adaptiv model + ressourcekategori | Dedikeret mekanisme-/teorifil og operationelle predictions |
| CPTSD | ✅/🟡 | `05_MODELS/CPTSD_MODEL.md`, `06_MEASUREMENT/CPTSD_MEASUREMENT.md` | Flere DSO-studiekort og longitudinelle mekanismedata |
| Selvmodel / identitet | 🟡 🔬 | CPTSD-model | Dedikeret spor for memory/identity og negativt selvkoncept |
| Social threat learning | 🟡 🔬 | CPTSD + generalization engine | Humane paradigmer og klinisk overførsel |

## V1.0-krav
- ✅ CPTSD har separat measurement-layer.
- Predictive-processing-påstande skal omsættes yderligere til målbare predictions.
- FearPrime skal fortsat tydeligt skelne teori, mekanisme og klinisk effekt.

---

# 2. Fear / safety learning

| Del | Status | Filer | Hvad mangler |
|---|---|---|---|
| Fear acquisition | 🟡 | `EXTINCTION_ENGINE.md`, `LEARNING_METRICS.md`, studieregister | Dedikeret acquisition/metodeoversigt |
| Extinction | ✅/🟡 | `EXTINCTION_ENGINE.md`, `LEARNING_METRICS.md` | Større paradigme- og metodebibliografi |
| Inhibitory learning | 🟡 | arbejdsmodeller + teorikort | Egen engine/strategikort |
| Expectancy violation | ✅/🟡 | arbejdsmodeller + learning metrics | Bedre paradigmestandardisering |
| Safety learning | ✅/🟡 | `GENERALIZATION_AND_SAFETY_LEARNING_ENGINE.md` | Flere PTSD-specifikke primærstudier |
| Threat/safety discrimination | ✅/🟡 | generalization engine + learning metrics | Paradigme-/populationsspecifik evidens |
| Generalization | ✅/🟡 | generalization engine + learning metrics | Perceptuel/social/interoceptiv evidens opdelt |
| Context learning | 🟡 | adaptive model + extinction | Dedikeret hippocampus/context-fil |
| Extinction recall | ✅/🟡 | extinction/reconsolidation + learning metrics | Mere study-level standardisering |

## V1.0-krav
FearPrime skelner nu eksplicit:

```text
acquisition
extinction
extinction recall
generalization
renewal
reinstatement
spontaneous recovery
reacquisition
```

uden at bruge dem som synonymer.

---

# 3. Return of fear og reconsolidation

| Del | Status | Hvad mangler |
|---|---|---|
| Return of fear | ✅/🟡 | Samlet kvantitativ evidens for renewal/reinstatement/spontaneous recovery |
| Retrieval | ✅ | Skal fortsat adskilles fra destabilisering |
| Reconsolidation | ✅/🟡 | Flere replikationer, negative studier og paradigmeforskelle |
| Boundary conditions | ✅/🟡 | `RECONSOLIDATION_BOUNDARY_CONDITIONS.md`; individuelle studiekort + R0–R4 coding mangler |
| Klinisk PTSD-reconsolidation | ✅/🟡 | Nyere trials, registre og meta-analytisk syntese |

## v0.19-opdatering
[Reconsolidation boundary conditions](../03_EXTINCTION/RECONSOLIDATION_BOUNDARY_CONDITIONS.md) dækker nu:
- prediction error,
- reminder/retrieval duration,
- memory strength,
- memory age,
- memory type,
- reminder specificity,
- context/state,
- intervention timing,
- reconsolidation versus extinction,
- evidensniveau R0–R4.

Boundary conditions må ikke bruges post hoc som universalforklaring på negative resultater.

---

# 4. Neurocircuitry

| Del | Status | Hvad mangler |
|---|---|---|
| Masterkort | ✅ | `02_MECHANISMS/FEAR_CIRCUIT_MASTER_MAP.md` |
| Amygdala | 🟡 | Mere nuclei-/procesopdeling |
| vmPFC/mPFC | 🟡 | Extinction recall og valuation-kilder |
| Hippocampus | 🟡 | Dedikeret context/discrimination-fil |
| Insula | 🟡 | Dedikeret interoception-fil |
| dACC | 🟡 | Trusselsudtryk og konflikt |
| BNST / sustained threat | 🔴/🟡 | Dedikeret litteraturspor |
| PAG / defensive output | 🟡 | Freeze/flight/fight-mekanismer |
| Striatum | 🟡 | Dopamin/prediction-error-kobling |
| Netværksmodeller | 🟡 | SN/DMN/CEN og connectivity |

## V1.0-krav
Minimum tre særskilte mekanismefiler:
1. `HIPPOCAMPUS_CONTEXT_DISCRIMINATION.md`
2. `INSULA_INTEROCEPTION.md`
3. `HPA_STRESS_MEMORY.md`

---

# 5. Molekylær plasticitet

| Del | Status | Hvad mangler |
|---|---|---|
| HDAC / epigenetik | ✅/🟡 🔬 | Human translation, isoform-specificitet |
| BDNF / TrkB | ✅/🟡 | Direkte human mekanismemåling |
| PNN / critical periods | ✅/🟡 🐀 | Human translation |
| Dopamin | ✅/🟡 | Fase- og dosisafhængighed |
| 5-HT7 / 5-HT1A | 🟡 🔬 | Direkte humane læringsdata |
| NMDA / AMPA | 🟡 | Dedikeret mekanismedossier |
| Endocannabinoider | 🟡 👤🐀 | Dossier og klinisk translation |
| Glucocorticoider | 🟡 👤 | Timing: acquisition vs retrieval vs consolidation |
| GABA/glutamat-balance | 🔴/🟡 | Egen evidenssyntese uden “imbalance”-forenkling |
| Mitokondrier/metabolisme | 🟡 🔬 | Direkte kobling til fear learning mangler |

---

# 6. Farmakologisk / biologisk augmentation

## Godt dækket
- ✅ Butyrat
- ✅/🟡 Lurasidon
- 🟡 L-DOPA
- 🟡 Oxytocin
- ✅/🟡 HDAC2-selectivitet som forskningsspor

## Kandidater med studiekort, men uden fuldt dossier
- 🟡 D-cycloserin
- 🟡 propranolol
- 🟡 hydrokortison
- 🟡 mifepriston
- 🟡 ketamin
- 🟡 CBD
- 🟡 FAAH/CB1
- 🟡 MDMA
- 🟡 psilocybin
- 🟡 hormoner
- 🟡 guanfacin
- 🟡 memantin

## Primære dossier-huller
Opret senere:
1. `DCS_DOSSIER.md`
2. `PROPRANOLOL_DOSSIER.md`
3. `GLUCOCORTICOID_DOSSIER.md`
4. `ENDOCANNABINOID_DOSSIER.md`
5. `NMDA_AMPA_DOSSIER.md`
6. `AMISULPRIDE_DOSSIER.md`

## Lavere prioritet / eksplorativt
Bromantan, tyrosin, lithium, 7,8-DHF, NAC og systemiske vaskulære kandidater bør forblive 🔬 indtil direkte relevans for FearPrime-outcomes er dokumenteret.

---

# 7. CPTSD, dissociation og defensive states

| Del | Status | Hvad mangler |
|---|---|---|
| CPTSD-definition/model | ✅ | v0.18-model |
| DSO measurement | ✅/🟡 | ITQ-layer findes; flere interventions-/longitudinelle data mangler |
| Dissociation | 🟡 | Eget målespor og state-dependent learning |
| Tonic immobility | 🟡/✅ | Review/meta findes; mekanismemodul mangler |
| Freeze / shutdown | 🟡 | Skelnen mellem begreber og fysiologi |
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

## Eksisterer efter v0.19
- ✅ `MEASUREMENT_PLAN.md`
- ✅ `CPTSD_MEASUREMENT.md`
- ✅ `LEARNING_METRICS.md`
- ✅ `SESSION_TEMPLATE.md`
- ✅ `RETURN_OF_FEAR_TEMPLATE.md`
- ✅ `FP_BL_01_TEST_PLAN.md`

### ✅ CPTSD measurement
Det nye modul indeholder:
- ITQ-reference og scoringprincipper uden kopiering af questionnaire-items,
- PTSD og DSO separat,
- funktion separat,
- probable classification adskilt fra klinisk diagnose,
- versions-/sprog-/clinical-check metadata.

### ✅ Learning metrics
Standardfelter er nu defineret for:
- threat expectancy,
- safety expectancy,
- prediction error,
- discrimination,
- acquisition,
- extinction change/slope,
- delayed recall,
- generalization gradient,
- renewal,
- reinstatement,
- spontaneous recovery,
- reacquisition,
- behavior/function og fysiologi.

### 🟡 fysiologi
Modaliteter er konceptuelt adskilt:
- HR/HRV,
- SCR,
- startle,
- respiration,
- subjektiv distress.

Der mangler stadig preprocessing/QC-standarder.

### 🟡 funktion
Funktionsaksen er styrket, men et dedikeret valideret funktionsinstrument-spor kan tilføjes senere.

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
| Effektstørrelser systematisk | 🟡 |
| Risk-of-bias standard | 🔴/🟡 |
| GRADE/certainty-lignende lag | 🔴 |
| Registrering af deltager-overlap | 🟡 |
| Preregistration-lignende hypothesis registry | 🔴/🟡 |

## V1.0-krav
Tilføj en standard til hvert centralt studiekort:

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
🔴 En maskinlæsbar study index (CSV/JSON/YAML)  
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

Det vil gøre repoet langt lettere at analysere med scripts/agenter.

---

# 12. V1.0-prioriteret roadmap

## P0 — framework-kerne
1. ✅ CPTSD-model.
2. ✅ Fear Circuit Master Map.
3. ✅ Generalization & Safety Learning Engine.
4. ✅ Reconsolidation boundary conditions.
5. ✅ CPTSD measurement / ITQ-spor.
6. ✅ Learning metrics.
7. ✅ Coverage-plan opdateret til v0.19.

**P0 er nu afsluttet på framework-niveau.** Det er ikke det samme som komplet systematisk evidensdækning.

## P1 — høj værdi
8. Hippocampus/context discrimination.
9. Insula/interoception.
10. HPA/stress-memory timing.
11. NMDA/AMPA-dossier.
12. Endocannabinoid-dossier.
13. DCS-dossier.
14. Propranolol-dossier.
15. Boundary-condition studiekort + negative replikationer + R0–R4 coding.

## P2 — evidensstyrke
16. Risk-of-bias template.
17. Effektstørrelser + CI i kerne-studier.
18. Systematiske søgninger for hver P0/P1-domæne.
19. Maskinlæsbar study database og session-schema.

## P3 — v1.0-polering
20. samlet glossary-kontrol.
21. link-check.
22. changelog/version-fil.
23. README som komplet navigationskort.
24. særskilt `KNOWN_LIMITATIONS.md`.

---

# Definition af FearPrime v1.0
FearPrime bør først betegnes **v1.0**, når følgende er sandt:

- Kerneprocesserne threat, safety, context, generalization, extinction, reconsolidation og return of fear er særskilt dokumenteret.
- PTSD og CPTSD kan måles separat.
- Biologiske kandidater er mærket efter human/præklinisk/hypotetisk evidens.
- Negative studier og null-fund er integreret.
- Centrale påstande kan spores til primærkilder.
- Mindst kerne-domænerne har en reproducerbar litteratursøgning.
- Learning outcomes og kliniske symptom-outcomes blandes ikke sammen.
- Frameworket har eksplicitte falsifikationskriterier.
- Data- og versionsstrukturen kan læses både af mennesker og software.

## Samlet status
**FearPrime er efter v0.19 et sammenhængende pre-v1.0 framework med P0-kernen dækket.**

Det afgørende hul er nu ikke grundmodellen eller de centrale målebegreber. Næste fase er **P1-mekanismer + systematisk study-level evidens + reproducerbar dataarkitektur**.
