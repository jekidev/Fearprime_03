# FearPrime — HPA-akse, stresshormoner og hukommelse

Version 0.20 · 2026-09-17

## Formål
Dette modul beskriver HPA-aksen og glucocorticoider som **timing-afhængige modulatorer af læring, retrieval, extinction og konsolidering**. FearPrime afviser en enkel model hvor PTSD forklares som “for meget” eller “for lidt” cortisol.

Se også:
- [Fear Circuit Master Map](FEAR_CIRCUIT_MASTER_MAP.md)
- [Reconsolidation Boundary Conditions](../03_EXTINCTION/RECONSOLIDATION_BOUNDARY_CONDITIONS.md)
- [Learning Metrics](../06_MEASUREMENT/LEARNING_METRICS.md)

---

## 1. HPA-kæden

```text
stress/threat appraisal
      ↓
hypothalamus (CRH)
      ↓
pituitary (ACTH)
      ↓
adrenal cortex
      ↓
cortisol
      ↓
MR/GR + genomiske og hurtige signalveje
      ↓
hukommelse, arousal, metabolisme, immunfunktion
```

Denne kæde interagerer med noradrenalin, endocannabinoider, hippocampus, amygdala, PFC og søvn/døgnrytme.

## 2. PTSD er ikke et enkelt cortisolniveau
Dunlop & Wong (2019) gennemgår HPA-fund ved PTSD og fremhæver inkonsistens på tværs af basalniveauer, challenge paradigmer, køn, tidlig belastning, genetik/epigenetik og interventionsdesign.

- PMID `30342071`

En nyere review af HPA-dysregulering og fysisk sygdom ved PTSD understreger igen, at HPA- og SAM-systemerne bør vurderes dynamisk og i relation til komorbiditet og systemiske outcomes.

- PMID `39280087`
- DOI `10.1016/j.bbih.2024.100849`

## 3. Timing er den centrale variabel
Stresshormoner kan have forskellige effekter afhængigt af læringsfase.

### Acquisition / initial encoding
Glucocorticoider kan under visse forhold styrke konsolideringen af emotionelt materiale.

### Retrieval
Akut forhøjede glucocorticoider kan reducere retrieval af allerede lagrede emotionelle minder.

### Extinction
Den samme retrieval-dæmpning kan potentielt mindske konkurrencen fra fear memory under exposure, mens glucocorticoider samtidig kan påvirke konsolideringen af den nye extinction memory.

### Reconsolidation
Effekter omkring post-retrieval-vinduet må ikke antages at være de samme som effekter under extinction. Reconsolidation kræver først plausibel destabilisering.

Merz & Wolf (2022) gennemgår netop denne faseafhængighed i humane fear/anxiety-memory paradigmer.

- PMID `36228925`
- DOI `10.1016/j.neubiorev.2022.104901`

## 4. Extinction og glucocorticoider
En translational review fra 2019 beskriver en model hvor glucocorticoider kan støtte extinction-baserede interventioner gennem kombinationen af mindre retrieval af den gamle aversive hukommelse og stærkere konsolidering af ny extinction learning.

- PMID `30610352`

FearPrime behandler dette som en plausibel fase-model, ikke som dokumentation for at “cortisol er godt for exposure” i enhver dosis, person eller timing.

Repoets humane hydrocortison-studier ligger i:
`07_STUDIES/VERIFIED/2015_2021_Hydrocortisone_PE_PTSD.md`.

## 5. MR, GR og feedback
Cortisol virker bl.a. gennem mineralocorticoid- og glucocorticoidreceptorer. Receptorbalance, feedback-sensitivitet, circadian fase og tidligere stresshistorik kan ændre effekten. Derfor er plasma-/spytcortisol alene ikke et fuldt mål for HPA-funktion.

## 6. Døgnrytme
Cortisol har en stærk døgnprofil. En værdi uden tidspunkt, søvnstatus, opvågningstid og samplingkontekst er derfor svær at fortolke.

FearPrime bør registrere:
- klokkeslæt,
- tid siden opvågning,
- søvnvarighed/-kvalitet,
- koffein/nikotin hvis relevant for forsøget,
- akut stressor,
- medicin/hormoner der påvirker HPA-aksen.

## 7. FearPrime phase matrix

| Fase | Mulig glucocorticoid-effekt | Hvad skal måles |
|---|---|---|
| Acquisition | encoding/konsolidering af ny fare | CS+/CS−, expectancy, senere recall |
| Retrieval | ændret adgang til gammel hukommelse | baseline fear expression |
| Extinction | gammel retrieval + ny safety learning | extinction slope + CS− |
| Post-extinction | konsolidering | næste-dags recall |
| Reactivation | kun relevant hvis memory destabiliseres | prediction error + controls |
| Reconsolidation | mulig restabilisering | senere return-of-fear, ikke akut state |

## 8. Falsificerbare predictions
HPA-modellen svækkes hvis:
- timing ikke modererer glucocorticoid-effekter,
- ændringer i cortisol kun følger subjektiv distress uden relation til læring eller recall,
- exogen glucocorticoid-effekt ikke kan adskilles fra sedation/arousal/placebo,
- HPA-mål ikke bidrager ud over søvn, circadian fase og generel belastning.

## 9. Debug
- PTSD har ikke ét universelt “cortisol-signatur”.
- Lavt basal-cortisol er ikke synonymt med lav HPA-aktivitet eller lav stress.
- En akut cortisolændring beviser ikke GR-medieret memory modification.
- Exogen hydrocortison og endogenous stress-respons er ikke identiske interventioner.
- Symptomlettelse under en session er ikke evidens for forbedret extinction consolidation.

## FearPrime-konklusion
HPA-aksen skal modelleres som en **fase-, kontekst- og receptorafhængig memory modulator**. Det vigtigste spørgsmål er ikke “er cortisol højt eller lavt?”, men **hvornår signalet opstår, hvilken hukommelsesproces der er aktiv, og hvilket senere outcome der ændres**.