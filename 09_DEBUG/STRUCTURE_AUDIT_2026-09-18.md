# FearPrime — Structure Audit 2026-09-18

## Scope
Hele repoets tree blev scannet før oprydning.

Pre-cleanup:
- 252 filer
- 20 mapper
- ca. 880 KB tekst/data
- 145 filer under `07_STUDIES/`
- 22 filer under `09_DEBUG/`

Der blev ikke fundet identiske blob-filer.

## Primære problemer

### 1. README som changelog
Root README indeholdt 21 versionssektioner og fungerede samtidig som navigation, status, changelog og research summary.

**Løsning:** aktiv README er nu kort navigation/status. Hele v0.26-versionen er arkiveret ordret.

### 2. Study Ledger og Source Register som parallel historik
Begge filer indeholdt evidensnavigation plus gentagen versionshistorik.

**Løsning:**
- Study Ledger = evidensnavigation/robusthed.
- Source Register = bibliografisk navigation.
- gamle fulde filer bevaret ordret i `09_DEBUG/ARCHIVE/`.

### 3. Parallelle compact/master models
- `models/FEAR_EXTINCTION_MODEL.md` overlapper Extinction Engine.
- `02_MECHANISMS/MECHANISM_MAP.md` overlapper Fear Circuit Master Map.

**Løsning:** compact-filerne bevares som legacy/intro og peger på kanonisk model.

### 4. Kandidat-specialmoduler så ud som parallelle dossiers
Særligt:
- butyrate formulation brain,
- butyrate head-to-head,
- lurasidone receptors/learning,
- core synthesis.

**Løsning:** scope-markører gør hoveddossier vs specialmodul eksplicit.

### 5. Berceli 2014 dobbeltkort
To filer beskrev samme PMID 25568824 / DOI 10.7453/gahmj.2014.032.

**Løsning:** det kortere kort er markeret som alias; Pilot-kortet er kanonisk. Begge bevares.

### 6. Debug-status overlap
Coverage Plan og v1 Gap Audit gentog status.

**Løsning:**
- Coverage Plan = domænedækning.
- Gap Audit = v1 release-readiness.
- begge gamle v0.26-versioner arkiveret.

### 7. Search log overlap
Rolling reconsolidation log og dateret search kunne forveksles.

**Løsning:**
- rolling log = kumulativ provenance,
- dateret search = immutable snapshot.

### 8. Mekanisme-source-index overlap
MECHANISM_SOURCE_INDEX, PNN_SOURCE_INDEX og PLASTICITY_WINDOW_SOURCE_INDEX havde delvist overlappende kilder.

**Løsning:** Mechanism Source Index er master; PNN/Plasticity er specialindeks.

## Bevidst bevaret krydsindeksering

Følgende er ikke behandlet som problem:
- resources efter medietype og tema,
- study cards + machine-readable CSV,
- dossiers + certainty profiles,
- models + mechanism modules.

De er forskellige views af samme evidens og har nu eksplicit forskellige roller.

## Nye kanoniske navigationslag
- `README.md`
- `REPO_MAP.md`
- `CHANGELOG.md`
- `VERSION`
- README-filer i mechanisms/extinction/candidates/models/measurement/studies/debug.

## Bevaring
Ingen forskningsfil blev slettet.

Historisk indhold fra de store indeksfiler er bevaret i:
- `ARCHIVE/README_v0.26_SNAPSHOT.md`
- `ARCHIVE/STUDY_LEDGER_v0.26_SNAPSHOT.md`
- `ARCHIVE/SOURCE_REGISTER_v0.26_SNAPSHOT.md`
- `ARCHIVE/COVERAGE_PLAN_v0.26_SNAPSHOT.md`
- `ARCHIVE/FEARPRIME_V1_GAP_AUDIT_v0.26_SNAPSHOT.md`

## Fremtidig regel
Nye resultater skal gå til den filtype, der ejer ansvaret:
- nyt studie → study card + data row,
- ny kandidatfortolkning → kandidatdossier,
- ny claim certainty → certainty profile/data,
- ny search → dated search log,
- ny release → CHANGELOG,
- nyt roadmap-hul → Coverage Plan,
- nyt v1 blocker-status → Gap Audit.
