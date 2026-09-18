# FearPrime — PTSD-mareridt, THC/cannabinoider, butyrat og drømmearbejde

Version 0.26 · 2026-09-18  
**Status: eksplorativ forskningshypotese — ikke behandlingsprotokol.**

## Forskningsspørgsmål
Kan en præ-søvn manipulation af cannabinoid-systemet og/eller butyrat ændre:
1. PTSD-relateret nightmare frequency/distress,
2. dream recall og emotional salience,
3. næste dags threat expectancy,
4. mulighed for efterfølgende imagery rescripting / drømmelog?

## Hvorfor hypotesen overhovedet er interessant

### Cannabinoidsporet
Små/heterogene studier og reviews har rapporteret signaler for cannabinoider ved PTSD-relaterede søvnproblemer og mareridt, men evidensen er svag. Nabilone har et lille placebo-kontrolleret nightmare-signal, mens nyere reviews ikke finder robust superiority for almindelig cannabis/THC som PTSD-behandling.

FearPrime må derfor holde disse adskilt:

```text
nabilone-data
≠
THC-data
≠
cannabis-data
≠
FAAH/AEA-data
```

THC kan desuden påvirke søvnarkitektur og dream recall, og cannabis-withdrawal kan give REM rebound og mere forstyrret drømning.

### Butyratsporet
Ribbens 2026 viser, at akut natriumbutyrat kan påvirke senere human extinction-memory retrieval efter stærk nok extinction learning.

Der findes derimod **ingen direkte evidens i FearPrime-korpuset for, at butyrat ved sengetid reducerer PTSD-mareridt eller specifikt forbedrer REM-relateret emotional memory processing.**

## Hovedhypotese
Hvis nightmares delvist fungerer som gentagen reactivation af threat-memory under søvn, kunne ændret cannabinoid tone påvirke akut nightmare expression, mens butyrat teoretisk kunne påvirke plasticitet/consolidation.

Men retningen er ukendt:

```text
mere plasticitet
kan styrke safety/update
ELLER
styrke maladaptiv/salient learning
```

Derfor er “THC + butyrat før søvn = bedre reconsolidation” **ikke** en understøttet konklusion.

## Dream interpretation / drømmearbejde
“Drømmetydning” registreres som **kvalitativ hypotesegenerering**, ikke som valideret PTSD-mekanisme.

Mere evidensnært kan næste-morgens arbejde opdeles i:
- dream log,
- nightmare distress,
- tema/cue-kodning,
- trigger/context mapping,
- imagery rescripting / imagery rehearsal som separat intervention.

Image Rehearsal Therapy har langt stærkere klinisk støtte ved PTSD-relaterede mareridt end fri symbolsk drømmetydning.

## Falsificerbare predictions
Hvis hypotesen har værdi, bør man kunne observere adskillelige ændringer i:
- nightmare frequency,
- nightmare distress,
- awakenings,
- dream recall,
- subjective sleep quality,
- næste-dags arousal,
- trauma-cue intrusions,
- senere imagery-rescripting response.

## Alternative forklaringer
- sedation,
- anxiolysis uden memory change,
- mindre dream recall uden færre nightmares,
- expectancy/placebo,
- REM suppression/rebound,
- sleep fragmentation,
- tolerance/withdrawal,
- ændret emotionel salience.

## Kritisk evidensstatus
- **Cannabis/THC som samlet PTSD-behandling:** lav/konfliktfyldt evidens; nuværende VA/DoD-guideline anbefaler imod cannabis/cannabisderivater til PTSD.
- **Nabilone for nightmares:** lille signal; ikke direkte overførbart til THC.
- **THC + butyrat-kombination:** ingen direkte evidens identificeret.
- **Butyrat → nightmares:** ingen direkte evidens identificeret.
- **Drømmetydning → symptomreduktion:** ikke etableret; imagery rehearsal/rescripting er mere evidensbaseret.

## Sikkerheds-/designregel
Dette dokument specificerer **ingen dosis eller hjemmeprotokol**. Søvn-/nightmare-forskning skal adskille akut symptomdæmpning fra ændring i memory learning og tage højde for cannabinoidbivirkninger, tolerance og withdrawal.


## Measurement integration v0.26
Den operationelle måling ligger nu i [Nightmare Measurement Engine](../06_MEASUREMENT/NIGHTMARE_MEASUREMENT_ENGINE.md).

Maskinlæsbare skabeloner:
- [nightmare_schema.yaml](../data/nightmare_schema.yaml)
- [nightmare_log_template.csv](../data/nightmare_log_template.csv)

Hypotesen må kun vurderes med adskilte outcomes for nightmare burden, dream recall, sleep continuity, next-day state og senere learning/function.
