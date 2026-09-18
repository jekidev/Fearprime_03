# FearPrime — certainty framework

Version 0.24 · 2026-09-18

## Formål
Dette lag vurderer **tillid til en konkret evidenspåstand/outcome på tværs af studier**.

Det er inspireret af GRADE, men er **ikke en formel GRADE-vurdering**, fordi FearPrime endnu ikke har fuld systematisk søgning, dobbelt-screening og komplet outcome-level data for alle domæner.

## Skala
- **HIGH** — yderligere evidens er usandsynlig at ændre hovedkonklusionen væsentligt.
- **MODERATE** — yderligere evidens kan ændre estimat eller fortolkning mærkbart.
- **LOW** — yderligere evidens vil sandsynligvis ændre sikkerheden/estimatet væsentligt.
- **VERY_LOW** — evidensen giver kun meget usikker støtte til påstanden.

## Fem kernedomæner
For hvert claim/outcome vurderes:
1. **Risk of bias**
2. **Inconsistency**
3. **Indirectness**
4. **Imprecision**
5. **Publication bias**

## FearPrime-separate annotationer
- **R0–R4** = replikations-/robusthedsstatus.
- **M0–M4** = mekanistisk reconsolidation-inferens.
- **population transfer** = fx healthy-human lab → PTSD.
- **outcome transfer** = fx startle → clinical symptoms.
- **participant overlap**.
- **preregistration/registered replication**.

## Ingen automatisk pointsum
Certainty må ikke beregnes som R + M + RoB = certainty. Hvert domæne dokumenteres kvalitativt, og den samlede rating begrundes eksplicit.

## Direktehed
- Healthy-human fear conditioning er relativt direkte for en claim om conditioned fear expression.
- Det er indirekte for en claim om PTSD-symptombehandling.
- PTSD symptomændring er indirekte for en claim om memory reconsolidation som mekanisme, medmindre mekanismen isoleres.

## Imprecision
CI'er og informationsmængde prioriteres over p-værdi. Når CI spænder fra meningsfuld fordel til nul/skade, nedgraderes certainty for en positiv effektpåstand.

## Inconsistency
Direkte negative replikationer vægtes stærkt. Boundary conditions må ikke bruges til post hoc at eliminere inconsistency. En moderator kan først reducere inconsistency-problemet, når den forudsiger resultater på tværs af uafhængige studier.

## Publication bias
Ved små, fleksible proof-of-concept-felter sættes publication bias som mindst UNCLEAR, indtil registreringer, upublicerede resultater og funnel/small-study analyser er vurderet.

## Certainty ≠ recommendation
En certainty-rating fortæller, hvor sikkert evidensgrundlaget støtter et claim. Den siger ikke automatisk, at interventionen bør anvendes, at benefit > harm, eller at en bestemt person bør tage et præparat.

## V1.0-krav
Et claim kan først få HIGH i FearPrime, når search-korpus er reproducerbart og tilstrækkeligt komplet, relevante studier har RoB, direkte studies er konsistente eller heterogenitet forklaret prospektivt, effektstørrelser/CI er tilstrækkeligt præcise, publication bias er vurderet, og population/outcome matcher claimet.

## Kilder
Metoden er GRADE-informeret efter Cochrane/GRADE Working Group, men FearPrime-ratings mærkes separat for ikke at foregive en formel GRADE reviewproces.