# FearPrime v1.0 — Gap Audit

**Version 0.32 · 2026-09-25**

## Rolle

Denne fil svarer kun på:

> **Hvad mangler, før FearPrime med rimelighed kan kaldes v1.0?**

Domænedækning ligger i [Coverage Plan](COVERAGE_PLAN.md).  
Historisk v0.26 audit ligger i [arkivet](ARCHIVE/FEARPRIME_V1_GAP_AUDIT_v0.26_SNAPSHOT.md).

## Definition af v1.0

FearPrime v1.0 kræver ikke, at alle biologiske hypoteser er korrekte.

Det kræver, at frameworket er:
1. navigerbart,
2. metodisk konsistent,
3. reproducerbart nok til audit,
4. eksplicit om usikkerhed,
5. maskinlæsbar på centrale evidensfelter,
6. fri for skjult dobbelt-tælling,
7. tydelig om forskellen mellem model, mekanisme, studie og clinical efficacy.

## Readiness

| Krav | Status |
|---|---|
| Klar repo-arkitektur og kanoniske indgange | ✅ v0.27 cleanup |
| README uden indlejret changelog | ✅ |
| Central changelog/version | ✅ |
| Studie-/kilde-/data-lag adskilt | ✅ |
| Evidence-type rules | ✅ |
| R0–R4 robusthed adskilt fra M0–M4 mekanisme | ✅ |
| Claim-level certainty framework | ✅/🟡 |
| Study-level RoB på centrale humane claims | 🟡 — foreløbige screens findes for PE/CPT-RCT og Kooistra-forsøget; fuld RoB 2 og bredere kernekorpus mangler |
| Effect-size/CI på centrale humane claims | 🟡 — PE/CPT-estimater er indkodet; Kooistra-studiets numeriske effekter er markeret som ikke udtrukket; bredere dækning mangler |
| Participant-overlap audit | 🟡 — Schnurr-forbindelsen er verificeret, og Kooistra (N=60) er registreret som foreløbig separat kohorte; Brunet/Roullet og øvrige mulige overlap mangler kontrol |
| Reproducerbare searches for kerneområder | 🟡 — rekonsolidering har en delvis eksport; adfærd og øvrige kerneområder mangler præcise søgninger, screening og deduplikering |
| Native PubMed hit counts/export for centrale searches | 🟡 — der mangler komplet direkte eksport fra PubMed for de øvrige kerneområder |
| Publication-bias vurdering | 🔴/🟡 |
| Reviewer/screening-status eksplicit | 🟡 — adfærdsevidensoversigten angiver sin afgrænsning; systematisk screening med uafhængige reviewere mangler stadig |
| Machine-readable study/effect/RoB/certainty data | ✅/🟡 — PE/CPT- og Kooistra-studier samt Kooistra-status for ikke-udtrukne effekter er registreret; samlet data-paritet er fortsat delvis |
| Link/integrity QA efter strukturændringer | ✅ — relative links og referencer valideres i streng CI; kendte gentagne DOI-henvisninger er triageret i reference-registret |
| Dokumenteret release checklist | ✅ |

## Vigtigste blockers

### 1. Search completeness
Reconsolidation har et verificeret screening/export-set, men ikke komplet native PubMed/PRISMA-flow.

Før v1.0 bør kerneområder have:
- exact query,
- søgedato,
- total hit count når muligt,
- screeningstatus,
- inclusion/exclusion,
- deduplication,
- update cadence.

### 2. Quantitative evidence
Flere centrale claims mangler stadig fuld:
- effect-size extraction,
- CI,
- RoB,
- sample-overlap kontrol.

### 3. Certainty
Ingen claim bør få HIGH alene på baggrund af frameworkets interne vurdering.

HIGH kræver:
- tilstrækkelig search completeness,
- direkte population/outcome,
- tilstrækkelig precision,
- konsistens/replication,
- RoB,
- publication-bias vurdering.

### 4. Data completeness
`data/` er strukturelt etableret, men er endnu et seed-korpus, ikke en komplet spejling af alle 07_STUDIES-filer.

### 5. QA/release
`tools/fearprime_repo_audit.py` automatiserer nu:
- interne Markdown-linktargets og versionsmatch,
- CSV-struktur, kontrollerede evidence-værdier, numeriske effect/CI-felter samt study-ID/effect/RoB- og studiekortsti-referencer,
- YAML-syntaks via PyYAML,
- CPR-mønstre som advarsler til manuel kontrol,
- orphan diagnostics,
- triage af dokumenterede gentagne DOI/PMID-par via `data/duplicate_reference_registry.csv`, mens ikke-registrerede dubletter fortsat advares.

Følgende mangler stadig som pålidelige release-gates:
- CSV-felter har nu grundlæggende semantiske kontroller i CI; YAML-syntaks kontrolleres, men semantisk validering mod formelle skemaer mangler stadig,
- studiekortstier og CSV-krydsreferencer kontrolleres nu som CI-fejl; fuld dataparitet mangler stadig,
- kendte gentagne kildepar er registreret maskinlæsbart og triageret; bredere kontrol af deltageroverlap mangler stadig,
- en CPR-formatkontrol giver nu en advarsel til manuel gennemgang; fuld kontrol for persondata mangler stadig,
- triage af audit-advarsler før release; seed-dækningsadvarslen kræver stadig en afgrænsningsbeslutning, og den nye semantiske audit skal bekræftes i GitHub Actions.

## Ikke blockers for v1.0

Følgende behøver ikke være “løst” før v1.0:
- at en bestemt kandidat viser efficacy,
- at reconsolidation er endeligt afgjort,
- at alle P3-hypoteser har humane data,
- at alle ressourcefiler er systematiske reviews.

v1.0 handler om **framework-kvalitet**, ikke om at fremtvinge positive forskningsresultater.

Se også [Release Checklist](RELEASE_CHECKLIST.md).

## Release gate

FearPrime kan kaldes v1.0, når:

1. alle vigtige README/index-links er valideret,
2. kerneclaims har synligt evidence trail,
3. centrale humane claims har mindst baseline RoB/effect extraction,
4. duplicate/sample-overlap er håndteret,
5. search completeness er dokumenteret for kerneområder,
6. datafiler parser korrekt,
7. changelog/release-version er samlet,
8. ingen historisk snapshot bruges som aktiv source-of-truth.

## Næste audit

Næste gap-audit bør kun opdatere denne checklist — ikke gentage Coverage Plan eller detaljerede science summaries.
