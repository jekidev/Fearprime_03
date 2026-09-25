# FearPrime — beregningsværktøjer

Værktøjsversion 0.3 · repo v0.31

Beregningsværktøjerne bruger standardbiblioteket. Repo-auditten bruger desuden PyYAML til syntakskontrol af YAML-filer (`python -m pip install PyYAML`).

## 1. Beregner for forventningsopdatering

Input er en CSV med felterne fra [ViolEx-skabelonen](../data/violex_exposure_template.csv).

```bash
python tools/fearprime_bayesian_calculator.py data/computational_demo.csv -o out/violex_calculated.csv
```

Beregneren tilføjer mål for forudsigelsesfejl med fortegn og absolut værdi, forventningsopdatering, opdateringseffektivitet, tilpasnings-/fastholdelseslignende scorer, ændring i overordnet overbevisning, fastholdelse næste dag og generalisering.

Scorer for tilpasning og fastholdelse af overbevisninger er **projektets heuristikker**, ikke validerede kliniske skalaer. Beregnerens eget versionsnummer er fortsat v0.1.

## 2. Sammenligning af beregningsmodeller

```bash
python tools/fearprime_model_compare.py data/computational_demo.csv \
  -o out/model_comparison.csv \
  --predictions out/model_predictions.csv
```

Alle modeller forudsiger samme mål: `post_threat_expectancy`.

| Model | Parametre | Fortolkning |
|---|---:|---|
| Ingen opdatering | 0 | Reference uden læring |
| Rescorla–Wagner | 1 | Sammenligningsmodel med deltaregel |
| Bayes med gradueret evidens | 1 | Forenklet bayesiansk sammenligning |
| HGF-lignende tilpasning til omskiftelighed | 3 | Tilnærmelse, ikke en fuld HGF-implementering |
| Aktiv-inferens-inspireret vægtning og handlingsvalg | 3 | Tilnærmelse, ikke en fuld aktiv-inferens-/POMDP-model |

Resultatet indeholder SSE, MAE, RMSE, gaussisk negativ log-likelihood, AIC, BIC og ΔBIC. Rangordningen er udforskende og foretages på de samme data, som modellerne tilpasses til; den er ikke en uafhængig test af forudsigelsesevne. Modelsammenlignerens eget versionsnummer er fortsat v0.1.

Rækkefølgen betyder noget for modeller med intern tilstand. Flere deltagere må ikke blandes i én sekvens uden særskilt håndtering af deltagerskift.

## 3. Kontrol af repoets struktur

```bash
python tools/fearprime_repo_audit.py . --strict
```

Kontrollen ændrer ikke filer. `--strict` giver fejlkode, hvis der findes egentlige fejl; uden flaget udskrives blot rapporten.

Den kontrollerer:

- om interne Markdown-links peger på eksisterende filer eller mapper,
- om `VERSION`, forsiden, emnekortet og seneste udgivelse i versionshistorikken stemmer overens,
- CSV-læsbarhed, entydige kolonnenavne, rækkeformater og tværreferencer mellem study-ID'er,
- om studiekortstier i data peger på eksisterende filer,
- YAML-syntaks via PyYAML,
- CPR-formater som advarsel til manuel kontrol,
- Markdown-filer uden indgående links som advarsler,
- gentagne PMID-/DOI-henvisninger, triageret mod duplicate-reference-registeret.

Gentagne henvisninger kan være aliaser, genanalyser eller bevidste krydsreferencer. De er ikke automatisk ekstra studier. Verificerede par ligger i [duplicate-reference-registeret](../data/duplicate_reference_registry.csv); andre gentagelser bliver stående som advarsler.

Kontrollen validerer **ikke** eksterne links, Markdown-ankre eller semantiske regler i YAML-skemaerne. CPR-mønstret er kun en målrettet privatdataindikator, ikke en fuld persondata-audit. Se [udgivelseschecklisten](../09_DEBUG/RELEASE_CHECKLIST.md).

## Test

```bash
python -m unittest discover -s tests -v
```

GitHub Actions kører test, en praktisk gennemkørsel af begge beregnere og streng strukturkontrol. Demodata er syntetiske og indgår ikke i evidensgrundlaget.

## Fortolkningsregel

En tilpasset parameter er ikke en neuronal biomarkør. En model, der beskriver adfærdsdata godt, er ikke dermed bevist som hjernens mekanisme. Se [modelsammenligningen](../05_MODELS/COMPUTATIONAL_MODEL_COMPARISON.md).
