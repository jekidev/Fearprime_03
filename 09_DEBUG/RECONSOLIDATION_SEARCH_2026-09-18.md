# FearPrime — reconsolidation update search 2026-09-18

Version 0.23 · 2026-09-18

## Formål
Første v0.22-protokolbaserede update-pass for:
1. klinisk PTSD + propranolol/reactivation,
2. human retrieval-extinction/prediction error,
3. nyere boundary-condition-studier,
4. nyere systematiske reviews.

Dette er en **reproducerbar målrettet update-søgning**, men ikke endnu en fuld PRISMA-systematisk reviewkørsel.

## Kørte queries
### FP-RECON-20260918-01
Database/source: PubMed-indexeret web search  
Query:
```text
"memory reconsolidation" fear extinction humans PTSD propranolol retrieval 2023 2024 2025 2026
```

### FP-RECON-20260918-02
```text
PTSD propranolol traumatic memory reactivation randomized trial reconsolidation 2021 2022 2023 2024 2025
```

### FP-RECON-20260918-03
```text
retrieval extinction fear reconsolidation replication prediction error humans 2020 2021 2022 2023 2024 2025
```

### FP-RECON-20260918-04
```text
PTSD propranolol traumatic memory reactivation reconsolidation
```
Trial-registry spor blev kontrolleret via registrerings-ID'er i primærartiklerne (bl.a. NCT01127568 og NCT01713556).

## Nye/opgraderede kilder fra passet
1. Chen et al. 2025 — PMID 40570716; DOI 10.1016/j.cognition.2025.106224.
2. Paul & Asthana 2025 — PMID 40653191; DOI 10.1016/j.neuroscience.2025.07.014.
3. Li et al. 2025 propranolol/PTSD meta — PMID 39944616; DOI 10.3389/fphar.2025.1545493.
4. Xia, Quednow & Bach 2026 — PMID 41513054; DOI 10.1016/j.neubiorev.2026.106548.
5. 2026 systematic review of spontaneous recovery in human fear conditioning — DOI 10.3389/fnbeh.2026.1820847; bruges som nyere review-spor for replication status.

## Centrale allerede kendte kilder genkontrolleret
- Brunet 2018 — PMID 29325446.
- Wood 2015 — PMID 25441015.
- Chalkia registered replication 2020 — PMID 32580869.
- Chalkia verification report 2020 — PMID 32563517.
- Roullet 2021 — PMID 33612830.
- Raut 2022 meta — PMID 35405409.
- Stemerding 2022 — eksisterende boundary replication-failure card.

## Screening-/værktøjsbegrænsning
Den anvendte websøgeflade returnerede relevante PubMed-indekserede poster, men eksponerede ikke et stabilt komplet PubMed-result count for de booleske queries. Derfor registreres **ikke et opdigtet PRISMA-n**.

Søgningen er reproducerbar på query/date/source-niveau, men må først kaldes en fuld systematisk søgning, når:
- den samme query køres direkte i PubMed/MEDLINE,
- total hit count eksporteres,
- alle records deduplikeres,
- title/abstract-screening logges,
- full-text exclusions registreres.

## Foreløbig syntese
- Nyere 2025-studier understøtter fortsat PE og memory strength som mulige boundary conditions, men gør dem mere graduerede/paradigmeafhængige.
- De ophæver ikke Chalkia/Stemerding-type replication failures.
- 2026-reviewet finder relativt stærk human laboratoriekonvergens for propranolol/reconsolidation.
- Klinisk PTSD-evidens for propranolol er stadig review-afhængig og konfliktfyldt (2022 vs. 2025 meta-analyser).

## Debug
FearPrime må ikke efterrationalisere negative fund ved at tilføje en ny boundary condition, medmindre den nye moderator efterfølgende kan forudsige data i uafhængige studier.
