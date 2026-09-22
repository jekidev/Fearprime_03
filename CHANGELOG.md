# FearPrime changelog

Fra v0.27 ligger aktiv versionshistorik her. Ældre v0.6–v0.26-historik er bevaret i [README v0.26 snapshot](09_DEBUG/ARCHIVE/README_v0.26_SNAPSHOT.md).

## Unreleased — 2026-09-22

- Tilføjet `08_RESOURCES/SPOTIFY.md` som separat lag for personligt betydningsfuld musik.
- Første Spotify-spor er registreret som personlig ressource.
- Spotify-laget er eksplicit markeret som **ikke evidens**, ikke intervention og ikke behandlingsanbefaling.
- Ressourceindeks og repo-map er opdateret, så personlige musikressourcer ikke blandes med studier eller mekanistiske påstande.
- Tilføjet dependency-free `tools/fearprime_repo_audit.py` til repo-wide QA.
- Audit-v0.1 kontrollerer interne Markdown-links, release-versioner og CSV-integritet samt rapporterer orphan-filer og mulige PMID/DOI-duplikater til manuel triage.
- Tilføjet `tests/test_repo_audit.py` og GitHub Actions QA-rapport.
- v1.0 Gap Audit er opdateret, så resterende QA-blockers er eksplicitte i stedet for at blive markeret som løst.

## v0.30 — 2026-09-20 — Bayesian Calculator + computational model comparison

- Tilføjet dependency-free `tools/fearprime_bayesian_calculator.py` v0.1.
- Calculatoren udleder prediction error, expectancy update, update efficiency, descriptive accommodation/immunization, retention og generalization fra ViolEx CSV.
- Tilføjet `tools/fearprime_model_compare.py` v0.1.
- Samme target (`post_threat_expectancy`) sammenlignes mellem no-update baseline, Rescorla–Wagner, soft-evidence Bayesian, HGF-like adaptive volatility og active-inference-inspired precision/policy.
- Model comparison rapporterer SSE, MAE, RMSE, Gaussian NLL, AIC, BIC og ΔBIC.
- HGF-like og active-inference-inspired modeller er eksplicit markeret som approximationsmodeller, ikke canonical HGF/POMDP/FEP.
- Tilføjet [Computational Model Comparison](05_MODELS/COMPUTATIONAL_MODEL_COMPARISON.md).
- Tilføjet syntetisk `data/computational_demo.csv` til reproducerbar smoke testing.
- Tilføjet unit tests i `tests/test_fearprime_tools.py`.
- Tilføjet GitHub Actions CI på Python 3.11 og 3.12.
- Stateful model-rækkefølge og risikoen ved blandede participant-sekvenser er dokumenteret.
- Version bump til v0.30.

## v0.29 — 2026-09-20 — ViolEx measurement + predictive processing/active inference

- Tilføjet [ViolEx Exposure Measurement Sheet](06_MEASUREMENT/VIOLEX_EXPOSURE_MEASUREMENT_SHEET.md).
- Tilføjet maskinlæsbar `violex_exposure_template.csv` og `violex_exposure_schema.yaml`.
- Tilføjet [Predictive Processing / Bayesian / Active Inference Model](05_MODELS/PREDICTIVE_PROCESSING_ACTIVE_INFERENCE_MODEL.md).
- Modellen kobler priors, likelihood, precision weighting, hierarchical beliefs, interoception og action/policy selection til ViolEx.
- Tilføjet model-comparison regel.
- Tilføjet Kube et al. 2020 og Hodson et al. 2024 kildekort.

## v0.28 — 2026-09-20 — ViolEx 2.0 integration

- Tilføjet [ViolEx 2.0 expectation-update model](05_MODELS/VIOLEX_2_EXPECTATION_UPDATE_MODEL.md).
- Integreret accommodation, immunization, assimilation og experimentation.
- Tilføjet Panitz et al. 2021 teorikort.

## v0.27 — 2026-09-18 — struktur-cleanup

- Scannet hele repoet: 252 filer / 20 mapper.
- Ingen forskningsfiler eller evidens er slettet.
- README, Study Ledger og Source Register blev ryddet og historik arkiveret.
- `REPO_MAP.md` definerer ansvar pr. filtype.

## v0.26 og tidligere

Se de bevarede snapshots:
- [README v0.26](09_DEBUG/ARCHIVE/README_v0.26_SNAPSHOT.md)
- [Study Ledger v0.26](09_DEBUG/ARCHIVE/STUDY_LEDGER_v0.26_SNAPSHOT.md)
- [Source Register v0.26](09_DEBUG/ARCHIVE/SOURCE_REGISTER_v0.26_SNAPSHOT.md)
