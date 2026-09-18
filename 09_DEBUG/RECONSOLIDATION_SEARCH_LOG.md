# Rekonsolidering og tilbagevendende frygt — kildekontrol
2026-09-18 · Version 0.24 · Målrettet reproducerbar update-søgning, ikke fuld PRISMA-systematisk litteraturoversigt.

> **Rolling historical search log.** Brug denne til kumulativ provenance. En konkret søgekørsel skal dokumenteres i en dateret search-fil, fx [RECONSOLIDATION_SEARCH_2026-09-18.md](RECONSOLIDATION_SEARCH_2026-09-18.md).

## v0.23 update-pass
Den detaljerede query-/screeninglog findes i [RECONSOLIDATION_SEARCH_2026-09-18.md](RECONSOLIDATION_SEARCH_2026-09-18.md) og maskinlæsbart i [data/search_log.csv](../data/search_log.csv).

Nye selvstændige kort:
- [Bos et al. 2019 — acute but not permanent propranolol effects](../07_STUDIES/VERIFIED/2019_Bos_Acute_Not_Permanent_Propranolol.md), PMID `30846933`, DOI `10.3389/fnhum.2019.00051`.
- [Gerlicher et al. 2022 — PE reconsolidation null](../07_STUDIES/VERIFIED/2022_Gerlicher_PE_Reconsolidation_Null.md), PMID `35393469`, DOI `10.1038/s41598-022-09720-w`.
- [Chen et al. 2025 — kvantificeret prediction error](../07_STUDIES/VERIFIED/2025_Chen_Quantified_Prediction_Error_Reconsolidation.md), PMID `40570716`, DOI `10.1016/j.cognition.2025.106224`.
- [Paul & Asthana 2025 — memory strength × prediction error](../07_STUDIES/VERIFIED/2025_Paul_Memory_Strength_PE_Retrieval_Extinction.md), PMID `40653191`, DOI `10.1016/j.neuroscience.2025.07.014`.
- [Li et al. 2025 — propranolol/PTSD meta-analyse](../07_STUDIES/REVIEWS/2025_Li_Propranolol_PTSD_Meta.md), PMID `39944616`, DOI `10.3389/fphar.2025.1545493`.
- [Xia et al. 2026 — farmakologi og human aversiv hukommelse](../07_STUDIES/REVIEWS/2026_Xia_Pharmacological_Human_Aversive_Memory.md), PMID `41513054`, DOI `10.1016/j.neubiorev.2026.106548`.

**Search-begrænsning:** den anvendte web/PubMed-indekserede søgeflade eksponerede ikke et stabilt komplet hit-count for de booleske queries. FearPrime registrerer derfor ikke et opdigtet PRISMA-n. Exact query, dato, kilder og inkluderede records er bevaret; en direkte PubMed-export er stadig nødvendig for en fuld systematisk search-flow.

## Søgninger
- Schiller 2010 preventing return fear humans reconsolidation update extinction
- Chalkia 2020 preregistered replication reactivation extinction fear
- Sevenster Beckers Kindt 2012 retrieval not sufficient reconsolidation
- Sevenster Beckers Kindt 2013 prediction error
- Sevenster Beckers Kindt 2014 retrieval reconsolidation new learning prediction error
- Stemerding 2022 boundary conditions unsuccessful replication
- Kindt Soeter Vervliet 2009 propranolol human fear reconsolidation
- Wood 2015 PTSD three negative reconsolidation studies
- Brunet 2018 propranolol PTSD reactivation randomized trial
- Roullet 2021 propranolol traumatic memory reactivation PTSD randomized trial
- propranolol reconsolidation meta-analysis conflicting 2022
- Nader Schafe LeDoux 2000 fear memories protein synthesis
- context renewal reinstatement human fear

## Primærkilder kontrolleret
- Nader 2000: PMID `10963596`, præklinisk foundational reconsolidation-spor.
- Kindt, Soeter & Vervliet 2009: PMID `19219038`, DOI `10.1038/nn.2271`. Positivt humant propranolol proof-of-concept.
- Schiller 2010: PMID `20010606`, DOI `10.1038/nature08637`. Positiv retrieval-extinction-rapport.
- Sevenster, Beckers & Kindt 2012: PMID `22406658`, DOI `10.1016/j.nlm.2012.01.009`. Retrieval alene ikke tilstrækkelig i paradigmet.
- Sevenster, Beckers & Kindt 2013: PMID `23413355`, DOI `10.1126/science.1231357`. Prediction error som nødvendig betingelse i det konkrete paradigme.
- Sevenster, Beckers & Kindt 2014: PMID `25320349`, DOI `10.1101/lm.035493.114`. Forslag om overgang retrieval → reconsolidation → new learning afhængigt af PE.
- Wood et al. 2015: PMID `25441015`, DOI `10.1016/j.psychres.2014.09.005`. Tre små negative kliniske PTSD-studier.
- Brunet et al. 2018: PMID `29325446`, DOI `10.1176/appi.ajp.2017.17050481`. Positivt klinisk RCT-signal under pre-reactivation propranolol.
- Chalkia et al. 2020: PMID `32580869`, DOI `10.1016/j.cortex.2020.04.017`. Registreret direkte replikation uden forventet retrieval-extinction-fordel.
- Roullet et al. 2021: PMID `33612830`, DOI `10.1038/s41386-021-00984-w`. Klinisk RCT uden samlet propranololfordel på hovedfortolkningen.
- Stemerding et al. 2022: PMID `35145138`, DOI `10.1038/s41598-022-06119-5`. Mislykket replikation af det præcise single-PE boundary-mønster.

## Nye studiekort i v0.20
- `07_STUDIES/VERIFIED/2009_Kindt_Propranolol_Human_Fear_Reconsolidation.md`
- `07_STUDIES/VERIFIED/2012_Sevenster_Retrieval_Not_Sufficient.md`
- `07_STUDIES/VERIFIED/2014_Sevenster_PE_Retrieval_Reconsolidation_New_Learning.md`
- `07_STUDIES/VERIFIED/2022_Stemerding_Boundary_Replication_Failure.md`

Eksisterende kort for Schiller, Sevenster 2013, Wood, Brunet, Chalkia og Roullet bevares og indgår nu i den samlede robusthedsmatrix.

## R0–R4 robusthed
`07_STUDIES/STUDY_LEDGER.md` indeholder nu en claim-specific R0–R4-score. Det er et projektinternt robustheds-/replikationsindeks, ikke en behandlingseffekt-score.

Vigtig regel:
- et positivt proof-of-concept kan være R2,
- en stærk negativ direkte replikation kan være R3,
- R4 kræver bred uafhængig konvergens i relevant population/paradigme/outcome.

Reconsolidation boundary-modulet bruger separat **M0–M4** for graden af mekanistisk inferens, så robusthed og mekanisme ikke blandes sammen.

## Aktuel syntese
1. Reconsolidation har et stærkt præklinisk fundament.
2. Human fear-memory updating efter retrieval er dokumenteret i flere paradigmer, men modality og boundary conditions betyder meget.
3. Retrieval alene er ikke en valideret destabiliseringsmarkør.
4. Prediction error er plausibelt vigtig, men “én PE” er ikke robust reproduceret som universal regel.
5. Retrieval-extinction har positive fund, men den registrerede direkte replikation af Schiller-proceduren var negativ.
6. Kliniske propranolol/PTSD-studier er blandede; symptomforbedring identificerer ikke automatisk reconsolidation som mekanisme.
7. Boundary conditions må ikke bruges post hoc til at immunisere teorien mod nulresultater.

## Begrænsninger
Denne runde er målrettet mod kernefund, boundary conditions og replikation. Den er ikke en PRISMA-systematisk review og beregner ikke pooled effektstørrelser. N, kønsfordeling, alle eksklusionskriterier, preregistration og risk-of-bias er endnu ikke fuldt udtrukket for alle studier.

Kredlow-meta-analysen (PMID `26689086`) er et ældre videre læsespor; dens søgning til juni 2014 kan ikke alene beskrive nyere replikationsstatus. De modstridende propranolol-metaanalyser fra 2022 er registreret særskilt i `07_STUDIES/REVIEWS/2022_Propranolol_Reconsolidation_Conflicting_MetaAnalyses.md`.

## Næste kildekontrol
1. Effektstørrelser og CI for Schiller/Chalkia/Sevenster/Stemerding.
2. Risk-of-bias/preregistration-status for de kliniske propranolol-forsøg.
3. Deltager-overlap og analyseversioner i propranolol-litteraturen.
4. Hold fear-potentiated startle, SCR, expectancy, symptoms og funktion som separate outcomes.
5. Udvid med uafhængige laboratorier, ikke kun samme forskningslinje.


## v0.24 screening/export + certainty
- [PubMed/MEDLINE export-status](PUBMED_RECONSOLIDATION_EXPORT_2026-09-18.md)
- [Verified 30-record export set](../data/pubmed_reconsolidation_records_2026-09-18.csv)
- [Screening/dedup log](../data/reconsolidation_screening_2026-09-18.csv)
- [Reconsolidation certainty profile](RECONSOLIDATION_CERTAINTY_PROFILE.md)

Native PubMed total hit count remains unverified because the ESearch/bulk-export endpoint was inaccessible in the current retrieval environment. This limitation is explicit and prevents PRISMA-complete labeling.
