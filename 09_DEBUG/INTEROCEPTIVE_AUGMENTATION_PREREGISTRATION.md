# FearPrime — preregistration: interoceptiv augmentation design

Version 0.26 · 2026-09-18
**Status: forskningsdesign / preregistration-template — ikke selvforsøgs- eller doseringsprotokol.**

## Research question
Kan en biologisk plasticitetsmodulator før en standardiseret, superviseret interoceptiv challenge og en post-learning dopaminerg eller oxytocinrelateret manipulation ændre akut bodily-threat updating, 24-timers recall, 7-dages recall, generalization, return of fear og funktion uden at effekten blot skyldes akut sedation, arousal eller expectancy?

## Designprincip
Den oprindelige sekvenshypotese — butyrat → interoceptiv challenge → L-DOPA → oxytocin — må ikke testes som én samlet uigennemsigtig stack først.

Primært design er komponentdekomposition.

### Stage A — pre-challenge plasticity factor
B0 = control/placebo condition
B1 = butyrate condition

### Stage B — post-learning consolidation factor
D0 = control/placebo condition
D1 = dopaminergic/L-DOPA condition

Konceptuelt 2×2 factorial design:

| | D0 | D1 |
|---|---|---|
| B0 | control | dopaminergic only |
| B1 | butyrate only | butyrate + dopaminergic |

Oxytocin behandles ikke som tredje faktor i første test, fordi humane data er retningsmæssigt inkonsistente og kan øge eller reducere extinction afhængigt af timing/kontekst.

## Interoceptiv challenge
Challenge skal være standardiseret, superviseret, have prædefinerede stopkriterier og fremkalde et målbart interoceptivt threat/safety prediction problem.

FearPrime specificerer ikke respirationsrate, varighed eller hyperventilationsinstruktioner her.

## Primary outcome
Primært outcome bør være delayed learning, ikke akut symptomlettelse.

Eksempler: 24h threat-expectancy recall eller 24h interoceptive safety-discrimination score.
Den præcise metric vælges før datalås.

## Secondary outcomes
- peak distress during challenge
- end-session threat expectancy
- end-session safety expectancy
- signed/absolute prediction error
- recovery slope
- 24h distress
- 7d recall
- generalization to related bodily cues
- reinstatement/return-of-fear measure
- approach/function
- dissociation
- adverse effects

Fysiologi holdes separat: respiration, heart rate, HRV og andre prædefinerede mål.

## Hypotheses
### H0-B
Butyrate-condition ændrer ikke primary delayed-learning outcome relativt til control.

### H1-B
Butyrate-condition ændrer primary delayed-learning outcome relativt til control.

### H0-D
Post-learning dopaminergic condition ændrer ikke delayed recall relativt til control.

### H1-D
Post-learning dopaminergic condition ændrer delayed recall.

### H0-B×D
Der er ingen interaction mellem pre-challenge butyrate-condition og post-learning dopaminergic condition.

### H1-B×D
Der er en interaction mellem de to faktorer.

### H0-OXT
En separat oxytocin-timing condition ændrer ikke delayed recall/safety learning.

### H1-OXT
Oxytocin ændrer delayed recall/safety learning. Retningen er tosidet i udgangspunktet pga. modstridende humane fund.

## Key interaction question
Det centrale spørgsmål er: B main effect? D main effect? B×D interaction? acute state only? delayed learning? generalization?

## Randomization and blinding
For et faktisk kontrolleret studie:
- randomisering genereres før inklusion afsluttes,
- allocation holdes skjult hvor muligt,
- assessor bør være blindet,
- condition guess registreres efter sessionen,
- blinding break registreres,
- analyse følger intention-to-treat hvor passende.

Hvis kendte akutte effekter gør blinding vanskelig, registreres expectancy/unblinding som egen bias-kilde.

## Timing registration
Registrér tidspunkt for pre-challenge condition, challenge start/slut, post-learning condition, 24h recall og 7d recall.
Ingen dosis eller administrationsvej fastlægges i denne prereg-template.

## Analysis plan
Konceptuel primary model:
primary_outcome ~ B + D + B:D + baseline_primary + prespecified_covariates

Ved repeated measures kan bruges:
outcome ~ B * D * time + baseline + random_intercept(participant)

Modeltype fastlægges før datalås.

## Multiplicity
Primary outcome og primary timepoint defineres før analyse.
Secondary outcomes mærkes secondary/exploratory og må ikke bruges til at omskrive et negativt primary result.

## Oxytocin Stage C
Oxytocin testes separat, fordi timing kan ændre retningen, social salience/threat processing kan påvirkes, og et større humant 2025-forsøg fandt dårligere extinction learning.

Stage C sammenligner control timing med predefined oxytocin timing og måler acute threat/salience, delayed recall og social/context generalization.

## Falsification criteria
Sekvenshypotesen nedgraderes hvis:
1. butyrate kun ændrer akut state, ikke delayed recall,
2. dopaminergic condition ikke ændrer delayed outcome,
3. B×D interaction er kompatibel med nul og CI udelukker en relevant interaction,
4. challenge giver høj arousal uden bedre safety learning,
5. bedre within-session respons ikke overføres til 24h/7d,
6. oxytocin forringer extinction/safety learning,
7. interventionseffekter forklares bedre af unblinding/expectancy,
8. adverse effects eller dissociation reducerer valid learning exposure,
9. generalization/funktion ikke ændres trods bedre laboratory metric.

## Safety/stopping rules
Et faktisk studie kræver formel klinisk/sikkerhedsmæssig godkendelse.

Sessionen stoppes efter prædefinerede kriterier ved fx synkope/presynkope, vedvarende brystsmerter, alvorlige neurologiske symptomer, uventet alvorlig autonom reaktion, markant dissociation der kompromitterer samtykke/opgaveevne, deltagers ønske om at stoppe eller investigator judgement om medicinsk risiko.

Ingen deltager må presses til at fortsætte for at gennemføre exposure.
Adverse events registreres separat fra fear/distress.

## Exclusion/safety assessment
Et faktisk protokolstudie kræver medicinsk vurdering af relevante kardiovaskulære og neurologiske risici, lægemiddelkontraindikationer/interaktioner, graviditet/reproduktiv sikkerhed hvor relevant, aktuelle behandlinger, substansbrug/withdrawal og forhold der gør interoceptiv challenge uforsvarlig.

Denne preregistration-template definerer ikke konkrete lægemiddeldoser.

## Own-empiricism rule
Brugerens egen erfaring med kontrolleret hyperventilation registreres som hypothesis-generating observation, ikke efficacy evidence, dose-finding evidence, safety evidence eller proof of mechanism.

## Data lock
Før outcome-inspektion låses primary outcome, primary timepoint, exclusions, covariates, missing-data plan, analysis model, multiplicity handling og adverse-event definitions.
Ændringer bagefter mærkes exploratory/post hoc.

## Machine-readable design
Se [data/interoceptive_factorial_schema.yaml](../data/interoceptive_factorial_schema.yaml).