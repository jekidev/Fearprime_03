# FearPrime — reconsolidation effect-size & RoB audit

Version 0.23 · 2026-09-18

## Formål
Dette dokument starter P2-arbejdet med at koble **effektstørrelser, usikkerhed, robusthed og risk-of-bias** til de centrale humane reconsolidation-/reactivation-studier.

Det er en målrettet audit, ikke en ny meta-analyse.

Se også:
- [Risk of Bias template](RISK_OF_BIAS_TEMPLATE.md)
- [Reconsolidation boundary conditions](../03_EXTINCTION/RECONSOLIDATION_BOUNDARY_CONDITIONS.md)
- [Study Ledger](../07_STUDIES/STUDY_LEDGER.md)
- [Propranolol-dossier](../04_CANDIDATES/PROPRANOLOL_DOSSIER.md)

---

## 1. Brunet 2018 — PTSD, propranolol + reactivation
**N:** 60 voksne med langvarig PTSD.  
**Design:** dobbeltblindet placebo-kontrolleret RCT, seks ugentlige sessioner.

### Rapporterede og udledte størrelser
- justeret post-treatment CAPS-gruppeforskel: `11.50` point til fordel for propranolol; rapporteret SE `5.24`.
- FearPrime-beregnet normal-approksimeret 95% CI for CAPS-forskellen: **1.23 til 21.77**. CI'en er beregnet som estimate ± 1.96×SE og er ikke kopieret som et rapporteret CI.
- within-group Cohen d, CAPS: propranolol `1.76`, placebo `1.25` — disse er **ikke** treatment-effect d.
- PCL-S: samlet rapporteret model-/gruppeforskel `14.58` point med SE `3.30`.
- FearPrime-beregnet normal-approksimeret 95% CI for PCL-S-forskellen: **8.11 til 21.05**.
- within-group Cohen d, PCL-S: propranolol `2.74`, placebo `0.55` — heller ikke between-group treatment effects.

DOI `10.1176/appi.ajp.2017.17050481` · PMID `29325446`.

### RoB-noter
- randomisering/dobbeltblinding: styrke.
- betablokade kan potentielt kompromittere blinding via mærkbare fysiologiske effekter.
- begge grupper fik repeated trauma reactivation; mekanismen kan ikke isoleres som reconsolidation alene.
- stor within-group d må ikke fortolkes som treatment-effect d.

**Robusthed:** R2.  
**Mekanistisk inferens:** højst M2–M3, afhængigt af den specifikke påstand.  
**RoB:** SOME.

---

## 2. Roullet 2021 — PTSD, direkte klinisk ikke-replikation
**N:** 66 randomiseret, 33/33.

### Rapporterede og udledte resultater
- PCL-S fald: propranolol `39.28%`, placebo `34.48%`; arm-level ændring, ikke treatment effect.
- samlet treatment effect: `F(1,55)=0.267`, `p=.607`; FearPrime-beregnet partial η² ≈ **0.0048**.
- treatment × session: `F(6,330)=1.682`, `p=.125`; FearPrime-beregnet partial η² ≈ **0.0297**.
- within-group Cohen d for PCL-S: propranolol `1.249`, placebo `1.411`; ikke between-group effect.
- 3-måneders PCL-S: propranolol `45.16 ± 19.55`, placebo `41.48 ± 19.04`, `p=.500`.
- FearPrime-beregnet raw mean difference (propranolol − placebo) ved 3 måneder: **+3.68**, 95% CI **−7.20 til 14.56**. Højere PCL-S er værre; fortegnet favoriserer derfor ikke propranolol, og CI krydser nul.
- uge 7→18 ændringsforskel: **−2.02**, 95% CI **−7.51 til 3.47**, `p=.464`; også kompatibel med nul.
- baseline-severity subgruppe behandles fortsat som eksplorativ og må ikke erstatte det samlede nulresultat.

DOI `10.1038/s41386-021-00984-w` · PMID `33612830`.

### RoB-noter
- dobbeltblindet RCT: styrke.
- alder var forskellig mellem grupper ved baseline.
- begge grupper fik repeated reactivation; ingen no-reactivation arm.
- post hoc/severity-moderation må ikke erstatte det samlede nulresultat.
- follow-up havde attrition/withdrawal relateret til videre behandling.

**Robusthed:** R3 som negativ direkte klinisk konvergens mod en generel propranololfordel.  
**Mekanistisk inferens:** M2.  
**RoB:** SOME.

---

## 3. Wood 2015 — tre negative kliniske PTSD-eksperimenter
De tre små randomiserede eksperimenter rapporterede ingen signifikante gruppeforskelle i de centrale fysiologiske eller kliniske outcomes.

### Effect-size status
De summary-data, der er verificeret i denne runde, er **ikke tilstrækkelige til at beregne et forsvarligt standardiseret between-group effect estimate med 95% CI** uden yderligere fuldtekstudtræk.

FearPrime registrerer derfor:
`not_derivable_from_verified_data`

Dette er metodisk stærkere end at imputere SD, korrelationer eller andre manglende størrelser.

**Robusthed:** R2.  
**Mekanistisk inferens:** M2.  
**RoB:** SOME.

---

## 4. Chalkia 2020 — registreret retrieval-extinction replication
**Design:** højt powered, direkte uafhængig registreret replikation af centrale betingelser fra Schiller 2010.

### Effektstørrelse / powergrundlag
- planlagt ud fra meta-analytisk effekt `g = 0.53` for forskel i spontaneous recovery.
- den oprindelige Schiller-betingelse, som blev replikeret, svarede til ca. `g = 0.73` i powerbeskrivelsen.
- replikationen fandt ikke den forventede vedvarende fordel af reactivation-extinction over almindelig extinction.

DOI `10.1016/j.cortex.2020.04.017` · PMID `32580869`.

### RoB-noter
- preregistration/direkte replication: stor styrke.
- større sample end originalen.
- udfordringer i originalens eksklusionskriterier var kendt før/under replication-programmet og blev undersøgt separat.

**Robusthed:** R3 for modfundet.  
**Mekanistisk inferens:** M2 for selve reactivation-extinction-proceduren; nulresultatet begrænser stærkere inference.  
**RoB:** LOW–SOME.

---

## 5. Schiller 2010 — klassisk retrieval-extinction signal
Det oprindelige studie rapporterede reduceret return of fear efter extinction inden for et retrieval-relateret tidsvindue.

Senere verification/reanalysis af originaldata viste, at centrale group differences var følsomme over for kvalitative eksklusionsbeslutninger, og en mere principiel reanalyse reducerede/eliminerede centrale forskelle.

Verification report: DOI `10.1016/j.cortex.2020.03.031` · PMID `32563517`.

### Reanalyse
I 2020-verification report, med den rapporterede originale inklusionsgruppe, var den centrale group × time-test for spontaneous recovery `F(2,62)=2.49`, `p=.091`, partial η² ≈ `0.07`.

Det er en **reanalyse af originaldata**, ikke en ny uafhængig sample.

### RoB-noter
- indflydelsesrig original demonstration.
- rapporterings- og eksklusionsproblemer i originalmaterialet øger bias-bekymring.
- verification/reanalysis svækkede den centrale stærke between-group fortolkning.
- direkte registreret replication var negativ.

**Robusthed for den oprindelige stærke procedurepåstand:** R2 → nedgraderet af reanalyse og replication.  
**RoB:** HIGH/SOME for den stærke oprindelige konklusion.

---

## 6. PTSD-propranolol meta-analyse 2022
Syv studier indgik i PTSD-symptommeta-analysen og tre i fysiologiske analyser.

Rapporteret konklusion:
- ingen klar samlet fordel på PTSD-symptomer,
- ingen klar effekt på SCR eller EMG,
- reduceret puls efter trauma recall,
- høj heterogenitet, dosisvariation og små samples begrænser sikkerheden.

PMID `35405409` · DOI `10.1016/j.jpsychires.2022.03.045`.

**Robusthed:** R3 review-level konflikt/modfund, ikke R4.

---

## 7. PTSD propranolol meta-analyse 2025
En nyere review/meta-analyse med søgning til oktober 2024 inkluderede syv RCT'er og rapporterede signifikant samlet forbedring i PTSD-symptomer med propranolol og lav statistisk heterogenitet i den valgte model.

PMID `39944616`.

### RoB-/interpretationsnote
Denne analyse er bredere end et rent reconsolidation-spørgsmål og kan inkludere forskellige interventionsformål/tidspunkter. Den må derfor ikke bruges som direkte mekanismebevis for trauma-memory reconsolidation.

**Robusthed:** R2–R3 for en bred symptom-påstand; review-konflikt består.

---

## 8. Nyere boundary-/review-opdatering 2025–2026

### Chen et al. 2025
Humant fear-conditioning-studie, der kvantificerer prediction error mere gradueret. Det understøtter PE som moderator, men ikke en universel destabiliseringsmarkør. R2 / M2.

### Paul & Asthana 2025
Humant laboratoriestudie der undersøger memory strength × prediction error. Foreløbigt R1–R2 / M2 indtil fuld RoB og effect extraction er udført.

### Xia et al. 2026
Systematisk review af akut farmakologisk modulation af human aversiv hukommelse. Reviewet beskriver relativt stærk laboratoriekonvergens for propranolol/reconsolidation i raske mennesker. Dette er **ikke** det samme som klinisk PTSD-effekt.

---

# Samlet audit
| Spor | Effektretning | R | M | RoB | Hovedproblem |
|---|---|---:|---:|---|---|
| Brunet 2018 | positiv | R2 | M2–M3 | SOME | mekanisme ikke isoleret |
| Roullet 2021 | samlet nul | R3 | M2 | SOME | meget lille samlet treatment η²; CI'er krydser nul |
| Wood 2015 | nul | R2 | M2 | SOME | effect/CI ikke beregnelig fra verificerede summary-data |
| Schiller 2010 | positiv originalpåstand | R2 | M2–M3 | SOME/HIGH | reanalyse group×time p=.091 + replication failure |
| Chalkia 2020 | negativ replication | R3 | M2 | LOW–SOME | paradigmespecificitet |
| Propranolol meta 2022 | samlet utilstrækkelig | R3 | NA | SOME | heterogenitet/små samples |
| Propranolol meta 2025 | positiv bred symptom-påstand | R2–R3 | NA | SOME | bredere spørgsmål end reconsolidation |

## Konklusion
FearPrime kan ikke udlede én stabil klinisk propranolol/reconsolidation-effekt fra den nuværende litteratur. Den mest forsvarlige læsning er:

1. biologisk reconsolidation er plausibel og stærkt præklinisk funderet,
2. enkelte humane paradigmer viser post-reactivation-effekter,
3. direkte humane procedurepåstande har væsentlige replikations- og boundary-problemer,
4. kliniske propranololresultater er blandede,
5. treatment effect og mekanistisk inference skal fortsat rapporteres separat.

## Næste P2-opgave
1. fuldtekst-udtræk af observeret standardized effect + CI fra Chalkia replication,
2. fuld statistisk udtrækning af Wood-delstudierne,
3. afstemning af 2022 vs. 2025 propranolol-meta-analysernes inklusionssæt,
4. udvidelse af study-level RoB/effect-tabeller til resten af de humane reconsolidation-studier.

Maskinlæsbare effekter findes i [data/effects.csv](../data/effects.csv).
