# Måleplan
Version 0.3 · 2026-09-17

## Formål
Adskil symptomer, læring og hverdagsfunktion. Denne plan er et observationsdesign; den identificerer ikke alene årsag eller neurotransmitterniveauer.

Se de to specialiserede målelag:
- [CPTSD measurement / ITQ](CPTSD_MEASUREMENT.md)
- [Standardiserede FearPrime learning metrics](LEARNING_METRICS.md)

| Felt | Definition | Hvornår |
|---|---|---|
| Konkret mål | Én observerbar handling, fx stille et spørgsmål | Før forløbet |
| Forventning | Sandsynlighed 0–100 for et præcist defineret udfald | Før hver opgave |
| Safety expectancy | Forventning om et præcist sikkert/ikke-aversivt udfald | Før relevante opgaver |
| Udfald | Skete det: ja, nej eller uklart? Beskriv observationen | Efter opgaven |
| Prediction error | Forskel mellem prædefineret forventning og observeret udfald | Efter opgaven |
| Handling | Udført, delvist udført eller ikke udført | Efter opgaven |
| Ubehag | Selvrapporteret 0–10, holdt adskilt fra forventning | Før og efter |
| Senere funktion | Kunne en sammenlignelig opgave udføres? | Ca. næste dag og syv dage senere |
| Kontekst | Sted, tidspunkt og relevante forhold | Ved hver opgave |
| Mulige forstyrrende faktorer | Søvn, sygdom, koffein og ændringer i behandling | Samme dag |

## Fire adskilte outcome-lag
FearPrime holder så vidt muligt følgende adskilt:

1. **kliniske symptomer** — fx PCL-5 eller ITQ,
2. **learning metrics** — expectancy, discrimination, extinction, recall, generalization og return of fear,
3. **funktion/adfærd** — hvad personen faktisk kan gøre,
4. **fysiologi** — fx SCR, startle, puls/HRV eller respiration, når det er relevant og måles ordentligt.

Ændring i ét lag må ikke automatisk beskrives som ændring i de øvrige.

## Enkel udgangspunkt
Brug eksempelvis syv dage med kort registrering af hverdagsfunktion og belastning. Syv dage er et praktisk valg, ikke en valideret nødvendighed. Vent ikke på en “perfekt udgangspunkt”, og udsæt ikke nødvendig behandling for at holde data rene. Ændringer markeres i tidslinjen.

## Symptommål
PCL-5 er et 20-spørgsmål selvrapporteringsmål for DSM-5 PTSD-symptomer. Det er ikke i sig selv en diagnose eller et specifikt CPTSD-mål. Brug en officiel version med uændret ordlyd og dokumenteret referenceperiode. En score må ikke omdøbes til procent helbredelse. Kilde og versioner: [VA PCL-5](https://www.ptsd.va.gov/professional/assessment/adult-sr/ptsd-checklist.asp).

For ICD-11 PTSD/CPTSD bruges [CPTSD_MEASUREMENT.md](CPTSD_MEASUREMENT.md), hvor PTSD, DSO og funktion registreres separat via ITQ-sporet. FearPrime kopierer ikke instrumentets spørgsmålstekst ind i repoet.

Projektets daglige 0–10-felter er egne observationsfelter og må ikke fremstilles som validerede PTSD-skalaer.

## Learning outcomes
[LEARNING_METRICS.md](LEARNING_METRICS.md) standardiserer blandt andet:

```text
acquisition
threat expectancy
safety expectancy
prediction error
threat/safety discrimination
extinction
extinction recall
generalization
renewal
reinstatement
spontaneous recovery
reacquisition
```

Rå CS+/CS−- eller tilsvarende cue-værdier bevares ved siden af differensscores. Within-session symptomlettelse er ikke automatisk retention eller reconsolidation.

## Ugentlig gennemgang
1. Hvilke meningsfulde handlinger blev faktisk lettere?
2. Var ændringen stabil eller kun akut?
3. Skete der samtidige ændringer, som kan forklare resultatet?
4. Hvilke data mangler? Manglende registrering er ikke nul symptomer.
5. Hvad taler imod vores foretrukne forklaring?
6. Ændrede kliniske symptomer, læringsmål og funktion sig i samme eller forskellige retninger?

Vis rå observationer og tidslinje før samlede gennemsnit. Undlad kausale påstande fra en ukontrolleret før/efter-sammenligning. Gentagne eksponeringer har læringsoverførsel; en simpel ABAB-model kan derfor ikke antage fuld tilbagevenden til udgangspunkt.

## Reconsolidation-orienterede målinger
Hvis et studie eller projekt hævder post-reactivation memory updating, bruges [RECONSOLIDATION_BOUNDARY_CONDITIONS.md](../03_EXTINCTION/RECONSOLIDATION_BOUNDARY_CONDITIONS.md).

Minimum registreres:
- target memory/type,
- reactivation cue,
- prediction-error-evidens,
- reminder-varighed,
- interventionstiming,
- delayed outcome,
- alternative forklaringer såsom extinction/new learning,
- return-of-fear-tests, hvis designet tillader det.

Retrieval alene må ikke mærkes som dokumenteret reconsolidation.

## Stabil behandling ved gentest
Tidligere tekst om test “uden læringstillæg” må ikke forstås som at springe ordineret medicin over. Registrér faktisk behandling. At skelne stofeffekt fra læring kræver et særskilt egnet forskningsdesign.

## Opbevaring
Dette repo er offentligt. Skabelonerne er tomme; udfyldte personlige helbredslogs skal opbevares privat.

## Kombination som forskningsspørgsmål
[FP-BL-01-testplanen](FP_BL_01_TEST_PLAN.md) adskiller tillægseffekt, synergi og mekanisme. Den indeholder forudvalgte mål og håndtering af læringsoverførsel; personlige observationer kan ikke erstatte dens kontrolgrupper.

## Status v0.19
FearPrime har nu et separat klinisk CPTSD-lag og et standardiseret læringslag. De næste måleopgaver er fysiologisk preprocessing/QC, maskinlæsbar session-schema og konsekvent effektstørrelse/CI i studieregistret.
