# FearPrime — participant overlap register

Version 0.23 · 2026-09-25

## Formål
Dette register forhindrer, at samme deltagere tælles flere gange, når én kohorte giver flere publikationer, reanalyser, sekundære outcomes eller follow-ups.

Maskinlæsbar version:
[data/participant_overlap.csv](../data/participant_overlap.csv)

## Statuskoder
- **distinct_sample** — verificeret særskilt sample.
- **same_original_data** — samme rådata/kohorte som anden publikation.
- **multiple_substudies** — én publikation indeholder flere selvstændige eksperimenter.
- **possible_overlap** — rimelig mistanke, ikke afklaret.
- **unknown_overlap** — overlap ikke undersøgt endnu.

## Kendte/registrerede eksempler

### Schiller 2010 ↔ Chalkia verification report 2020
Chalkia-gruppens verification/reanalysis af originaldata er **ikke et nyt deltagerforsøg**. Den analyserer originaldata og skal derfor ikke tælles som uafhængig sample.

Den registrerede direkte Chalkia replication fra 2020 er derimod en **ny sample**.

### Schnurr PE/CPT cohort, 2022 ↔ symptom-level reanalysis, 2024
The 2024 session-level symptom analysis reuses participants from the 2022 RCT registered as NCT01928732 (PMID 35044471). It is a secondary analysis of the same cohort, not an independent trial. The shared group ID `SCHNURR_PE_CPT_NCT01928732` is recorded in `data/participant_overlap.csv`.

### Wood 2015
Publikationen indeholder tre små randomiserede PTSD-eksperimenter. Ét paper må derfor heller ikke automatisk behandles som ét homogent studie i kvantitativ syntese.

### Brunet 2018 og Roullet 2021
De behandles som forskellige kliniske RCT'er i repoet, men participant-/site-overlap skal stadig kontrolleres via:
- trial registration,
- rekrutteringssteder,
- rekrutteringsperioder,
- forfattergrupper,
- baselinekarakteristika.

Indtil kontrollen er færdig står overlapstatus som **unknown_overlap**, ikke som verificeret nul overlap.

## Regler
1. Publikationsantal ≠ study count.
2. Study count ≠ independent cohort count.
3. Reanalysis tælles ikke som ny sample.
4. Protocol tælles ikke som effektstudie.
5. Follow-up kan være samme kohorte med nyt timepoint.
6. Secondary analysis kan give ny hypotese, men ikke nyt N.
7. Meta-analyser kontrolleres for overlappende primærstudier før sammenligning.

## Før meta-analyse
Hver inkluderet publikation får:
- study_id,
- cohort/overlap_group,
- registration,
- sample source,
- recruitment window,
- primary publication,
- secondary publications.

## Debug
Hvis overlap er uklart, må FearPrime hellere underklassificere certainty end antage uafhængighed.

## Gentagne kildehenvisninger ved strukturkontrol 2026-09-22

Dette er kontrol af dokumenternes identitet og rolle, ikke en ny kontrol af deltagernes rekrutteringshistorik. Automatikkens fire DOI-advarsler bevares synligt.

| Dokumentpar | Forklaring og tælleregel |
|---|---|
| [GLP-1-model](../07_STUDIES/PRECLINICAL/2026_GLP1_Liraglutide_PTSD_Model.md) og [kritisk vurdering](../07_STUDIES/PRECLINICAL/2026_GLP1_Liraglutide_PTSD_Audit.md) | Samme primærpublikation omtalt fra to vinkler; ikke to forsøg |
| [Ribbens 2026](../07_STUDIES/VERIFIED/2026_Ribbens_NaBu.md) og [epigenetisk samlekort](../07_STUDIES/MECHANISTIC/2012_2026_Epigenetics_FKBP5_COMT_HDAC_Extinction.md) | En primærartikel genbruges i en tværgående oversigt; ikke en replikation |
| [Zhao-protokol](../07_STUDIES/PROTOCOLS/2024_Zhao_TRE_Adolescent_RCT_Protocol.md) og [TRE-litteraturkort](../07_STUDIES/TRE_LITERATURE_MAP.md) | Protokollen henvises fra litteraturkortet; ingen ekstra effektdata |
| [Berceli-alias](../07_STUDIES/VERIFIED/2014_Berceli_TRE_Caregivers.md) og [pilotkort](../07_STUDIES/VERIFIED/2014_Berceli_TRE_Caregivers_Pilot.md) | Samme studie; pilotkortet er hovedkortet |

Filerne bevares. Ved evidensudtræk bruges primærpublikation og kohorte som tælleenhed, aldrig antal dokumenter eller links.

### Klinisk adfærd og funktion — kildekontrol 2026-09-25

[Det målrettede søgememo](BEHAVIOURAL_SEARCH_2026-09-25.md) registrerer de nye prøveforbindelser. Başoğlu 2005 og Salcioglu 2007 bruger samme sample. Davis 2012 (NCT00333801) og Davis 2018 VIP-STAR (NCT01817712) er særskilte randomiserede forsøg. Davis 2019 PRFI er en sekundær analyse af samme VIP-STAR-deltagere. Peterson (NCT03529435), Shea (NCT02586064) og IMPACT (NCT03581981) er selvstændige RCT-kohorter.

| Kohorter/publicationer | Tælleregel |
|---|---|
| [Başoğlu 2005](../07_STUDIES/VERIFIED/2005_Basoglu_SingleSession_Behavioral_PTSD_RCT.md) ↔ [Salcioglu 2007](../07_STUDIES/VERIFIED/2007_Salcioglu_BehavioralAvoidance_Reanalysis.md) | Én kohorte; 2007 er symptomniveau-reanalyse, ikke ny sample. |
| [Davis 2012](../07_STUDIES/VERIFIED/2012_Davis_Supported_Employment_PTSD_RCT.md) ↔ [Davis 2018 VIP-STAR](../07_STUDIES/VERIFIED/2018_Davis_VIPSTAR_Supported_Employment_PTSD_RCT.md) | Separate RCT'er; hver sin ClinicalTrials.gov-registrering og forskellig sample størrelse. |
| [Davis 2018](../07_STUDIES/VERIFIED/2018_Davis_VIPSTAR_Supported_Employment_PTSD_RCT.md) ↔ [Davis 2019 PRFI](../07_STUDIES/VERIFIED/2019_Davis_VIPSTAR_Functional_Outcomes_Secondary_Analysis.md) | Én VIP-STAR-kohorte; sekundær funktionsanalyse genbruger de 541 deltagere. |
| [Peterson 2023](../07_STUDIES/VERIFIED/2023_Peterson_Massed_vs_IOP_PE_Function_RCT.md), [Shea 2023](../07_STUDIES/VERIFIED/2023_Shea_IPT_vs_PE_Function_Veterans_RCT.md) og [IMPACT 2023](../07_STUDIES/VERIFIED/2023_Rauch_IMPACT_Function_RCT.md) | Tre separate kohorter med hver sit trial-ID; ingen delt sample identificeret i det målrettede kildecheck. |
