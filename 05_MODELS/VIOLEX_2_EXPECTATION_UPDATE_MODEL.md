# FearPrime — ViolEx 2.0: expectation-update model

Version 0.28 · 2026-09-20

## Status

Dette er et **valgfrit fortolkningslag** i FearPrime. Det erstatter ikke den adaptive PTSD-model, inhibitory-learning-sporet, predictive processing eller reconsolidation-modellerne.

ViolEx 2.0 er et interdisciplinært teoriframework for, hvad der kan ske, når et faktisk udfald ikke matcher en forventning. Det er ikke en valideret PTSD-behandling og specificerer ikke i sig selv en bestemt neurokemisk mekanisme.

## Kerneidé

FearPrime kan bruge ViolEx til at stille et ekstra spørgsmål efter en læringshændelse:

> Der opstod et mismatch mellem forventning og udfald — men blev mismatch'et faktisk brugt til at opdatere den gamle model?

Den kompakte proces er:

```text
generaliseret forventning
→ situationsspecifik forventning
→ anticipatoriske reaktioner/adfærd
→ faktisk udfald
→ forventningsbekræftelse eller forventningsbrud
→ accommodation og/eller immunization
→ opdateret eller bevaret forventning

parallel adfærdsakse:
assimilation ↔ experimentation
approach ↔ avoidance
```

## Tre centrale responser

### 1. Accommodation — forventningen opdateres

Accommodation betyder, at udfaldet integreres i forventningen.

Det kan vise sig som:
- ændring af den forventede sandsynlighed for et udfald,
- lavere eller højere sikkerhed i forventningen,
- destabilisering eller stabilisering af en forventning.

FearPrime-fortolkning:

```text
"Jeg forventede X"
→ "Y skete"
→ "Y er relevant evidens"
→ næste forventning flyttes i retning af Y
```

### 2. Immunization — forventningen beskyttes mod mismatch

Immunization betyder, at disconfirming evidence får mindre betydning for den generaliserede forventning.

#### Data-oriented immunization

Selve evidensen devalueres.

Eksempler:
- "det tæller ikke",
- "målingen/oplevelsen var upålidelig",
- "det var bare held",
- "det var en undtagelse".

#### Concept-oriented immunization

Betydningen eller kategorien omdefineres, så udfaldet ikke længere tester den oprindelige generaliserede forventning.

Eksempel:

```text
"Andre mennesker er farlige"
→ en bestemt person opfører sig sikkert
→ "den person er bare en særundtagelse / det siger intet om mennesker generelt"
```

### 3. Assimilation — adfærd øger sandsynligheden for bekræftelse

I ViolEx 2.0 er assimilation primært en anticipatorisk adfærdsstrategi: adfærd ændrer situationen, så forventningsbekræftelse bliver mere sandsynlig eller forventningsbrud mindre sandsynligt.

I et fear-learning-spor kan det fx undersøges, om sikkerhedsadfærd, kontrol, scanning eller undgåelse gør det svært at få diagnostisk ny information.

Det betyder ikke, at al beskyttelsesadfærd er irrationel. Spørgsmålet er, om adfærden gør testen af den konkrete forventning informativ eller uinformativ.

## FearPrime × ViolEx under exposure

Den eksisterende [Extinction Engine](../03_EXTINCTION/EXTINCTION_ENGINE.md) kan få et ekstra ViolEx-lag.

### Før

Registrér:
1. situationsspecifik forventning,
2. forventet udfald,
3. sandsynlighed/sikkerhed i forventningen,
4. relevante anticipatoriske reaktioner,
5. mulig sikkerhedsadfærd/assimilation,
6. hvad der faktisk ville tælle som modbevis.

### Under

Registrér:
- faktisk udfald,
- om forventningen blev bekræftet eller brudt,
- størrelsen af mismatch'et,
- om adfærden gjorde udfaldet diagnostisk.

### Efter

Spørg:
1. Hvad skete der faktisk?
2. Hvor meget ændrede forventningen sig?
3. Hvor meget ændrede sikkerheden i forventningen sig?
4. Blev udfaldet accepteret som relevant evidens?
5. Hvis ikke: var forklaringen data-oriented immunization, concept-oriented immunization eller en rationel kvalitetskontrol af evidensen?
6. Hvad forventes næste gang?

## Hvorfor "prediction error" ikke automatisk betyder læring

FearPrime bør holde disse led adskilt:

```text
mismatch/prediction error
≠ automatisk accommodation
≠ automatisk extinction
≠ automatisk reconsolidation
```

Et stort forventningsbrud kan give stærk opdatering, men ViolEx 2.0 diskuterer også, at meget små brud kan ignoreres som støj, mens meget store brud kan kategoriseres som undtagelser.

Derfor foreslår forfatterne, at sammenhængen mellem violation-magnitude og sandsynligheden for accommodation **kan** være omvendt U-formet i nogle domæner. Det er en hypotese/boundary-condition-idé, ikke en universel lov.

## Kobling til den adaptive PTSD-model

ViolEx passer som et specifikt læringslag under den bredere [Adaptive PTSD Model](ADAPTIVE_PTSD_MODEL.md).

En mulig FearPrime-formulering er:

```text
tidligere trusselserfaring
→ stærk generaliseret trusselsforventning
→ situationsspecifik prediction
→ scanning / undgåelse / sikkerhedsadfærd
→ nyt udfald
→ expectation violation
→ accommodation ELLER immunization
→ mere fleksibel eller fortsat rigid forventningsmodel
```

Dette gør det muligt at undersøge en vedvarende trusselsmodel uden at antage, at systemet er "defekt". Modellen kan være historisk adaptiv, men samtidig være vanskelig at opdatere med ny kontekstspecifik evidens.

## Experimentation som kontrast til assimilation

ViolEx 2.0 skelner også mellem assimilation og **experimentation**.

Experimentation betyder her adfærd, der søger valid forventningsrelevant information uanset om den ender med at bekræfte eller afkræfte forventningen.

FearPrime kan bruge dette som designprincip:

> Målet med en læringsprøve er ikke at bevise "alt er sikkert", men at gøre den konkrete prediction testbar og få så diagnostisk information som muligt.

## Minimumsmål til et ViolEx-spor

Et simpelt datasæt pr. episode/session kan indeholde:

| Felt | Eksempel |
|---|---|
| Prediction | "X vil ske" |
| Prediction confidence | 0–100 |
| Expected cost | 0–100 |
| Anticipatory reaction | scanning / undgåelse / fysiologi |
| Assimilation/safety behavior | ja/nej + type |
| Actual outcome | hvad skete |
| Violation magnitude | 0–100 |
| Evidence credibility | 0–100 |
| Response | accommodation / immunization / blandet |
| Immunization subtype | data / concept / ingen |
| Updated prediction | næste forventning |
| Updated confidence | 0–100 |
| Later recall | næste dag / senere |
| Generalization | samme læring i ny kontekst? |

## Testbare FearPrime-hypoteser

ViolEx-laget gør bl.a. disse spørgsmål testbare:

1. Forudsiger større **accommodation** bedre senere ændring i forventning end akut angstfald gør?
2. Forudsiger **immunization** return of fear, selv når en exposure-session objektivt var sikker?
3. Reducerer mindre sikkerhedsadfærd/assimilation immunization ved at gøre udfaldet mere diagnostisk?
4. Generaliserer accommodation fra én situation til beslægtede situationer?
5. Er ekstreme expectation violations mindre lærerige i nogle personer/situationer, fordi de subtypes som undtagelser?

De er forskningsspørgsmål, ikke etablerede FearPrime-resultater.

## Vigtige begrænsninger

- ViolEx 2.0 er et teoriframework, ikke et PTSD-RCT.
- Frameworket beskriver funktionelle kognitive/adfærdsmæssige processer; det identificerer ikke alene deres neurale årsag.
- Immunization er ikke automatisk en bias eller fejl. Det kan være rationelt at afvise upålidelig evidens.
- "Prediction error" bruges på tværs af felter med forskellige formelle betydninger; FearPrime skal definere det konkret i hvert eksperiment.
- Den omvendte U-form mellem violation og accommodation er en foreslået mulighed, som kræver yderligere empirisk afprøvning.
- Ændret expectation er ikke i sig selv bevis på memory reconsolidation.

## Kilde

Se [Panitz et al. 2021 — ViolEx 2.0](../07_STUDIES/THEORY/2021_Panitz_ViolEx_2_0.md).

Originalartikel:
- Panitz C, Endres D, Buchholz M, et al. *A Revised Framework for the Investigation of Expectation Update Versus Maintenance in the Context of Expectation Violations: The ViolEx 2.0 Model.*
- Frontiers in Psychology. 2021;12:726432.
- DOI: 10.3389/fpsyg.2021.726432
- PMID: 34858264
- PMCID: PMC8632008

## FearPrime-regel

**Et forventningsbrud er først interessant som læring, når vi også undersøger, hvad systemet gjorde med informationen bagefter.**
