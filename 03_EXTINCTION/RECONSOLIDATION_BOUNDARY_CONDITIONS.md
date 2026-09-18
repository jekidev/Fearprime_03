# FearPrime — reconsolidation boundary conditions

Version 0.23 · 2026-09-18

## Formål
Dette dokument definerer, hvornår FearPrime **må** og **ikke må** bruge reconsolidation som forklaring på memory updating.

Kerneprincippet er:

> Retrieval er ikke det samme som destabilisering, og en post-retrieval effekt er ikke automatisk reconsolidation.

Se også:
- [Extinction, reconsolidation og return of fear](EXTINCTION_RECONSOLIDATION_RETURN.md)
- [Klinisk PTSD-reconsolidation](CLINICAL_PTSD_RECONSOLIDATION.md)
- [Generalization & Safety Learning Engine](GENERALIZATION_AND_SAFETY_LEARNING_ENGINE.md)
- [Learning Metrics](../06_MEASUREMENT/LEARNING_METRICS.md)
- [Study Ledger og R0–R4 robusthed](../07_STUDIES/STUDY_LEDGER.md)

**Skala-afklaring:** Dette dokument bruger **M0–M4** til graden af *mekanistisk reconsolidation-inferens*. `STUDY_LEDGER.md` bruger separat **R0–R4** til *robusthed/replikation*. De to skalaer må ikke blandes.

---

# 1. Proceskæden

FearPrime skelner mellem:

```text
retrieval
   ↓
reactivation
   ↓
possible prediction error / novelty
   ↓
possible destabilization
   ↓
updating / interference
   ↓
restabilization (reconsolidation)
```

Det er ikke tilladt at springe direkte fra:

```text
memory retrieved
→ reconsolidation occurred
```

Den empiriske litteratur viser, at retrieval i sig selv kan være utilstrækkeligt til at fremkalde labilisering af en human fear memory.

Reference: Sevenster, Beckers & Kindt (2012), PMID 22406658, DOI `10.1016/j.nlm.2012.01.009`.

---

# 2. Boundary condition: prediction error

Prediction error (PE) er mismatch mellem forventet og observeret udfald.

Human fear-conditioning-data har vist, at PE kan være vigtig for at afgøre, om retrieval efterfølges af reconsolidation-relevant plasticitet.

### Centrale fund
Sevenster et al. (2013) viste i et human fear-conditioning paradigme, at prediction error var nødvendig for den observerede propranolol-sensitive effekt på learned fear.

Reference: PMID 23413355. DOI `10.1126/science.1231357`.

Sevenster et al. (2014) viste desuden, at graden/strukturen af prediction error kan være med til at afgrænse overgang mellem:

```text
retrieval
reconsolidation
new learning
```

Reference: PMID 25320349. DOI `10.1101/lm.035493.114`.

### FearPrime-regel
Prediction error øger plausibiliteten af destabilisering, men:

```text
PE ≠ bevis for reconsolidation
```

PE kan også drive extinction, new learning eller andre updating-processer.

### Replikationskontrol
Stemerding et al. (2022) forsøgte at replikere det præcise mønster, hvor én PE var reconsolidation-sensitiv, men fandt ikke evidens for den forventede specifikke effekt. Kontrolgruppernes fear retention gjorde samtidig fortolkningen mindre ren.

PMID `35145138` · DOI `10.1038/s41598-022-06119-5`.

Det betyder, at “én prediction error” **ikke** må bruges som en valideret universal klinisk regel.

### Nyere kvantificering af PE
Chen et al. (2025) brugte expectancy-data og en forenklet Rescorla–Wagner-model til at estimere graden af prediction error i et humant fear-conditioning paradigme. De rapporterede, at den faktisk estimerede PE ikke altid fulgte den simple operationelle kategori/antal forventningsbrud.

PMID `40570716` · DOI `10.1016/j.cognition.2025.106224`.

FearPrime bruger dette som støtte for:
```text
PE = gradueret/modelafhængig moderator
≠
universel binær “window open/window closed”-markør
```

Det nyere fund må ikke bruges post hoc til at forklare alle ældre replication failures.

---

# 3. Boundary condition: reminder/retrieval duration

Reminderens længde og informationsindhold kan ændre hvilken proces der dominerer.

For kort/forudsigelig retrieval kan give:

```text
retrieval uden tilstrækkelig destabilisering
```

Mere mismatch kan åbne et updating-vindue.

Men omfattende ikke-forstærket eksponering kan i stedet producere:

```text
new inhibitory learning / extinction
```

Derfor er “mere retrieval” ikke monotont lig med “mere reconsolidation”.

FearPrime modellerer dette som en procesovergang:

```text
for lidt ny information
        ↓
retrieval

passende mismatch
        ↓
possible destabilization/reconsolidation

omfattende ny læring
        ↓
extinction / new memory formation
```

De præcise grænser er paradigmeafhængige og kan ikke angives som én universel minutværdi.

---

# 4. Boundary condition: memory strength

Stærkere memories kan være mere resistente mod destabilisering i nogle paradigmer.

Mulige determinants:
- antal acquisition trials,
- reinforcement history,
- salience,
- emotional arousal,
- repetition,
- senere rehearsal/retrieval.

Men litteraturen viser ikke en simpel regel som:

```text
strong memory = cannot reconsolidate
```

Boundary conditions interagerer med reminderens egenskaber og prediction error.

Fernández et al. (2016) viste i humane declarative-memory tests, at strength/age-boundaries kan være dynamiske snarere end absolutte.

DOI `10.1016/j.nlm.2016.03.001`.

Paul & Asthana (2025) manipulerede reinforcement history/memory strength sammen med PE-relaterede retrievalbetingelser i et humant fear-conditioning paradigme. Resultatet var konsistent med, at stærkere memories kan være mere resistente mod den testede retrieval-extinction-manipulation.

PMID `40653191` · DOI `10.1016/j.neuroscience.2025.07.014`.

FearPrime behandler dette som et **nyere enkeltstudie om interaction mellem strength og PE**, ikke som en universel tærskel og ikke som direkte evidens om langvarige autobiografiske traumeminder.

---

# 5. Boundary condition: memory age

Alderen på et memory trace er ofte foreslået som en boundary condition.

Men en kritisk gennemgang af reconsolidation-litteraturen viser heterogene resultater: forskellige paradigmer finder forskellige tidsgrænser, og nogle finder ikke en simpel age-gradient.

FearPrime må derfor ikke bruge en universel regel såsom:

```text
“minder ældre end X dage/år kan ikke destabiliseres”
```

Memory age registreres som moderator, ikke som binær mekanismeafgørelse.

---

# 6. Boundary condition: memory type

Resultater fra én hukommelsestype må ikke automatisk overføres til en anden.

Skeln mindst mellem:

```text
simple Pavlovian fear conditioning
declarative memory
autobiographical memory
trauma memory
procedural/habit memory
reward/appetitive memory
```

Et laboratoriefund med billede–shock association dokumenterer ikke automatisk samme destabiliseringsbetingelser for et mangeårigt autobiografisk traumeminde.

Dette er en central translation-grænse i FearPrime.

---

# 7. Boundary condition: reminder specificity

En reminder skal matche det relevante memory trace tilstrækkeligt til at reaktivere det, men kan samtidig indeholde ny information.

FearPrime registrerer:
- cue identity,
- context,
- expected outcome,
- actual outcome,
- reminder duration,
- similarity til original læring,
- nye elementer.

Dette gør det muligt at skelne mellem:

```text
reactivation of target memory
vs
activation of adjacent/new associations
```

---

# 8. Boundary condition: context

Context kan påvirke både retrieval og hvilken memory representation der dominerer.

Relevant kontekst inkluderer:
- fysisk miljø,
- social kontekst,
- intern/interoceptiv state,
- tidspunkt,
- instruktioner,
- forventninger.

En ændring i context kan skabe prediction error, men kan også reducere retrieval af target trace.

Det er derfor ikke givet, at maksimal novelty er optimalt.

Se også [hippocampus/context discrimination](../02_MECHANISMS/HIPPOCAMPUS_CONTEXT_DISCRIMINATION.md).

---

# 9. Boundary condition: state

Mulige state-moderatorer omfatter:
- stress/arousal,
- søvn,
- hormoner,
- farmakologi,
- autonom tilstand,
- attention.

Der findes human evidens for at stress kan påvirke reconsolidation af declarative memory, men dette kan ikke direkte generaliseres til alle trauma-memory paradigmer.

Eksempel: Bos et al. (2014), PMID 24882163, DOI `10.1016/j.psyneuen.2014.04.011`.

Se også [HPA/stress-memory](../02_MECHANISMS/HPA_STRESS_MEMORY.md).

---

# 10. Boundary condition: intervention timing

Hvis en manipulation gives omkring retrieval, skal timing dokumenteres præcist.

Registrér:

```text
T_retrieval
T_intervention
T_extinction/new-learning
T_test
```

### Hvorfor
En effekt efter retrieval kan skyldes:
- encoding af ny information,
- extinction consolidation,
- state-dependent retrieval,
- performance-effekt,
- reconsolidation,
- nonspecific drug effect.

Timing alene beviser ikke mekanismen, men dårlig timing gør mekanistisk fortolkning svagere.

---

# 11. Reconsolidation vs extinction

FearPrime bruger følgende konceptuelle skel:

## Reconsolidation-hypotese
Den tidligere consolidated memory bliver destabiliseret og modificeret før restabilisering.

## Extinction-hypotese
En ny memory lærer noget i retning af:

```text
CS → no US / safety
```

som konkurrerer med den ældre association.

### Testmæssig forskel
Stærkere reconsolidation-påstande kræver mere end within-session fear reduction.

Undersøg fx:
- spontaneous recovery,
- renewal,
- reinstatement,
- reacquisition,
- længerevarende retention.

Selv fravær af return of fear er ikke alene definitivt bevis for, at det oprindelige trace er “slettet”.

---

# 12. Retrieval-extinction

Retrieval-extinction paradigmer forsøger at placere extinction i et tidsvindue efter memory reactivation.

FearPrime klassificerer dem som:

```text
reconsolidation-oriented behavioral updating
```

indtil designet faktisk kan skelne mellem:
- modification af original trace,
- stærkere extinction,
- context effects,
- interference,
- ordinary relearning.

Det klassiske Schiller-spor er derfor relevant, men ikke alene tilstrækkeligt til at konkludere permanent memory erasure.

Den registrerede direkte replikation af Chalkia et al. (2020) fandt ikke en fordel af retrieval+extinction over almindelig extinction til forebyggelse af recovery. Dette sænker robustheden af den specifikke procedure, men afviser ikke reconsolidation som biologisk proces.

---

# 13. Farmakologisk blockade som mekanismeprobe

Propranolol og andre manipulationer er blevet brugt som probes af post-reactivation-processer.

Men FearPrime kræver:

```text
reactivation condition
+ control condition
+ manipulation timing
+ delayed test
+ modality-specific outcomes
```

før en stærk reconsolidation-fortolkning.

Human forskning viser også dissociation mellem fear-potentiated startle, skin conductance og expectancy. Én outcome-kanal må derfor ikke generaliseres til “hele fear memory”.

---

# 14. Negative fund og replikationer er centrale

Reconsolidation-feltet indeholder både positive fund, failures og paradigmeafhængige resultater.

FearPrime kræver derfor, at et reconsolidation-dossier indeholder:

```text
positive studies
null findings
failed replications
boundary-condition explanations
alternative learning explanations
```

Boundary conditions må ikke bruges post hoc til at forklare ethvert negativt fund væk.

Hvis en boundary-condition-hypotese ikke var specificeret før data, markeres den som post hoc.

Centrale modfund omfatter:
- Wood et al. 2015: tre små negative kliniske PTSD-forsøg,
- Chalkia et al. 2020: registreret direkte retrieval-extinction-replikation uden forventet fordel,
- Roullet et al. 2021: ingen samlet propranololfordel i et større klinisk PTSD-RCT,
- Stemerding et al. 2022: mislykket replikation af det præcise single-PE boundary-mønster.

Se claim-specific robusthed i [Study Ledger](../07_STUDIES/STUDY_LEDGER.md).

---

# 15. M0–M4: mekanistisk inferens for reconsolidation claims

**Vigtigt:** M0–M4 beskriver *hvor stærkt et konkret design tillader reconsolidation som mekanismeinferens*. Det er separat fra R0–R4, som beskriver *robusthed/replikation* i Study Ledger.

## Niveau M0 — retrieval only
Memory blev genkaldt.

**Tilladt konklusion:** retrieval fandt sted.

## Niveau M1 — retrieval + prediction error
Der var dokumenteret mismatch/novel information.

**Tilladt konklusion:** destabilisering er mere plausibel.

## Niveau M2 — post-reactivation updating
En intervention efter reactivation ændrede senere responding relativt til relevante kontroller.

**Tilladt konklusion:** post-reactivation updating er understøttet.

## Niveau M3 — reconsolidation-consistent pattern
Designet viser:
- relevant reactivation,
- boundary-condition-sensitive effekt,
- delayed test,
- relevante kontroller,
- mønster konsistent med reconsolidation frem for enkel state/performance-effekt.

**Tilladt konklusion:** resultatet er reconsolidation-consistent.

## Niveau M4 — stærk mekanistisk inference
Flere uafhængige paradigmer/manipulationer og replikationer understøtter destabilisering + restabilisering af target memory.

**Tilladt konklusion:** stærk reconsolidation-inference.

FearPrime bruger meget sjældent ord som “erasure”.

---

# 16. Standardregistrering

Ved ethvert reconsolidation-orienteret studie registreres:

```yaml
memory_type: null
memory_age: null
memory_strength_proxy: null
original_learning: null
reactivation_cue: null
reactivation_duration: null
context_match: null
expected_outcome: null
observed_outcome: null
prediction_error_evidence: null
intervention: null
intervention_timing: null
new_learning_trials: null
delayed_test: null
outcomes:
  expectancy: null
  affect: null
  SCR: null
  startle: null
  behavior: null
return_of_fear:
  renewal: null
  reinstatement: null
  spontaneous_recovery: null
  reacquisition: null
alternative_explanations: []
mechanistic_inference_level: M0-M4
robustness_score: R0-R4
```

---

# 17. FearPrime beslutningstræ

```text
Blev target memory faktisk retrieved?
        |
        ├─ nej/uklart → ingen reconsolidation-påstand
        |
        └─ ja
            ↓
Var der dokumenteret ny information / prediction error?
            |
            ├─ nej → retrieval kan være utilstrækkelig til destabilisering
            |
            └─ ja
                ↓
Var reminder/new-learning så omfattende, at extinction/new learning er plausibel?
                |
                ├─ ja → konkurrerende forklaring skal testes
                |
                └─ nej/uklart
                    ↓
Findes delayed effect + egnet kontrol?
                    |
                    ├─ nej → kun svag mekanistisk inference
                    |
                    └─ ja
                        ↓
Er return-of-fear og alternative forklaringer testet?
                        |
                        ├─ nej → reconsolidation-consistent, ikke bevist
                        |
                        └─ ja → stærkere inference afhængigt af replikation
```

---

# 18. Klinisk translation til PTSD/CPTSD

Den største translation-fejl FearPrime skal undgå er:

```text
laboratory fear reconsolidation
=
trauma memory reconsolidation
```

De er relaterede forskningsområder, men ikke identiske.

Ved kliniske PTSD-studier registreres derfor særskilt:
- type af trauma memory/reactivation,
- symptom-outcome,
- fysiologisk outcome,
- funktionsoutcome,
- kontrolbetingelse,
- om studiet faktisk manipulerer den antagede reconsolidation-proces.

Klinisk symptomreduktion kan være reel uden at reconsolidation er den dokumenterede mekanisme.

---

# 19. Centrale reviews

### Fernández, Boccia & Pedreira 2016
*The fate of memory: Reconsolidation and the case of Prediction Error.* Neurosci Biobehav Rev. PMID 27287939. DOI `10.1016/j.neubiorev.2016.06.004`.

Kernepunkt: prediction error, memory strength og age indgår som centrale boundary-condition-spor.

### Fernández et al. 2016
*The dynamic nature of the reconsolidation process and its boundary conditions: Evidence based on human tests.* Neurobiol Learn Mem. DOI `10.1016/j.nlm.2016.03.001`.

Kernepunkt: boundary conditions er dynamiske og afhænger af interaktionen mellem memory- og reminder-egenskaber.

### Appraising reconsolidation theory and its empirical validation
Kritisk review: boundary-condition-resultater er blandede, og præcise grænser varierer mellem paradigmer.

### Chen et al. 2025
*How Fear Memory is Updated: From Reconsolidation to Extinction?* Neurosci Bull. 2025.

Kernepunkt: reconsolidation og extinction bør forstås som relaterede, men forskellige updating-processer med betingelsesafhængige overgange.

---

# 20. 2025–2026-opdatering: boundary conditions og farmakologisk konvergens

Et nyere systematisk review af akut farmakologisk manipulation af human aversiv hukommelse (Xia, Quednow & Bach 2026; PMID `41513054`; DOI `10.1016/j.neubiorev.2026.106548`) vurderer evidensen for propranolols påvirkning af reconsolidation i raske humane laboratorieparadigmer som relativt stærk sammenlignet med andre compounds/stadier.

FearPrime-regel:
```text
human laboratory convergence
≠
clinical PTSD efficacy
≠
universal reliable reconsolidation-window induction
```

Dette review sameksisterer derfor med de blandede kliniske propranolol-resultater og de negative retrieval-extinction-replikationer.

# 21. 2026-opdatering: dopamine/novelty

Nyere review-litteratur fremhæver dopamine og salient novelty som mulige mekanismer, der kan påvirke prediction-error-signaler og hjælpe med at overvinde visse boundary conditions.

Dette er mekanistisk plausibilitet, ikke dokumentation for at dopaminerg augmentation generelt forbedrer klinisk trauma-memory reconsolidation.

Reference: *Breaking boundaries: Dopamine’s role in prediction error, salient novelty, and memory reconsolidation.* Neuroscience. 2026;594:31–41. DOI `10.1016/j.neuroscience.2025.12.038`.

Dette spor kobles til [HDAC/BDNF/5-HT7/dopamin-mekanismedokumentet](../02_MECHANISMS/HDAC_BDNF_5HT7_DOPAMINE.md), men holdes som separat hypotese.

---

# 21. Falsifikationskriterier

FearPrimes reconsolidation-model svækkes, hvis:

1. dokumenteret prediction error ikke modererer post-reactivation updating i relevante replikationer,
2. de samme effekter opstår uden target-memory reactivation,
3. effekten forklares lige så godt af state/performance eller almindelig extinction,
4. alleged reconsolidation-effekter ikke holder ved delayed test,
5. return-of-fear-profiler ikke adskiller sig fra almindelig extinction,
6. boundary conditions kun bruges efterfølgende til at redde negative fund.

---

# 22. Praktisk evidensregel

FearPrime skriver aldrig:

```text
“Dette minde blev reconsolidated/slettet.”
```

på baggrund af retrieval + symptomlettelse alene.

Foretrukne formuleringer:

```text
“post-reactivation updating”
“reconsolidation-oriented design”
“resultat konsistent med reconsolidation”
“mekanismen er ikke isoleret fra extinction/new learning”
```

indtil evidensen retfærdiggør stærkere mekanistisk sprog.

---

# Status

P0-hullet om reconsolidation boundary conditions er dækket på framework-niveau, og v0.20 har nu:
1. individuelle kort for centrale boundary-condition-studier,
2. systematisk integration af negative replikationer,
3. **M0–M4** for mekanistisk inferens,
4. **R0–R4** i Study Ledger for robusthed/replikation.

Næste niveau er effektstørrelser, risk-of-bias og en maskinlæsbar study database.