# FearPrime v1.0 — gap-audit

Dato: 2026-09-17  
Status efter version 0.18

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

Det største arbejde mod v1.0 ligger ikke længere i at opfinde en grundidé, men i at gøre hvert led **målbart, kildekomplet og falsificerbart**.

---

# 1. Grundmodel og teori

| Del | Status | Filer | Hvad mangler før v1.0 |
|---|---|---|---|
| Funktionel/adaptiv PTSD-model | ✅ | `00_MANIFESTO/FEARPRIME_MODEL.md`, `05_MODELS/ADAPTIVE_PTSD_MODEL.md` | Flere direkte empiriske tests af adaptive vs rigide strategier |
| Klassiske PTSD-teorier | 🟡 | `05_MODELS/PTSD_THEORIES.md`, `07_STUDIES/THEORY/` | Nyere teori-reviews, prospektive tests, bedre model-sammenligning |
| Predictive processing | 🟡 🔬 | adaptiv model + ressourcekategori | Dedikeret mekanisme-/teorifil og operationelle predictions |
| CPTSD | ✅/🟡 | `05_MODELS/CPTSD_MODEL.md` | ITQ-målemodul, DSO-studiekort, longitudinelle mekanismedata |
| Selvmodel / identitet | 🟡 🔬 | CPTSD-model | Dedikeret spor for memory/identity og negativt selvkoncept |
| Social threat learning | 🟡 🔬 | CPTSD + generalization engine | Humane paradigmer og klinisk overførsel |

## V1.0-krav
- CPTSD skal have separat måling.
- Predictive-processing-påstande skal omsættes til målbare predictions.
- FearPrime skal tydeligt skelne teori, mekanisme og klinisk effekt.

---

# 2. Fear / safety learning

| Del | Status | Filer | Hvad mangler |
|---|---|---|---|
| Fear acquisition | 🟡 | `EXTINCTION_ENGINE.md`, studieregister | Dedikeret oversigt over acquisition og målemetoder |
| Extinction | ✅/🟡 | `EXTINCTION_ENGINE.md` | Større metode- og boundary-condition-del |
| Inhibitory learning | 🟡 | arbejdsmodeller + teorikort | Egen engine/strategikort |
| Expectancy violation | 🟡 | arbejdsmodeller | Formaliseret målemodel |
| Safety learning | ✅/🟡 | `GENERALIZATION_AND_SAFETY_LEARNING_ENGINE.md` | Flere PTSD-specifikke primærstudier |
| Threat/safety discrimination | 🟡 | generalization engine | Standardiseret målemodul |
| Generalization | ✅/🟡 | generalization engine | Perceptuel/social/interoceptiv evidens opdelt |
| Context learning | 🟡 | adaptive model + extinction | Dedikeret hippocampus/context-fil |
| Extinction recall | 🟡 | extinction/reconsolidation | Dedikerede outcome-standarder |

## V1.0-krav
FearPrime skal kunne skelne mindst:

```text
acquisition
extinction
extinction recall
generalization
renewal
reinstatement
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
| Boundary conditions | 🔴 | Egen fil: alder/styrke af memory, prediction error, retrieval-varighed, timing |
| Klinisk PTSD-reconsolidation | ✅/🟡 | Nyere trials, registre og meta-analytisk syntese |

## Høj prioritet
Opret:
`03_EXTINCTION/RECONSOLIDATION_BOUNDARY_CONDITIONS.md`

Dette er et af de vigtigste resterende konceptuelle huller.

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
| CPTSD-definition/model | ✅ | Ny v0.18-model |
| DSO | 🟡 | Måling + interventionsstudier |
| Dissociation | 🟡 | Eget målespor og state-dependent learning |
| Tonic immobility | 🟡/✅ | Review/meta findes; mekanismemodul mangler |
| Freeze / shutdown | 🟡 | Skelnen mellem begreber og fysiologi |
| Social threat | 🟡 🔬 | Eksperimentelle paradigmer |
| Attachment / relational safety | 🔴/🟡 | Skal adskilles fra generisk social støtte |

---

# 8. Somatiske og adfærdsmæssige moduler

| Del | Status | Hvad mangler |
|---|---|---|
| Exposure | ✅/🟡 | Udvidet engine og outcome-standarder |
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
- ✅ `SESSION_TEMPLATE.md`
- ✅ `RETURN_OF_FEAR_TEMPLATE.md`
- ✅ `FP_BL_01_TEST_PLAN.md`

## Mangler før v1.0

### 🔴 CPTSD measurement
- ITQ-reference og scoringprincipper
- PTSD og DSO separat
- funktion separat

### 🔴 Learning metrics
Standardfelter for:
- threat expectancy,
- safety expectancy,
- prediction error,
- discrimination,
- extinction slope,
- next-day recall,
- generalization transfer,
- renewal/reinstatement.

### 🟡 fysiologi
Definér hvad der kan måles uden at blande:
- HR/HRV,
- SCR,
- startle,
- respiration,
- subjektiv distress.

### 🟡 funktion
Der mangler en stærkere funktionsakse end symptom-score alene.

## Høj prioritet
Opret:
- `06_MEASUREMENT/CPTSD_MEASUREMENT.md`
- `06_MEASUREMENT/LEARNING_METRICS.md`

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
| GRADE/certeainty-lignende lag | 🔴 |
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
Senere:

```text
/data/studies.csv
/data/candidates.csv
/data/mechanisms.csv
CHANGELOG.md
VERSION
```

Det vil gøre repoet langt lettere at analysere med scripts/agenter.

---

# 12. V1.0-prioriteret roadmap

## P0 — nødvendigt
1. ✅ CPTSD-model.
2. ✅ Fear Circuit Master Map.
3. ✅ Generalization & Safety Learning Engine.
4. 🔴 Reconsolidation boundary conditions.
5. 🔴 CPTSD measurement / ITQ-spor.
6. 🔴 Learning metrics.
7. 🟡 Opdatér coverage-plan og README til v0.18.

## P1 — høj værdi
8. Hippocampus/context discrimination.
9. Insula/interoception.
10. HPA/stress-memory timing.
11. NMDA/AMPA-dossier.
12. Endocannabinoid-dossier.
13. DCS-dossier.
14. Propranolol-dossier.

## P2 — evidensstyrke
15. Risk-of-bias template.
16. Effektstørrelser + CI i kerne-studier.
17. Systematiske søgninger for hver P0/P1-domæne.
18. Maskinlæsbar study database.

## P3 — v1.0-polering
19. samlet glossary-kontrol.
20. link-check.
21. changelog/version-fil.
22. README som komplet navigationskort.
23. særskilt `KNOWN_LIMITATIONS.md`.

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
**FearPrime er efter v0.18 et sammenhængende pre-v1.0 framework.**

Det mest afgørende hul er ikke længere selve PTSD-modellen. Det er overgangen fra teori til **standardiserede mål + boundary conditions + systematisk evidenssyntese**.
