# FearPrime — Source Register

**Aktiv struktur: v0.27 · 2026-09-18**

Source Register er nu et **bibliografisk navigationslag**, ikke endnu en parallel Study Ledger eller versionshistorik.

Den tidligere komplette v0.26-registerfil er bevaret ordret i:
[Source Register v0.26 snapshot](../09_DEBUG/ARCHIVE/SOURCE_REGISTER_v0.26_SNAPSHOT.md).

## Kilde-of-truth

For en konkret publikation er prioriteten:

1. det individuelle studiekort i `07_STUDIES/`,
2. bibliografiske felter i [data/studies.csv](../data/studies.csv),
3. specialiserede source indexes,
4. dette navigationsregister.

Hvis de er uenige, skal den primære publikation genkontrolleres.

## Bibliografiske hovedområder

### Humane studier
[VERIFIED/](VERIFIED/)

### Prækliniske studier
[PRECLINICAL/](PRECLINICAL/)

### Mekanistiske/PK/receptor-kilder
[MECHANISTIC/](MECHANISTIC/)

Specialindeks:
- [Mechanism Source Index](MECHANISTIC/MECHANISM_SOURCE_INDEX.md)
- [Plasticity Window Source Index](MECHANISTIC/PLASTICITY_WINDOW_SOURCE_INDEX.md)
- [PNN Source Index](MECHANISTIC/PNN_SOURCE_INDEX.md)

### Reviews/meta-analyser
[REVIEWS/](REVIEWS/)

### Teori
[THEORY/](THEORY/)

### Kvalitativ forskning
[QUALITATIVE/](QUALITATIVE/)

### Protokoller
[PROTOCOLS/](PROTOCOLS/)

## Søge- og screeningproveniens

Søgehistorik hører i `09_DEBUG/`, ikke i Source Register.

Aktive indgange:
- [Systematic Search Protocol](../09_DEBUG/SYSTEMATIC_SEARCH_PROTOCOL.md)
- [Reconsolidation Search Log](../09_DEBUG/RECONSOLIDATION_SEARCH_LOG.md)
- [Dateret reconsolidation search](../09_DEBUG/RECONSOLIDATION_SEARCH_2026-09-18.md)
- [PubMed export/screening-status](../09_DEBUG/PUBMED_RECONSOLIDATION_EXPORT_2026-09-18.md)

Maskinlæsbar søgelog:
[data/search_log.csv](../data/search_log.csv)

## Citation-regel

Hvert nyt studiekort bør, når det findes, indeholde:
- originaltitel,
- år,
- DOI,
- PMID/PMCID,
- registrerings-ID,
- population/design,
- kontrolniveau.

Dossierer må gerne linke til kilder, men de bør ikke udvikle deres eget konkurrerende bibliografiske register.

## Historik

Alle tidligere PMID-/DOI-lister og versionsudvidelser er bevaret i v0.26-snapshot-filen. De er ikke slettet; de er flyttet ud af den aktive navigation for at undgå tredobbelt vedligeholdelse mellem README, Study Ledger og Source Register.
