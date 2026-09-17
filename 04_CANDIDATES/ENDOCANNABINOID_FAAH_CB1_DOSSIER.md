# FearPrime — endocannabinoid / FAAH / CB1-dossier

Version 0.21 · 2026-09-17

## Formål
Dette dossier samler FearPrimes evidensspor for **anandamid (AEA), FAAH og CB1** i fear/safety learning, extinction og PTSD-relevant stressregulering.

Optagelse i dossieret betyder forskningsrelevans — ikke dokumenteret PTSD-behandling.

Se også:
- [Kandidatmatrix](CANDIDATE_MATRIX.md)
- [Learning metrics](../06_MEASUREMENT/LEARNING_METRICS.md)
- [Generalization & Safety Learning Engine](../03_EXTINCTION/GENERALIZATION_AND_SAFETY_LEARNING_ENGINE.md)
- [Humant FAAH/CB1-studiekort](../07_STUDIES/VERIFIED/2012_2019_Endocannabinoid_CB1_FAAH_Human_Extinction.md)

---

## 1. Mekanistisk kerne
Endocannabinoidsystemet er et aktivitetsafhængigt modulatorsystem. I FearPrime er det centrale spørgsmål ikke "mere cannabinoid = mindre frygt", men om ændring i endocannabinoid tone påvirker bestemte faser af læring:

```text
acquisition
→ extinction learning
→ extinction consolidation
→ delayed extinction recall
→ stress reactivity
→ generalization / return of fear
```

CB1-receptorer findes i flere relevante kredsløb, bl.a. amygdala, hippocampus og præfrontale områder. Effekten er kredsløbs-, celle- og timingafhængig.

## 2. FAAH → anandamid
FAAH nedbryder anandamid (AEA). Farmakologisk FAAH-hæmning kan derfor øge endogen AEA uden at være det samme som direkte CB1-agonisme.

Dette skel er vigtigt:

```text
FAAH inhibition ≠ THC ≠ CBD ≠ direct CB1 agonism
```

De kan påvirke overlappende systemer, men deres farmakologi og evidens må ikke slås sammen.

## 3. Central human kausal evidens: Mayo et al.
Mayo et al. 2020 udførte et dobbeltblindet, placebokontrolleret experimental-medicine-studie hos raske voksne med FAAH-hæmmeren PF-04457845.

- aktiv gruppe: n=16
- placebo: n=29
- 4 mg dagligt i 10 dage
- anandamid steg omtrent ti gange
- 24-timers extinction recall blev forbedret
- autonom stressreaktivitet og stress-induceret negativ affekt blev reduceret

PMID `31590924` · DOI `10.1016/j.biopsych.2019.07.034`.

### FearPrime-fortolkning
Dette er direkte human kausal støtte til, at FAAH-hæmning kan påvirke **delayed extinction recall og stressreaktivitet**. Det er ikke et klinisk PTSD-forsøg og dokumenterer ikke symptomremission.

**Evidenstype:** B  
**Robusthed:** R2 — kontrolleret enkeltfund; uafhængig klinisk replikation mangler.

## 4. CB1-genetik
Heitland et al. 2012 fandt forskelle i fear extinction relateret til genetisk variation i CNR1 i et humant conditioning-paradigme.

PMID `23010766` · DOI `10.1038/tp.2012.90`.

Genetisk association støtter biologisk relevans, men kan ikke sidestilles med en interventionseffekt.

**Evidenstype:** B/D  
**Robusthed for farmakologisk effekt:** R1.

## 5. PTSD-translation
PTSD-litteraturen indeholder observationer af ændret endocannabinoid tone og CB1-relaterede markører, men biomarkørforskelle beviser ikke, at farmakologisk normalisering forbedrer extinction eller kliniske symptomer.

Et nyere review fra 2025 beskriver endocannabinoidsystemet som et relevant mål for fear acquisition/extinction og stressregulering, men fremhæver samtidig, at en stor del af interventionsgrundlaget fortsat er præklinisk eller tidligt humant.

PMID `40789309`.

## 6. CBD skal holdes separat
CBD påvirker flere targets og er ikke en selektiv FAAH- eller CB1-intervention. Rodentdata for aversiv memory updating er mere omfattende end humane data.

Review 2024: PMID `39029986`, DOI `10.1016/bs.irn.2024.03.007`.

FearPrime beholder derfor CBD i sit eksisterende separate spor.

## 7. Hvad dossieret IKKE viser
Der er ikke dokumenteret:

- at FAAH-hæmning er en etableret PTSD-behandling,
- at PF-04457845 forbedrer klinisk exposure-terapi,
- at højere AEA altid er fordelagtigt,
- at cannabinoid agonisme og FAAH-hæmning er funktionelt ækvivalente,
- at akut anxiolyse er lig med bedre extinction memory.

## 8. FearPrime-predictions
Hvis FAAH/AEA-sporet faktisk forbedrer extinction-memory snarere end blot akut state, forventes:

1. bedre **delayed recall** frem for kun lavere akut distress,
2. forbedring der kan måles separat på CS+/CS− eller relevant safety discrimination,
3. mindre return of fear i relevante paradigmer,
4. et resultat der ikke reduceres til sedation eller generel dæmpning,
5. mulig moderator-effekt af stress-state, genotype eller baseline AEA.

## 9. Målekrav
Registrér separat:

```yaml
acute_distress: null
threat_expectancy: null
safety_expectancy: null
extinction_slope: null
delayed_recall_24h: null
generalization: null
renewal: null
reinstatement: null
SCR: null
startle: null
HR_HRV: null
stress_negative_affect: null
```

## 10. Evidensstatus
| Påstand | Evidens | Status |
|---|---|---|
| CB1/endocannabinoider er relevante for fear extinction | human + præklinisk | ✅/🟡 |
| FAAH-hæmning øger AEA hos mennesker | RCT experimental medicine | ✅ |
| FAAH-hæmning kan forbedre delayed extinction recall | ét kontrolleret humant studie | 🟡 R2 |
| FAAH-hæmning forbedrer PTSD-behandling | mangler direkte klinisk evidens | 🔴 |
| CBD/THC kan bruges som proxy for FAAH-hæmning | farmakologisk ugyldigt | ❌ |

## 11. Debug
Den største risiko er at springe fra et elegant translationalt kædeforløb — FAAH → AEA → extinction recall — direkte til klinisk behandling. FearPrime kræver mindst uafhængig human replikation og klinisk PTSD-transfer før en sådan opgradering.
