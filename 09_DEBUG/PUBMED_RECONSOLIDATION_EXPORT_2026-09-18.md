# FearPrime — PubMed/MEDLINE reconsolidation export status

Version 0.24 · 2026-09-18

## Status
**PARTIAL — verified record export + deduplication/screening completed; native PubMed ESearch bulk export/hit count not available through the current retrieval interface.**

FearPrime må ikke mærke dette som en komplet PRISMA/PubMed-systematisk søgning.

## Gennemført
- Daterede search-concepts og query-spor er bevaret.
- PubMed-indekserede records, der faktisk blev identificeret og verificeret, er eksporteret til `data/pubmed_reconsolidation_records_2026-09-18.csv`.
- Screening, inklusion/eksklusion og sample-overlap er eksporteret til `data/reconsolidation_screening_2026-09-18.csv`.
- PMID er primær bibliografisk deduplikationsnøgle.
- Publikationsdublet holdes adskilt fra participant/sample overlap.
- Chalkia 2020 verification/reanalysis er koblet til Schiller 2010-datasættet og tælles ikke som ny participant sample.
- Wood 2015 er markeret som én publikation med tre randomiserede delstudier.

## Verificeret export-set
30 PubMed-indekserede records blev eksplicit screenet i dette pass. **30 er størrelsen på det verificerede eksport-set — ikke PubMeds totale hit count for de underliggende Boolean queries.**

## Hvorfor total PubMed hit count ikke rapporteres
Den aktuelle retrievalflade kan læse individuelle PubMed-poster og PubMed-indekserede søgeresultater, men PubMeds native ESearch/export-endpoint var ikke tilgængeligt. Derfor er total result count ukendt, og der indføres ikke et opdigtet PRISMA identification-N.

## Inklusionslogik
Core: mennesker; fear/aversive memory eller PTSD; retrieval/reactivation/reconsolidation eller retrieval-extinction; empirisk intervention/boundary-condition studie eller direkte relevant systematic review.

Context/indirect: human episodic-memory reconsolidation, extinction-only beta-blockade og kliniske analogue-populationer.

Excluded from core: preclinical-only studier, tidlig PTSD prevention uden reconsolidation/reactivation-spørgsmål samt narrative reviews som primær effect evidence.

## Deduplikation
Bibliographic duplicate: samme PMID/DOI fra flere queries → én record.

Participant duplicate: forskellige publikationer fra samme rådata/kohorte → linkes og tælles ikke som uafhængige samples.

## Mangler før ægte PubMed/MEDLINE systematic export
1. Kør den gemte Boolean query i native PubMed/MEDLINE.
2. Registrér exact total hit count på søgedatoen.
3. Eksportér alle PMID/NBIB/RIS records.
4. Deduplicér på tværs af queries.
5. Title/abstract-screening med reviewer-status.
6. Full-text exclusion log med grunde.
7. PRISMA flow counts.
8. Dateret update-search.

## Aktuelt signal
- Raut 2022 fandt ingen klar samlet PTSD-symptomfordel af propranolol-reconsolidation og rapporterede betydelig usikkerhed/heterogenitet.
- Li 2025 rapporterede et positivt bredere propranolol/PTSD meta-signal, så review-litteraturen er fortsat konfliktfyldt.
- Xia 2026 rapporterede relativt solid evidens for propranolol og reconsolidation i healthy-human aversive-memory paradigmer; dette er mere direkte for laboratorie-reconsolidation end for klinisk PTSD.
- Chen 2025 støtter en gradueret PE-model, mens Stemerding 2022 og Gerlicher 2022 bevarer vigtige replication/null-fund.

## Terminologiregel
Indtil native PubMed-export er gennemført bruges formuleringen: **"reproducible targeted PubMed-indexed evidence pass with a verified export set"**, ikke **"complete systematic PubMed review"**.