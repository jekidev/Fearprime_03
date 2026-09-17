# FearPrime — reconsolidation effect-size & RoB audit

Version 0.21 · 2026-09-17

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

### Rapporterede størrelser
- justeret post-treatment CAPS-gruppeforskel: `11.50` point til fordel for propranolol i originalrapporten.
- within-group Cohen d, CAPS: propranolol `1.76`, placebo `1.25`.
- PCL-S: estimeret ekstra fald `2.43` point/uge, samlet rapporteret forskel `14.58` point.
- within-group Cohen d, PCL-S: propranolol `2.74`, placebo `0.55`.

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

### Rapporterede resultater
- PCL-S fald: propranolol `39.28%`, placebo `34.48%`.
- treatment-period interaction: ikke signifikant (`F(6,330)=1.682`, `p=.125`).
- within-group Cohen d for PCL-S: propranolol `1.249`, placebo `1.411`.
- 3-måneders PCL-S: propranolol `45.16 ± 19.55`, placebo `41.48 ± 19.04`, `p=.500`.
- baseline-severity subgruppe: mellemgruppe d ved 3 mdr. ca. `0.520` for PCL-S i severe subgroup; eksplorativt/post hoc-lignende moderatorfund og ikke et samlet primært treatment effect.

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

## 3. Chalkia 2020 — registreret retrieval-extinction replication
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

## 4. Schiller 2010 — klassisk retrieval-extinction signal
Det oprindelige studie rapporterede reduceret return of fear efter extinction inden for et retrieval-relateret tidsvindue.

Senere verification/reanalysis af originaldata viste, at centrale group differences var følsomme over for kvalitative eksklusionsbeslutninger, og en mere principiel reanalyse reducerede/eliminerede centrale forskelle.

Verification report: DOI `10.1016/j.cortex.2020.03.031` · PMID `32563517`.

### RoB-noter
- indflydelsesrig original demonstration.
- rapporterings- og eksklusionsproblemer i originalmaterialet øger bias-bekymring.
- direkte registreret replication var negativ.

**Robusthed for den oprindelige stærke procedurepåstand:** R2 → nedgraderet af reanalyse og replication.  
**RoB:** HIGH/SOME for den stærke oprindelige konklusion.

---

## 5. PTSD-propranolol meta-analyse 2022
Syv studier indgik i PTSD-symptommeta-analysen og tre i fysiologiske analyser.

Rapporteret konklusion:
- ingen klar samlet fordel på PTSD-symptomer,
- ingen klar effekt på SCR eller EMG,
- reduceret puls efter trauma recall,
- høj heterogenitet, dosisvariation og små samples begrænser sikkerheden.

PMID `35405409` · DOI `10.1016/j.jpsychires.2022.03.045`.

**Robusthed:** R3 review-level konflikt/modfund, ikke R4.

---

## 6. PTSD propranolol meta-analyse 2025
En nyere review/meta-analyse med søgning til oktober 2024 inkluderede syv RCT'er og rapporterede signifikant samlet forbedring i PTSD-symptomer med propranolol og lav statistisk heterogenitet i den valgte model.

PMID `39944616`.

### RoB-/interpretationsnote
Denne analyse er bredere end et rent reconsolidation-spørgsmål og kan inkludere forskellige interventionsformål/tidspunkter. Den må derfor ikke bruges som direkte mekanismebevis for trauma-memory reconsolidation.

**Robusthed:** R2–R3 for en bred symptom-påstand; review-konflikt består.

---

# Samlet audit
| Spor | Effektretning | R | M | RoB | Hovedproblem |
|---|---|---:|---:|---|---|
| Brunet 2018 | positiv | R2 | M2–M3 | SOME | mekanisme ikke isoleret |
| Roullet 2021 | samlet nul | R3 | M2 | SOME | begge grupper reactivation |
| Schiller 2010 | positiv | R2 | M2–M3 | SOME/HIGH | eksklusion/analyse + replication failure |
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
Udtræk fuldtekstdata og CI fra de resterende kliniske reconsolidation-studier, og opret samme RoB+effect-schema på studiekortniveau i stedet for kun i denne samlede audit.
