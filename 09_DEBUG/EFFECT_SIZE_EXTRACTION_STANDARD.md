# FearPrime — effect-size & CI extraction standard

Version 0.22 · 2026-09-18

## Formål
Denne standard bestemmer, hvordan FearPrime registrerer effektstørrelser uden at blande **within-group change**, **between-group treatment effect**, laboratorie-respons og kliniske symptommål.

## Prioritetsrækkefølge
For RCT/interventionsstudier foretrækkes:
1. prespecificeret between-group estimate for primary outcome,
2. adjusted model estimate med 95% CI,
3. raw mean difference med SD/SE og N,
4. standardiseret mellemgruppeeffekt,
5. response/remission RR eller OR.

Within-group Cohen d må registreres, men må aldrig stå som treatment-effect estimate.

## Standardfelter
```yaml
effect_id: null
study_id: null
outcome: null
outcome_family: null
timepoint: null
comparison: null
metric: null
estimate: null
ci95_low: null
ci95_high: null
standard_error: null
p_value: null
n_intervention: null
n_control: null
direction: null
adjusted: null
covariates: []
source_location: null
calculated_by_fearprime: false
assumptions: []
```

## Kontinuerte outcomes
Mulige metrics:
- MD = raw mean difference,
- SMD / Cohen d,
- Hedges g,
- model beta,
- ratio of means, når fagligt passende.

### Hedges g
Hvis FearPrime selv beregner standardiseret mellemgruppeeffekt:
1. pooled SD beregnes fra verificerede gruppe-SD'er,
2. Cohen d beregnes,
3. small-sample correction anvendes til Hedges g,
4. 95% CI beregnes med dokumenteret formel,
5. alle input gemmes.

Ingen SD må imputeres ved gæt.

## Binære outcomes
Brug efter rapportering/design:
- RR,
- OR,
- risk difference.

Registrér events og denominators, hvis de findes.

## Repeated measures / longitudinal data
En mixed-model interaction er ikke direkte ækvivalent med et simpelt post-treatment Cohen d.

Registrér:
- modeltype,
- interaction term,
- timepoints,
- covariance/correlation hvis nødvendig for senere beregning.

Hvis nødvendige parametre mangler, bruges statusværdien: not_derivable_from_verified_data.

## Fear-conditioning outcomes
Hold modaliteter separat:
- expectancy,
- SCR,
- startle,
- heart rate,
- behavior,
- fMRI/ROI/network.

En effekt på startle må ikke kopieres til “fear memory” generelt.

## Return-of-fear
Angiv eksplicit outcome:
- renewal,
- reinstatement,
- spontaneous recovery,
- reacquisition.

Et composite outcome må kun bruges, hvis originalstudiet definerer det.

## Meta-analyser
Registrér:
- model: fixed/random,
- effect metric,
- pooled estimate + CI,
- I²/tau² når rapporteret,
- antal studier/deltagere,
- population,
- intervention definition,
- publication-bias analyser,
- inclusion window/search date.

En pooled meta-effekt må ikke gives R4 alene på grund af signifikans.

## Multiple outcomes
Primary outcome prioriteres.
Sekundære outcomes bevares, men må ikke cherry-pickes til hovedkonklusion.

## Subgrupper
Markér:
- prespecified vs post hoc,
- interaction test,
- multiplicity.

Et signifikant resultat i én subgruppe er ikke dokumentation for forskel mellem subgrupper uden en relevant interaction test.

## Direction
Brug eksplicit:
- favors_intervention,
- favors_control,
- null,
- mixed,
- not_applicable.

Undgå at gøre fortegn (+/-) til semantisk retning uden at definere skalaen.

## CI-regel
Hvis CI ikke er rapporteret og ikke kan beregnes direkte:
- skriv not_extracted eller not_derivable,
- udfyld ikke med et estimat fra en anden publikation.

## Repo-output
Effect-level data gemmes i:
[data/effects.csv](../data/effects.csv)

RoB gemmes på study-level og kan senere kobles via study_id.

## Debug
De største fejl FearPrime skal undgå:
1. within-group d → treatment effect,
2. p-værdi → effektstørrelse,
3. symptomændring → reconsolidation mechanism,
4. én fysiologisk kanal → global fear memory,
5. ikke-signifikant → ækvivalent,
6. meta-analyse → automatisk høj certainty.
