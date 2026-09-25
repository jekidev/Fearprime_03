# FearPrime data layer

Index version 0.30 · 2026-09-20

Denne mappe er FearPrimes maskinlæsbare evidens- og målelag.

**Schema-versioner er uafhængige af repo-releaseversionen.** Markdown-filerne er fortsat den menneskeligt læsbare hoveddokumentation; datafilerne skal kunne analyseres af scripts/agenter uden at opfinde manglende information.

## Filer
- `studies.csv` — seed-indeks over centrale verificerede studier; komplet spejling af alle studiekort er ikke målet for denne fil endnu.
- `study_schema.yaml` — felter og tilladte statuskoder for study-level evidens.
- `effects.csv` — effect-level seed-data; numeriske effekter og konfidensintervaller står tomme, når de ikke er udtrukket.
- `risk_of_bias.csv` — study-level RoB seed-kodning.
- `participant_overlap.csv` — register over kendt/muligt deltager-overlap.
- `duplicate_reference_registry.csv` — triagerede gentagne DOI/PMID-henvisninger mellem studiekort; adskiller gentagen omtale fra uafhængige evidenskilder.
- `session_schema.yaml` — maskinlæsbar struktur til FearPrime learning/session-data.
- `violex_exposure_schema.yaml` — schema til prediction → violation → accommodation/immunization → retention/generalization.
- `violex_exposure_template.csv` — tom trial/session-template til ViolEx exposure-måling.
- `computational_demo.csv` — **syntetisk** demo-data til calculator/model-comparison og CI; må ikke behandles som empiriske data.
- `nightmare_schema.yaml` — nightly nightmare/sleep/dream/next-day schema.
- `nightmare_log_template.csv` — tom nightly nightmare-log template.
- `interoceptive_factorial_schema.yaml` — maskinlæsbar factorial research-design.
- `interoceptive_trial_template.csv` — tom trial-level template.
- `search_log.csv` — standardiseret log for reproducerbare litteratursøgninger.
- `pubmed_reconsolidation_records_2026-09-18.csv` — PubMed export-set.
- `reconsolidation_screening_2026-09-18.csv` — screeninglog.
- `certainty.csv` — claim-level FearPrime certainty-ratings.

## Regler
1. Tomme felter betyder **ikke verificeret / ikke udtrukket**, ikke nul.
2. Én publikation, ét studie og én deltagerkohorte er forskellige enheder.
3. `R0–R4` = robusthed/replikation; `M0–M4` = mekanistisk reconsolidation-inferens.
4. Effektstørrelse og 95% CI gemmes kun, når de er rapporteret eller kan beregnes uden tvivlsomme antagelser.
5. Kliniske outcomes, laboratorielæring, fysiologi og mekanisme holdes adskilt.
6. Personlige N=1/N=3-data må ikke lægges i det offentlige repo.
7. Subjective confidence må ikke automatisk fortolkes som computational precision.
8. Prediction-error felter i ViolEx-schemaet er projektdeskriptive, ikke neurale PE-mål.
9. Stateful modeller som HGF-like approximation forudsætter korrekt trial-rækkefølge; bland ikke flere deltagere i én sekvens uden eksplicit participant-level håndtering.

## Computational tools
- [Tool index](../tools/README.md)
- [Computational Model Comparison](../05_MODELS/COMPUTATIONAL_MODEL_COMPARISON.md)
- [ViolEx Exposure Measurement Sheet](../06_MEASUREMENT/VIOLEX_EXPOSURE_MEASUREMENT_SHEET.md)

## Source-of-truth-rækkefølge
1. Primærpublikation / registrering.
2. Study card i `07_STUDIES/`.
3. Struktureret row i `data/`.
4. Dossier/syntese.

Datafiler må ikke skabe nye claims, som ikke findes i den menneskeligt læsbare evidens.
