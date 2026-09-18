# FearPrime — Release Checklist

## Struktur
- [x] `VERSION` matcher seneste release.
- [x] `CHANGELOG.md` har release-entry.
- [x] Root README er navigation/status, ikke changelog.
- [x] Folder README/index-filer peger på kanoniske indgange.
- [x] Legacy/alias-filer er tydeligt mærket.

## Evidensintegritet
- [ ] Samme PMID/DOI tælles ikke dobbelt.
- [ ] Reanalysis/sample-overlap er markeret.
- [ ] Negative/null studies bevares.
- [ ] Evidence type, R-score, M-score og certainty holdes adskilt.
- [ ] Dossier-summary kan spores tilbage til konkrete studiekort.

## Links
- [x] Nye/aktive indeks-links valideret efter v0.27-cleanup.
- [x] Ingen kontrolleret aktiv indeksfil peger på en manglende sti.
- [x] Nye archive-links bruges kun til historik.

## Data
- [ ] CSV-filer har gyldige headers.
- [ ] YAML-schemas parser.
- [ ] Study IDs er stabile.
- [ ] Study-card paths i data peger på eksisterende filer.
- [ ] Personlige/private data er ikke committed.

## Search
- [ ] Exact query + dato bevaret.
- [ ] Search log og dated snapshot har forskellige roller.
- [ ] Inclusion/exclusion og dedup dokumenteret hvor relevant.
- [ ] Search completeness beskrives uden at opfinde hit counts.

## Release
- [ ] Coverage Plan opdateret kun ved coverage-ændring.
- [ ] Gap Audit opdateret kun ved readiness-ændring.
- [ ] Strukturændringer dokumenteret i Structure Audit/Changelog.
