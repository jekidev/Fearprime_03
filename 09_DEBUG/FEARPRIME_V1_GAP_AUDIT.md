# FearPrime v1.0 — Gap Audit

**Version 0.31 · 2026-09-22**

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
| Study-level RoB på centrale humane claims | 🟡 — første større PE/CPT-RCT screenet; resten af kernekorpus mangler |
| Effect-size/CI på centrale humane claims | 🟡 — primært CAPS-5-estimat og responsmål udtrukket for PE/CPT-RCT; bredere dækning mangler |
| Participant-overlap audit | 🟡 — Schnurr 2022/2024 same-sample link verified; Brunet/Roullet and other possible overlaps still need checking |
| Reproducerbare searches for kerneområder | 🟡 — reconsolidation has partial export; behavior and remaining domains still need exact queries, screening and dedup |
| Native PubMed hit counts/export for centrale searches | 🟡 — no complete native export for the remaining core domains |
| Publication-bias vurdering | 🔴/🟡 |
| Reviewer/screening-status eksplicit | 🟡 — new behavioral evidence table states its scope; systematic reviewer-level screening remains incomplete |
| Machine-readable study/effect/RoB/certainty data | ✅/🟡 — PE/CPT-studie og fire effektmål tilføjet; samlet data-paritet er fortsat delvis |
| Link/integrity QA efter strukturændringer | ✅ — relative links rettet, streng CI-kontrol; fire gentagne DOI-henvisninger er dokumenteret i overlapregistret |
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
- CSV-struktur samt study-ID/effect/RoB- og studiekortsti-referencer,
- YAML-syntaks via PyYAML,
- CPR-mønstre som advarsler til manuel kontrol,
- orphan diagnostics,
- triage af dokumenterede gentagne DOI/PMID-par via `data/duplicate_reference_registry.csv`, mens ikke-registrerede dubletter fortsat advares.

Følgende mangler stadig som pålidelige release-gates:
- YAML syntax validation now runs in CI; semantic validation against formal schemas is still open,
- study-card path and CSV cross-reference checks now run as strict CI errors; full data parity remains open,
- known repeated-source pairs are machine-registered and triaged; broader participant-overlap resolution remains open,
- a CPR-format scan now raises a manual-review warning; comprehensive personal-data detection is still open,
- triage af audit-warnings før release; the known seed-coverage warning still requires a deliberate scope decision.

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
