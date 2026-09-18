# FearPrime — Release Checklist

## Struktur
- [ ] `VERSION` matcher seneste release.
- [ ] `CHANGELOG.md` har release-entry.
- [ ] Root README er navigation/status, ikke changelog.
- [ ] Folder README/index-filer peger på kanoniske indgange.
- [ ] Legacy/alias-filer er tydeligt mærket.

## Evidensintegritet
- [ ] Samme PMID/DOI tælles ikke dobbelt.
- [ ] Reanalysis/sample-overlap er markeret.
- [ ] Negative/null studies bevares.
- [ ] Evidence type, R-score, M-score og certainty holdes adskilt.
- [ ] Dossier-summary kan spores tilbage til konkrete studiekort.

## Links
- [ ] Nye/interne links valideret.
- [ ] Ingen aktiv fil peger på slettet sti.
- [ ] Archive-links bruges kun til historik.

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
