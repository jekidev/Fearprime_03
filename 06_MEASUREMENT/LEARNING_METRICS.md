# FearPrime — learning metrics

Version 0.19 · 2026-09-17

## Formål
Dette dokument standardiserer FearPrimes mål for **fear/safety learning**. Målet er at undgå, at “mindre angst” bruges som erstatning for alle læringsprocesser.

Se også:
- [Måleplan](MEASUREMENT_PLAN.md)
- [CPTSD measurement](CPTSD_MEASUREMENT.md)
- [Generalization & Safety Learning Engine](../03_EXTINCTION/GENERALIZATION_AND_SAFETY_LEARNING_ENGINE.md)
- [Extinction Engine](../03_EXTINCTION/EXTINCTION_ENGINE.md)
- [Return of Fear Template](../03_EXTINCTION/RETURN_OF_FEAR_TEMPLATE.md)

---

## 1. Grundregel: hold målemodaliteter adskilt

FearPrime skelner mellem mindst fire outputtyper:

1. **expectancy/cognition** — hvad forventes at ske?
2. **affect/distress** — hvor ubehageligt/farligt føles det?
3. **behavior/function** — hvad gør personen faktisk?
4. **physiology** — fx SCR, startle, puls/HRV eller respiration.

En ændring i ét lag dokumenterer ikke automatisk ændring i de andre.

Den opdeling er vigtig, fordi human fear-conditioning-litteratur ofte viser forskellige resultater på forskellige mål. En opdateret meta-analyse fra 2025 fandt bl.a. forskelle i respons til safety cue (CS−), threat cue (CS+) og extinction recall, men ikke et ensartet mønster på tværs af alle mål og differensscores.

Reference: Kausche FM, Carsten HP, Sobania KM, Riesel A. 2025. *Fear and safety learning in anxiety- and stress-related disorders: An updated meta-analysis.* Neurosci Biobehav Rev. DOI `10.1016/j.neubiorev.2024.105983`.

---

# 2. Standardbegreber

## CS+
Stimulus der i acquisition-fasen er forbundet med et aversivt udfald (US) efter paradigmet.

## CS−
Stimulus der fungerer som safety cue / ikke-forstærket sammenligningsstimulus.

## US
Det udfald som deltageren forventer, fx et aversivt stimulus i laboratorieparadigmet.

## GS
Generalization stimulus: et nyt stimulus der deler egenskaber med en trænet stimulus.

I hverdags-/kliniske FearPrime-opgaver bruges disse begreber kun analogt, når designet faktisk understøtter sammenligningen.

---

# 3. Threat expectancy

## Definition
Forventet sandsynlighed for et præcist defineret negativt udfald.

Standard:

```text
0–100 %
```

Eksempel:

```text
“Hvis jeg går ind i butikken, bliver jeg tydeligt afvist.”
Threat expectancy = 75 %
```

Udfaldet skal defineres **før** opgaven, ellers kan målet flyttes bagefter.

---

# 4. Safety expectancy

## Definition
Forventet sandsynlighed for et præcist defineret sikkert/ikke-aversivt udfald.

Det er ikke altid blot `100 - threat expectancy`, fordi flere udfald kan være mulige og usikkerhed kan være høj.

Registrér derfor safety expectancy separat, hvis forskningsspørgsmålet handler om safety learning.

---

# 5. Prediction error

Prediction error (PE) beskriver forskellen mellem forventet og observeret udfald.

## Binært udfald
Hvis et udfald kodes som:

```text
aversivt udfald = 100
ikke-aversivt udfald = 0
```

kan en simpel signed PE defineres som:

```text
PE_signed = observed_outcome - expected_outcome
```

Eksempel:

```text
forventet fare = 80
observeret fare = 0
PE_signed = -80
```

For FearPrime kan **absolute expectancy violation** også rapporteres:

```text
PE_absolute = |observed - expected|
```

### Kritisk begrænsning
Dette er en **projektdeskriptiv beregning**, ikke et direkte neuralt mål for dopaminerg prediction error eller dokumentation for reconsolidation.

Prediction error kan understøtte flere former for læring og er ikke specifik for reconsolidation.

---

# 6. Threat/safety discrimination

## Standard differensscore

```text
Discrimination = response(CS+) - response(CS−)
```

Kan beregnes separat for:
- expectancy,
- affect,
- SCR,
- startle,
- andre prædefinerede mål.

### Fortolkning
Højere differens betyder større forskel mellem threat- og safety-cue på den valgte målemodalitet.

Men differensscore må altid vises sammen med rå CS+ og CS− værdier.

Hvorfor: samme differens kan opstå ved meget forskellige profiler.

Eksempel:

```text
Person A: CS+ 80, CS− 20 → Δ = 60
Person B: CS+ 100, CS− 40 → Δ = 60
```

De har samme differens, men Person B reagerer stærkere på både threat og safety cue.

---

# 7. Acquisition

Fear acquisition beskrives mindst med:

```text
early acquisition CS+
early acquisition CS−
late acquisition CS+
late acquisition CS−
```

og, hvor muligt:

```text
ΔCS early
ΔCS late
```

Undgå kun at bruge sidste trial som repræsentation af hele acquisition-fasen.

Hvis der er tilstrækkeligt mange trials, kan en trial-level model eller regressionshældning bruges.

---

# 8. Extinction learning

Extinction er ikke bare lavere distress efter en session.

Minimum:

```text
early extinction
late extinction
```

for relevante mål.

## Enkel deskriptiv ændring

```text
Extinction change = early_extinction - late_extinction
```

For mål hvor høj værdi = mere threat/fear giver positiv værdi således større reduktion.

## Trial-level slope

Ved tilstrækkeligt antal trials:

```text
response ~ trial_number
```

Slope rapporteres som et læringsmål.

### Kritisk kontrol
En lineær slope kan være misvisende ved ikke-lineær læring. Rå trial-data og kurve bør bevares.

---

# 9. Extinction recall / retention

Extinction recall måles efter en tidsforsinkelse og holdes adskilt fra within-session extinction.

Minimum:

```text
end_of_extinction
next_day_recall
```

### Retention difference

```text
Recall_difference = recall_response - end_extinction_response
```

For fear-mål betyder positiv værdi mere returneret respons ved recall.

### Alternativ
Rapportér rå recall til CS+ og CS− samt ΔCS. Dette er ofte mere transparent end ét samlet indeks.

---

# 10. Generalization

Generalization skal undersøge respons på nye stimuli/kontekster, ikke bare gentagelse af samme cue.

Minimumsstruktur:

```text
CS+
GS_high_similarity
GS_medium_similarity
GS_low_similarity
CS−
```

hvis paradigmet tillader det.

## Generalization gradient

Rapportér respons som funktion af lighed med CS+.

Mulige summaries:
- lineær/nonlineær slope,
- area under curve (AUC),
- respons på hver GS,
- threshold for kategorisering som threat.

Ingen enkelt metric gøres obligatorisk på tværs af alle paradigmer.

En 2025 narrative review viser, at extinction-læring ikke nødvendigvis generaliserer ens afhængigt af, om extinction blev trænet direkte på CS eller på generalization stimuli. Generalisering skal derfor måles, ikke antages.

Reference: Wong AHK. 2025. *Spreading the reduction of fear: A narrative review of generalization of extinction learning in human fear conditioning.* Clin Psychol Rev. PMID 40184732. DOI `10.1016/j.cpr.2025.102580`.

---

# 11. Renewal

Renewal = return of fear ved kontekstskift efter extinction.

Eksempelstruktur:

```text
acquisition: context A
extinction:  context B
recall:      context A eller ny context C
```

Deskriptivt:

```text
Renewal = response_test_context - response_end_extinction
```

Rapportér råværdier og kontekst, ikke kun differensen.

---

# 12. Reinstatement

Reinstatement = øget conditioned responding efter usignaleret præsentation af US eller anden paradigmespecifik reinstatement-manipulation.

Deskriptivt:

```text
Reinstatement = post_reinstatement_response - pre_reinstatement_response
```

Dette må ikke bruges om enhver naturlig symptomforværring.

I hverdagsdata kan “reinstatement-like” kun bruges som analog hypotese, medmindre et egnet eksperimentelt design findes.

---

# 13. Spontaneous recovery

Spontaneous recovery = tilbagekomst af conditioned responding over tid efter extinction uden nødvendigvis kontekstskift eller reinstatement-manipulation.

Minimum:

```text
end_extinction
follow_up_time
same_or_documented_context
```

Tid siden extinction registreres eksplicit.

---

# 14. Reacquisition

Reacquisition undersøger hvor hurtigt en tidligere extingueret association genlæres ved ny reinforcement.

Det er konceptuelt forskelligt fra renewal, reinstatement og spontaneous recovery.

FearPrime bruger ikke disse fire begreber som synonymer.

---

# 15. Behavioral approach / funktion

FearPrime inkluderer funktionelle adfærdsmål, fx:

```text
attempted: yes/no
completed: yes/no
latency_seconds: optional
duration_seconds: optional
safety_behaviour_count: optional
escape: yes/no
```

Adfærd skal defineres før opgaven.

### Hvorfor
En person kan stadig rapportere høj distress og samtidig udvise større handlefrihed. Det er et andet outcome end symptomlettelse.

---

# 16. Distress / affect

Selvrapporteret distress kan registreres fx 0–10 eller 0–100.

Men:

```text
distress ≠ threat expectancy
```

Eksempel:

```text
Threat expectancy = 20 %
Distress = 8/10
```

Dette kan betyde, at personen ved at noget sandsynligvis er sikkert, men stadig oplever stærk autonom/affektiv aktivering.

FearPrime ser netop denne dissociation som vigtig information.

---

# 17. Fysiologi

Mulige mål:
- skin conductance response (SCR),
- fear-potentiated startle (FPS),
- heart rate,
- HRV,
- respiration.

### Regel
Hver modalitet analyseres separat før multimodal syntese.

Der må ikke konkluderes “fear memory erased”, fordi én fysiologisk respons falder.

---

# 18. Standard FearPrime-session

Minimumsfelter:

```yaml
session_id: null
date: null
context: null
phase: acquisition/extinction/recall/generalization/other
prediction:
  threat_expectancy: null
  safety_expectancy: null
outcome:
  observed: null
  definition_pre_registered: true
learning:
  prediction_error_signed: null
  prediction_error_absolute: null
affect:
  distress_pre: null
  distress_post: null
behavior:
  attempted: null
  completed: null
  escape: null
  safety_behaviours: null
physiology:
  modality: null
  value: null
confounders:
  sleep: null
  caffeine: null
  illness: null
  treatment_changes: null
```

---

# 19. Pre-registration light

Før en FearPrime-opgave skal mindst følgende defineres:

1. præcis prediction,
2. præcist observerbart outcome,
3. hvilken metric der er primær,
4. hvilket tidspunkt der er primært,
5. hvad der tæller som missing/unclear,
6. hvilke confounders der registreres.

Dette reducerer post-hoc reinterpretation.

---

# 20. Analysehierarki

FearPrime foretrækker denne rækkefølge:

```text
1. rå data
2. trial-/session-tidslinje
3. CS+ og CS− separat
4. differensscores
5. slopes/AUC
6. samlet interpretation
```

Ikke omvendt.

---

# 21. Falsifikationskriterier

FearPrime-modellen svækkes, hvis:

1. expectancy-opdatering ikke forudsiger nogen senere ændring i relevant adfærd eller recall,
2. bedre within-session extinction systematisk ikke hænger sammen med senere recall,
3. generalization-training ikke forbedrer transfer til nye sikre stimuli/kontekster,
4. threat/safety discrimination ikke tilfører information ud over generel distress,
5. biologiske augmentation-kandidater kun ændrer akut state uden målbar retention/generalization.

Ingen enkelt negativ test forkaster hele frameworket; de enkelte mekanismehypoteser vurderes særskilt.

---

# 22. Status

Med dette dokument har FearPrime nu standardmål for:

- acquisition,
- threat expectancy,
- safety expectancy,
- prediction error,
- discrimination,
- extinction,
- extinction recall,
- generalization,
- renewal,
- reinstatement,
- spontaneous recovery,
- reacquisition,
- behavior/function,
- physiology.

Næste kritiske measurement-opgave er at implementere disse felter i en maskinlæsbar sessionsstruktur og senere i `/data/`-laget.
