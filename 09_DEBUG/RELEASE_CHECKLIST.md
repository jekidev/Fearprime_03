# FearPrime — Release Checklist

## Struktur
- [x] `VERSION` matcher seneste release.
- [x] Root README giver navigation og status.
- [x] Folder README/index-filer peger på kanoniske indgange.
- [x] Legacy/alias-filer er tydeligt mærket.

## Evidensintegritet
- [ ] Samme PMID/DOI tælles ikke dobbelt.  
  Audit-tool rapporterer mulige dubletter som warnings; manuel resolution er stadig nødvendig.
- [ ] Reanalysis/sample-overlap er markeret.
- [ ] Negative/null studies bevares.
- [ ] Evidence type, R-score, M-score og certainty holdes adskilt.
- [ ] Dossier-summary kan spores tilbage til konkrete studiekort.

## Links
- [x] Nye/aktive indeks-links valideret efter v0.27-cleanup.
- [x] Ingen kontrolleret aktiv indeksfil peger på en manglende sti.
- [x] Nye archive-links bruges kun til historik.
- [ ] Repo-wide audit har ingen utriagerede hard errors.  
  Kør: `python tools/fearprime_repo_audit.py . --strict`

## Data
- [ ] CSV-filer har gyldige headers.  
  Dette kan nu kontrolleres automatisk af repo-audit.
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
- [ ] Strukturændringer dokumenteret i Structure Audit.
- [ ] Audit-warnings er manuelt triageret før versionsrelease.
