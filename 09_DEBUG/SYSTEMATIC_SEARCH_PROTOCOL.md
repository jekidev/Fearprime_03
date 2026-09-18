# FearPrime — reproducerbar litteratursøgning

Version 0.22 · 2026-09-18

## Formål
Denne protokol standardiserer FearPrimes litteratursøgninger. Den gør en søgning **reproducerbar og auditerbar**, men gør ikke automatisk et spor til et formelt systematisk review.

## Minimumskrav før en søgning
Registrér før screening:
- research question,
- population,
- exposure/intervention,
- comparator,
- outcomes,
- study designs,
- dato- og sproggrænser,
- databaser,
- primære og sekundære søgestrenge,
- inklusions-/eksklusionsregler.

## Databaser
Kerne:
1. PubMed/MEDLINE.
2. Crossref/DOI-kontrol eller forlagsside til metadata.
3. ClinicalTrials.gov eller relevant trial-register for kliniske interventionsspor.

Supplerende:
- Google Scholar/citation chasing,
- review-referencekæder,
- nyere citing articles,
- preregistration/protocol repositories, når relevant.

En supplerende søgekilde må ikke erstatte den dokumenterede kernesøgning.

## Search-ID
Format:
FP-<DOMAIN>-YYYYMMDD-NN

Eksempel:
FP-RECON-20260918-01

Search-ID gemmes i [data/search_log.csv](../data/search_log.csv).

## Query-princip
Gem den **eksakte** query, ikke en efterfølgende omskrivning.

Eksempelstruktur:
```text
(PTSD OR "posttraumatic stress disorder")
AND
(reconsolidation OR reactivation OR "memory updating")
AND
(propranolol OR retrieval OR extinction)
```

For fear-learning-spor registreres søgninger separat for:
- acquisition,
- extinction,
- extinction recall,
- generalization,
- safety learning,
- renewal,
- reinstatement,
- spontaneous recovery,
- reacquisition.

## Screening
### Trin 1 — metadata
Fjern åbenlyse:
- dubletter,
- ikke-relevante populationer,
- ikke-empiriske publikationer, hvis spørgsmålet er effekt,
- protokoller fra effektanalysen.

### Trin 2 — abstract
Registrér eksklusionsgrund:
- wrong population,
- wrong intervention/exposure,
- wrong outcome,
- wrong design,
- duplicate cohort/publication,
- insufficient empirical data.

### Trin 3 — full text
Kontrollér:
- sample source,
- randomisering/blinding,
- intervention/timing,
- outcome definition,
- analysed N,
- attrition,
- preregistration,
- effect estimate/CI,
- adverse events,
- participant overlap.

## Citation chasing
Backward og forward citation chasing logges som særskilte search-rækker, fordi de ikke er reproducerbare som én databasestreng.

## Trial-register
For kliniske interventionsstudier kobles publication ↔ trial registration, når registration kan verificeres.

Registrér:
- registration ID,
- prespecified primary outcome,
- planned N,
- ændringer fra protocol til publication.

## Dublet- og overlapkontrol
Før en publikation tælles som et nyt uafhængigt studie:
1. sammenlign forfattere,
2. rekrutteringssted,
3. tidsperiode,
4. sample size,
5. registration,
6. intervention/procedure,
7. baselinekarakteristika.

Muligt overlap registreres i:
- [participant-overlap-register](PARTICIPANT_OVERLAP_REGISTER.md)
- [data/participant_overlap.csv](../data/participant_overlap.csv)

## Opdateringssøgninger
Ved hver update:
- brug sidste dokumenterede search date,
- søg fra den dato til dags dato,
- behold samme kernesøgning,
- dokumentér eventuelle ændringer i query som en ny search-ID.

## Negative og null fund
Negative studier må ikke ekskluderes, fordi interventionen ikke virkede.
Registrér separat:
- null effect,
- harm/worsening,
- failed replication,
- inconclusive/underpowered.

## Evidensklassifikation
Efter inklusion:
- A–E = evidenstype,
- R0–R4 = robusthed/replikation,
- M0–M4 = reconsolidation-mekanismeinferens, når relevant,
- RoB = LOW/SOME/HIGH/UNCLEAR.

## Reproducerbarhedskrav
Et domæne kan først betegnes som “reproducerbart søgt”, når repoet indeholder:
- exact query,
- database,
- search date,
- result count,
- inclusion count,
- exclusions med grunde,
- citation chasing log,
- overlapkontrol,
- opdateringsdato.

## Debug
“Vi søgte bredt” er ikke reproducerbart. En query uden dato er ikke reproducerbar. En PubMed-liste uden eksklusionslog er ikke et systematisk review.
