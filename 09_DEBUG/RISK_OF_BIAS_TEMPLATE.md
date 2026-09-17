# FearPrime — Risk of Bias (RoB) template

Version 0.21 · 2026-09-17

## Formål
Dette dokument standardiserer FearPrimes vurdering af **systematiske fejlkilder**. Det er ikke en erstatning for Cochrane RoB 2, ROBINS-I eller andre validerede værktøjer; det er et repo-lag, der gør de vigtigste bias-kilder synlige og maskinlæsbare.

## Statuskoder
- `LOW` — lav bekymring ud fra tilgængelig dokumentation
- `SOME` — nogen bekymring / utilstrækkelig information
- `HIGH` — høj risiko for bias
- `NA` — ikke relevant
- `UNCLEAR` — ikke vurderbart fra den kontrollerede kilde

## Kernefelter
```yaml
study_id: null
population: null
design: null
preregistration: null
sample_randomized: null
sample_analyzed: null
primary_outcome_prespecified: null

risk_of_bias:
  randomization_process: UNCLEAR
  allocation_concealment: UNCLEAR
  participant_blinding: UNCLEAR
  personnel_blinding: UNCLEAR
  outcome_assessor_blinding: UNCLEAR
  deviations_from_intended_intervention: UNCLEAR
  missing_outcome_data: UNCLEAR
  outcome_measurement: UNCLEAR
  selective_reporting: UNCLEAR
  analysis_flexibility: UNCLEAR
  multiplicity: UNCLEAR
  baseline_imbalance: UNCLEAR
  treatment_fidelity: UNCLEAR
  expectancy_unblinding: UNCLEAR
  participant_overlap: UNCLEAR
  overall: UNCLEAR

notes: []
```

## Reconsolidation-specifikke felter
Ved retrieval/reconsolidation-studier tilføjes:

```yaml
reconsolidation_specific:
  target_memory_reactivated: UNCLEAR
  prediction_error_documented: UNCLEAR
  no_reactivation_control: UNCLEAR
  timing_prespecified: UNCLEAR
  delayed_test: UNCLEAR
  return_of_fear_tested: UNCLEAR
  modality_separation: UNCLEAR
  alternative_extinction_explanation_addressed: UNCLEAR
  mechanism_claim_matches_design: UNCLEAR
```

## Farmakologi-specifikke felter
```yaml
pharmacology_specific:
  dose_and_formulation_reported: UNCLEAR
  administration_timing_reported: UNCLEAR
  adherence_verified: UNCLEAR
  target_engagement_measured: UNCLEAR
  side_effect_unblinding_risk: UNCLEAR
  concomitant_medication_controlled: UNCLEAR
```

## Effektstørrelser
For hvert centralt outcome registreres, hvis rapporteret eller beregneligt uden tvivlsomme antagelser:

```yaml
effect:
  outcome: null
  timepoint: null
  metric: null  # Hedges g, Cohen d, SMD, RR, OR, beta, raw MD osv.
  estimate: null
  ci_95: null
  p_value: null
  direction: null
  source: null
  calculated_by_fearprime: false
```

FearPrime beregner ikke en effektstørrelse ud fra utilstrækkelige summary data og udfylder ikke manglende SD'er ved gæt.

## Centrale regler
1. En `p < .05` er ikke en effektstørrelse.
2. Stor within-group ændring er ikke det samme som stor treatment effect.
3. Post hoc subgruppeeffekter markeres som eksplorative.
4. Flere outcomes må ikke cherry-pickes til én samlet konklusion.
5. Manglende signifikans er ikke dokumentation for ækvivalens.
6. Et studie kan have høj R-robusthed for et **negativt fund**.
7. Mekanisme-score M0–M4 og robusthed R0–R4 rapporteres separat.

## Samlet vurdering
Hvert centralt studie bør til sidst have:

```text
Evidenstype: A–E
Robusthed: R0–R4
Mekanistisk inferens (hvis relevant): M0–M4
Risk of bias: LOW / SOME / HIGH / UNCLEAR
Effektstørrelse: rapporteret med CI eller eksplicit “ikke udtrukket”
```

## Debug
RoB-vurderingen skal kunne revideres, når fuldtekst, supplement eller preregistration bliver tilgængelig. `UNCLEAR` er bedre end falsk præcision.
