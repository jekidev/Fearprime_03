# FearPrime — Nightmare Measurement Engine

Version 0.26 · 2026-09-18

## Formål
Denne engine standardiserer måling af PTSD-relaterede mareridt, drømme, søvn og næste-dags lærings-/funktionsoutcomes uden at blande dem sammen.

Den er et **måleframework**, ikke en behandlingsprotokol.

Se også:
- [PTSD nightmare/sleep dossier](../03_EXTINCTION/PTSD_NIGHTMARE_SLEEP_DOSSIER.md)
- [Nightmare THC/butyrat-hypotese](../05_MODELS/PTSD_NIGHTMARE_THC_BUTYRATE_HYPOTHESIS.md)
- [Learning metrics](LEARNING_METRICS.md)
- [Measurement plan](MEASUREMENT_PLAN.md)

## Outcome-lag
FearPrime holder mindst syv lag adskilt:
1. nightmare occurrence
2. nightmare distress
3. dream recall
4. sleep continuity
5. content/theme
6. next-day state
7. later learning/function

Et lavere dream-recall score er ikke automatisk et bedre nightmare-outcome.

## Minimum nightly record
Minimumsfelter:

night_id, date, lights_out_time, final_wake_time, subjective_sleep_quality_0_10, awakenings_count, nightmare_occurred, nightmare_count, nightmare_distress_peak_0_10, nightmare_distress_on_waking_0_10, trauma_related, awakening_due_to_nightmare, dream_recall_present, recall_vividness_0_10, estimated_recall_fraction_0_100, trauma_similarity_0_10, morning_arousal_0_10, intrusion_load_0_10, avoidance_urge_0_10.

## Nightmare frequency
Rapportér både antal nightmare-nætter, antal totale nightmares og antal observerede nætter.

Missing night er ikke det samme som no nightmare.

## Dream recall
Dream recall holdes separat fra nightmare burden.

Regel: mindre recall ≠ færre nightmares ≠ bedre PTSD.

## Content coding
Drømmeindhold må ikke omsættes direkte til skjulte psykologiske sandheder.
FearPrime bruger content coding som deskriptiv hypotesegenerering.

Mulige tags: person, sted, trusselstype, flugt, fastfrysning, konfrontation, tab, skyld, skam, social afvisning, kontroltab, redning, sikkerhed, aggressor, kropslig sensation, ukendt/andet.

## Dream interpretation vs imagery rescripting
Drømmetydning kan gemmes som subjektiv fortolkning, hypotese eller temaassociation. Den må ikke bruges som et primært efficacy-outcome.

Imagery rescripting / IRT registreres særskilt med target night, ny ending, rehearsal, believability og distress før/efter.

## Next-day learning metrics
Hvis et mareridt bruges som trigger til næste-dags læring registreres threat expectancy, safety expectancy, trauma intrusion, cue avoidance, rescripting og konkret action goal.

## Predefined summaries
Vis rå nightly data først.
Derefter kan man beregne nightmare_frequency, mean_nightmare_distress, median_nightmare_distress, mean_dream_recall_vividness, mean_awakenings og mean_next_day_arousal.

## THC/cannabinoid + butyrat research fields
I et formelt studie registreres cannabinoid_condition, butyrate_condition, blinded, randomized og administration_time_relative_to_sleep.
Ingen dosis er defineret i denne engine.

## Confounders
Minimum: samlet sleep opportunity, tidligere natters søvn, sygdom, alkohol, cannabinoid withdrawal/tolerance, ændring i medicin, ændring i psykoterapi, akut stressor, sent koffein og miljø/soverum.

## Missing data
Tilladte koder: complete, missing_not_recorded, no_recall, no_nightmare, unclear.

## Falsifikationskriterier
Nightmare/plasticity-hypotesen svækkes hvis:
1. dream recall falder, men nightmare distress/frequency ikke ændres,
2. akut sedation forbedrer subjektiv søvn uden senere functional/learning benefit,
3. butyrat-condition ikke ændrer delayed nightmare/rescripting outcomes,
4. cannabinoid-condition kun ændrer recall,
5. rescripting ikke ændrer recurrence/distress over gentagne nætter,
6. effekter forsvinder ved kontrol for withdrawal/sleep opportunity.

## Machine-readable files
- [nightmare_schema.yaml](../data/nightmare_schema.yaml)
- [nightmare_log_template.csv](../data/nightmare_log_template.csv)

Udfyldte personlige data må ikke lægges i det offentlige repo.