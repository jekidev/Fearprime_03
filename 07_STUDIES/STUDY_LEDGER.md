# FearPrime — Study Ledger

**Aktiv struktur: v0.27 · 2026-09-18**

Dette er den menneskeligt læsbare indgang til FearPrimes evidensbibliotek.

Det er **ikke** længere et changelog. Historiske v0.26-noter er bevaret i [arkiv-snapshot](../09_DEBUG/ARCHIVE/STUDY_LEDGER_v0.26_SNAPSHOT.md).

## Evidenstyper

- **A — kliniske humane outcomes**
- **B — human experimental fear/learning**
- **C — prækliniske/dyreforsøg**
- **D — mekanistisk/PK/receptor/biokemi**
- **E — FearPrime-hypotese**

Bogstaverne er evidenstype, ikke automatisk kvalitetsrangering.

## Robusthed: R0–R4

R-score er claim-specifik robusthed/replikation.

- **R0** — ukontrolleret trace/hypotese
- **R1** — tidligt signal/pilot
- **R2** — kontrolleret enkeltfund eller begrænset konvergens
- **R3** — uafhængig replication/konvergens, positiv eller negativ
- **R4** — robust konvergens på relevant claim/population/outcome

R-score må ikke forveksles med reconsolidation **M0–M4** eller med certainty.

## Studiearkiv

- [VERIFIED](VERIFIED/) — humane studier og humane samlekort
- [PRECLINICAL](PRECLINICAL/) — dyreforsøg
- [MECHANISTIC](MECHANISTIC/) — PK, receptor-, target- og mekanismekilder
- [REVIEWS](REVIEWS/) — reviews og meta-analyser
- [THEORY](THEORY/) — teorikilder
- [QUALITATIVE](QUALITATIVE/) — kvalitativ forskning
- [PROTOCOLS](PROTOCOLS/) — protokoller uden færdige efficacy-outcomes

Se [07_STUDIES/README.md](README.md) for navigationsregler.

## Aktive evidensspor

### Reconsolidation
- [Boundary conditions](../03_EXTINCTION/RECONSOLIDATION_BOUNDARY_CONDITIONS.md)
- [Clinical PTSD reconsolidation](../03_EXTINCTION/CLINICAL_PTSD_RECONSOLIDATION.md)
- [Propranolol dossier](../04_CANDIDATES/PROPRANOLOL_DOSSIER.md)
- [Effect-size/RoB audit](../09_DEBUG/RECONSOLIDATION_EFFECT_SIZE_ROB_AUDIT.md)
- [Certainty profile](../09_DEBUG/RECONSOLIDATION_CERTAINTY_PROFILE.md)

### Extinction/plasticity candidates
- [Candidate matrix](../04_CANDIDATES/CANDIDATE_MATRIX.md)
- [Candidate certainty profile](../09_DEBUG/CANDIDATE_CERTAINTY_PROFILE.md)
- [Butyrat](../04_CANDIDATES/BUTYRATE_DOSSIER.md)
- [DCS](../04_CANDIDATES/DCS_DOSSIER.md)
- [FAAH/CB1](../04_CANDIDATES/ENDOCANNABINOID_FAAH_CB1_DOSSIER.md)
- [L-DOPA](../04_CANDIDATES/LDOPA_DOSSIER.md)
- [Oxytocin](../04_CANDIDATES/OXYTOCIN_DOSSIER.md)
- [Lurasidon](../04_CANDIDATES/LURASIDONE_DOSSIER.md)

### Clinical behavior
- [Schnurr et al. (2022): PE vs CPT multisite RCT](VERIFIED/2022_Schnurr_PE_CPT_Multisite_RCT.md) — klinisk symptomændring, behandlingssammenligning og foreløbig RoB-screening.
- [Ito et al. (2025): CPT og funktion i Japan](VERIFIED/2025_Ito_CPT_Function_Japan_RCT.md) — eksplorativt, selvrapporteret SDS-funktionsoutcome; ikke direkte adfærdsobservation.
- [Adfærdsevidensoversigt](../03_EXTINCTION/BEHAVIOURAL_EVIDENCE_TABLE.md) — RCT og systematiske synteser; reanalyser holdes adskilt fra nye kohorter.

### Context/interoception/sleep
- [Hippocampus/context](../02_MECHANISMS/HIPPOCAMPUS_CONTEXT_DISCRIMINATION.md)
- [Insula/interoception](../02_MECHANISMS/INSULA_INTEROCEPTION.md)
- [Nightmare/sleep dossier](../03_EXTINCTION/PTSD_NIGHTMARE_SLEEP_DOSSIER.md)

## Machine-readable evidence

Den kanoniske strukturerede parallel ligger i [data/](../data/README.md):

- `studies.csv`
- `effects.csv`
- `risk_of_bias.csv`
- `certainty.csv`
- `participant_overlap.csv`
- `search_log.csv`

Når et studie er repræsenteret i både Markdown og CSV, skal de beskrive samme publication/sample/claim og ikke tælles to gange.

## Dobbeltkort og samlekort

Et filkort er ikke nødvendigvis ét uafhængigt sample.

Eksempler:
- Berceli 2014 har et historisk alias-kort; det tælles som **samme studie**.
- Wood 2015 er én publikation med tre delstudier.
- Samlekort som “2012–2019 Endocannabinoid…” kan beskrive flere publikationer.

Participant/sample-overlap registreres separat i [participant overlap](../09_DEBUG/PARTICIPANT_OVERLAP_REGISTER.md).

## Kildeidentifikatorer

Se [Source Register](SOURCE_REGISTER.md).

Bibliografiske identifikatorer skal så vidt muligt ligge på selve studiekortet og i `data/studies.csv`, så Source Register ikke bliver endnu en parallel evidensfortolkning.

## Regel

**Study card = evidensbeskrivelse.  
Source Register = bibliografisk navigation.  
CSV = maskinlæsbar struktur.  
Dossier/model = syntese.  
Search log = søgehistorik.**

De fem lag må ikke tælles som fem separate evidenskilder.
