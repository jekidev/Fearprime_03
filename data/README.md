# FearPrime data layer

Version 0.22 · 2026-09-18

Denne mappe er FearPrimes maskinlæsbare evidens- og målelag. Markdown-filerne er fortsat den menneskeligt læsbare hoveddokumentation; datafilerne skal kunne analyseres af scripts/agenter uden at opfinde manglende information.

## Filer
- `studies.csv` — seed-indeks over centrale verificerede studier.
- `study_schema.yaml` — felter og tilladte statuskoder for study-level evidens.
- `participant_overlap.csv` — register over kendt/muligt deltager-overlap.
- `session_schema.yaml` — maskinlæsbar struktur til FearPrime learning/session-data.
- `search_log.csv` — standardiseret log for reproducerbare litteratursøgninger.

## Regler
1. Tomme felter betyder **ikke verificeret / ikke udtrukket**, ikke nul.
2. Én publikation, ét studie og én deltagerkohorte er forskellige enheder.
3. `R0–R4` = robusthed/replikation; `M0–M4` = mekanistisk reconsolidation-inferens.
4. Effektstørrelse og 95% CI gemmes kun, når de er rapporteret eller kan beregnes uden tvivlsomme antagelser.
5. Kliniske outcomes, laboratorielæring, fysiologi og mekanisme holdes adskilt.
6. Personlige N=1/N=3-data må ikke lægges i det offentlige repo.

Se også:
- [Risk-of-bias template](../09_DEBUG/RISK_OF_BIAS_TEMPLATE.md)
- [Effect-size extraction standard](../09_DEBUG/EFFECT_SIZE_EXTRACTION_STANDARD.md)
- [Participant-overlap register](../09_DEBUG/PARTICIPANT_OVERLAP_REGISTER.md)
- [Systematic search protocol](../09_DEBUG/SYSTEMATIC_SEARCH_PROTOCOL.md)
