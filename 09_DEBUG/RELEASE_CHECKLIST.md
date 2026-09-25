# FearPrime — Release Checklist

## Struktur
- [x] `VERSION` matcher seneste release.
- [x] Root README giver navigation og status.
- [x] Folder README/index-filer peger på kanoniske indgange.
- [x] Legacy/alias-filer er tydeligt mærket.

## Evidensintegritet
- [ ] Samme PMID/DOI tælles ikke dobbelt i alle synteser.  
  Kendte gentagne dokumenthenvisninger er triageret i `data/duplicate_reference_registry.csv`; ukendte par skal fortsat gennemgås.
- [ ] Reanalysis/sample-overlap er markeret for alle relevante claims.  
  Kendte Schiller/Chalkia-, Schnurr-, Berceli-pilot/alias- og Ribbens-forhold er registreret; Brunet/Roullet og flere mulige overlap er stadig uafklarede.
- [ ] Negative/null studies bevares.
- [ ] Evidence type, R-score, M-score og certainty holdes adskilt.
- [ ] Dossier-summary kan spores tilbage til konkrete studiekort.

## Links
- [x] Nye/aktive indeks-links valideret efter v0.27-cleanup.
- [x] Ingen kontrolleret aktiv indeksfil peger på en manglende sti.
- [x] Nye archive-links bruges kun til historik.
- [ ] GitHub Actions skal bekræfte de seneste audit-ændringer.  
  Utriagerede warnings blokerer stadig release; auditten køres i CI med `python tools/fearprime_repo_audit.py . --strict`

## Data
- [x] CSV-filer har gyldige headers og rækker; kontrolleres af repo-audit.
- [x] CSV-værdier kontrolleres semantisk for tilladte evidenskoder, numeriske felter og CI-rækkefølge.
- [x] YAML-filer parser syntaktisk via PyYAML i CI.  
  Semantisk validering mod egentlige YAML-schema-regler mangler stadig. Dokumenterede same-sample-kort i overlapregistret tælles ikke som ekstra seed-studier.
- [x] Study IDs er unikke; varig ID-stabilitet kræver fortsat redaktionel kontrol.
- [x] Study-card paths i data peger på eksisterende filer; studie-ID-referencer kontrolleres i CI.
- [ ] Personlige/private data er ikke committed.  
  CPR-format-checken er heuristisk og advarer til manuel kontrol; den er ikke en fuld privatdata-audit.

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
