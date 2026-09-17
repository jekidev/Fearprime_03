# FearPrime — propranolol-dossier

Version 0.21 · 2026-09-17

## Formål
Dette dossier samler FearPrimes evidens for **propranolol omkring memory reactivation** ved PTSD og human emotional/fear memory.

Dossieret skelner mellem:

```text
symptomændring
fysiologisk respons
memory expression
post-reactivation updating
mekanistisk reconsolidation
```

Disse er ikke samme outcome.

Se også:
- [Reconsolidation boundary conditions](../03_EXTINCTION/RECONSOLIDATION_BOUNDARY_CONDITIONS.md)
- [Klinisk PTSD-reconsolidation](../03_EXTINCTION/CLINICAL_PTSD_RECONSOLIDATION.md)
- [Study Ledger](../07_STUDIES/STUDY_LEDGER.md)
- [Risk-of-bias template](../09_DEBUG/RISK_OF_BIAS_TEMPLATE.md)

---

## 1. Mekanistisk hypotese
Propranolol blokerer beta-adrenerge receptorer. I reconsolidation-orienterede paradigmer er hypotesen, at noradrenerg modulation omkring retrieval kan påvirke senere expression/restabilisering af et reaktiveret emotionalt memory trace.

FearPrime bruger ikke formuleringen:

```text
propranolol = memory eraser
```

Den stærkere påstand kræver dokumentation for destabilisering og restabilisering, ikke blot symptomlettelse eller lavere puls.

## 2. Tidlig human experimental memory-evidens
En meta-analyse af raske deltagere fra 2013 rapporterede, at propranolol før reconsolidation/retrieval reducerede senere emotional memory/fear-expression med samlet Hedges g omkring `0.56` (95% CI `0.13–1.00`).

PMID `23182304`.

### Begrænsning
Populationen bestod primært af raske unge voksne og paradigmerne var ikke autobiografiske PTSD-traumeminder.

## 3. Klinisk PTSD — Brunet 2008
Tidligt pilotstudie med PTSD rapporterede lavere senere fysiologisk respons efter propranolol omkring traumegenkaldelse.

- lille sample
- fysiologi var central
- ikke alle outcomes ændrede sig

**FearPrime:** klinisk signal, men R1–R2 afhængigt af den konkrete påstand.

## 4. Wood 2015 — tre negative studier
Tre små PTSD-forsøg med propranolol/mifepriston/DCS-baserede reconsolidation-protokoller fandt ingen signifikante gruppeforskelle på de centrale fysiologiske/symptomatiske outcomes.

PMID `25441015` · DOI `10.1016/j.psychres.2014.09.005`.

Dette er et vigtigt modfund. Små samples betyder dog brede usikkerheder.

**Robusthed:** R2 for påstanden, at de specifikke protokoller ikke viste den forventede effekt.

## 5. Brunet 2018 — positivt RCT-signal
60 voksne med langvarig PTSD blev randomiseret dobbeltblindet til propranolol eller placebo omkring seks ugentlige trauma-reactivation-sessioner.

Begge grupper forbedredes, mens propranololgruppen viste større symptomfald i den oprindelige rapport.

PMID `29325446` · DOI `10.1176/appi.ajp.2017.17050481`.

**FearPrime:** R2 — kontrolleret klinisk signal, men mekanismen er ikke isoleret.

## 6. Roullet 2021 — samlet nulresultat
66 voksne med langvarig PTSD blev randomiseret dobbeltblindet til propranolol eller placebo før seks ugentlige reactivation-sessioner.

Symptomer faldt i begge grupper, men der var ingen samlet propranololfordel under behandlingen, ved kort opfølgning eller på gennemsnitlige 3-måneders outcomes.

PMID `33612830` · DOI `10.1038/s41386-021-00984-w`.

**FearPrime:** R3 som modfund, fordi det er et større kontrolleret klinisk studie der begrænser generalisering fra Brunet 2018.

## 7. Meta-analyser er uenige
### 2022 reconsolidation-fokuseret meta-analyse
Raut et al. inkluderede syv studier for PTSD-symptomer og tre for fysiologiske outcomes. Analysen fandt ikke klar samlet fordel på PTSD-symptomer, SCR eller EMG; puls efter traumegenkaldelse blev reduceret. Forfatterne fremhævede høj heterogenitet, dosisvariation og små samples.

PMID `35405409` · DOI `10.1016/j.jpsychires.2022.03.045`.

### 2025 bredere PTSD meta-analyse
En nyere systematisk review/meta-analyse med søgning til oktober 2024 inkluderede syv RCT'er og rapporterede en statistisk signifikant samlet forbedring i PTSD-symptomer med propranolol.

PMID `39944616`.

### FearPrime-fortolkning
De to reviews besvarer ikke nødvendigvis identiske spørgsmål. Forskelle i:

- forebyggelse vs behandling,
- reactivation/reconsolidation vs bred propranololbrug,
- outcomevalg,
- inklusionskriterier,
- tidspunkt og dosis,

kan ændre pooled estimates.

Derfor registreres **review-konflikt**, ikke et R4-konklusionsniveau.

## 8. Outcome-dissociation
Propranolol kan sænke puls og adrenerg arousal uden nødvendigvis at ændre:

- declarative content,
- expectancy,
- SCR,
- startle,
- PTSD-symptomer,
- funktion.

FearPrime kræver derfor modalitetsspecifik rapportering.

## 9. Reconsolidation M-score vs robusthed R-score
Et propranolol-studie kan have:

- højere **M-score** hvis designet isolerer retrieval + timing + delayed test + kontroller,
- højere **R-score** hvis fundet er uafhængigt replikeret eller robust konvergent.

De to skalaer må ikke blandes.

## 10. Risk-of-bias fokus
Ved propranolol skal der især kontrolleres for:

1. blinding: fysiologiske betablokade-effekter kan gøre condition mærkbar,
2. reactivation fidelity,
3. manglende no-reactivation-kontrol,
4. forskelle i terapeutkontakt,
5. selektiv rapportering af fysiologiske vs symptomatiske outcomes,
6. små samples og brede CI,
7. post hoc subgrupper,
8. forskellig timing/formulering.

## 11. Samlet evidensstatus
| Påstand | Status |
|---|---|
| Beta-adrenerg modulation kan påvirke emotional memory expression | ✅/🟡 human evidens |
| Propranolol omkring retrieval giver konsistent PTSD-symptomfordel | 🟡/konflikt |
| Propranolol åbner eller beviser reconsolidation-vinduet | 🔴 ikke dokumenteret |
| Propranolol reducerer adrenerg fysiologi omkring recall | 🟡 støtte |
| Klinisk rutinebrug som reconsolidation-behandling er robust etableret | 🔴 |

## 12. Debug
Den største fejl ville være at bruge ændret puls eller symptomscore som direkte bevis for ændring af det oprindelige trauma memory trace. FearPrime fastholder, at klinisk effekt og mekanistisk reconsolidation er to separate spørgsmål.
