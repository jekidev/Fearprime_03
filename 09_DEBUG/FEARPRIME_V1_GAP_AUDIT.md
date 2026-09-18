# FearPrime v1.0 — Gap Audit

**Version 0.27 · 2026-09-18**

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
| Study-level RoB på centrale humane claims | 🟡 |
| Effect-size/CI på centrale humane claims | 🟡 |
| Participant-overlap audit | 🟡 |
| Reproducerbare searches for kerneområder | 🟡 |
| Native PubMed hit counts/export for centrale searches | 🟡 |
| Publication-bias vurdering | 🔴/🟡 |
| Reviewer/screening-status eksplicit | 🟡 |
| Machine-readable study/effect/RoB/certainty data | ✅/🟡 |
| Link/integrity QA efter strukturændringer | 🟡 |
| Dokumenteret release checklist | 🔴 |

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
Der mangler en fast release-check:
- interne links,
- orphan files,
- duplicate publication IDs,
- version mismatch,
- schema validation,
- CSV/YAML parsing,
- no-personal-data check.

## Ikke blockers for v1.0

Følgende behøver ikke være “løst” før v1.0:
- at en bestemt kandidat viser efficacy,
- at reconsolidation er endeligt afgjort,
- at alle P3-hypoteser har humane data,
- at alle ressourcefiler er systematiske reviews.

v1.0 handler om **framework-kvalitet**, ikke om at fremtvinge positive forskningsresultater.

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
