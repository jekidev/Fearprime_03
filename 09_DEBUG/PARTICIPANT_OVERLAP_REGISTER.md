# FearPrime — participant overlap register

Version 0.22 · 2026-09-18

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
