# FearPrime changelog

Fra v0.27 ligger aktiv versionshistorik her. Ældre v0.6–v0.26-historik er bevaret i [README v0.26 snapshot](09_DEBUG/ARCHIVE/README_v0.26_SNAPSHOT.md).

## v0.29 — 2026-09-20 — ViolEx measurement + predictive processing/active inference

- Tilføjet [ViolEx Exposure Measurement Sheet](06_MEASUREMENT/VIOLEX_EXPOSURE_MEASUREMENT_SHEET.md).
- Tilføjet maskinlæsbar \`violex_exposure_template.csv\` og \`violex_exposure_schema.yaml\`.
- Tilføjet [Predictive Processing / Bayesian / Active Inference Model](05_MODELS/PREDICTIVE_PROCESSING_ACTIVE_INFERENCE_MODEL.md).
- Modellen kobler priors, likelihood, precision weighting, hierarchical beliefs, interoception og action/policy selection til ViolEx og FearPrime exposure.
- Tilføjet eksplicit model-comparison regel: Bayesian/active-inference modeller skal tilføre forklaringsværdi over enklere alternativer.
- Tilføjet teorikort for Kube et al. 2020 om PTSD predictive processing.
- Tilføjet reviewkort for Hodson et al. 2024 om den empiriske status for predictive coding og active inference.
- Den adaptive PTSD-model linker nu til det formelle computational layer.
- Putica & Agathos 2024 er koblet til det nye model-lag.
- Kube 2020 og Hodson 2024 er tilføjet til \`data/studies.csv\`.
- Version bump til v0.29.

## v0.28 — 2026-09-20 — ViolEx 2.0 integration

- Tilføjet [ViolEx 2.0 expectation-update model](05_MODELS/VIOLEX_2_EXPECTATION_UPDATE_MODEL.md) som valgfrit fortolkningslag.
- Integreret accommodation, data-/concept-oriented immunization, assimilation og experimentation med FearPrimes eksisterende exposure/extinction-flow.
- Tilføjet eksplicit skelnen mellem expectation violation/prediction error og faktisk expectation update.
- Den foreslåede omvendte U-relation mellem violation magnitude og accommodation er markeret som hypotese/boundary-condition, ikke som universel lov.
- Tilføjet teorikort for Panitz et al. 2021 med DOI, PMID og PMCID.
- Extinction Engine linker nu til ViolEx-laget.
- Panitz et al. 2021 er tilføjet til det maskinlæsbare study-register som teori.

## v0.27 — 2026-09-18 — struktur-cleanup

- Scannet hele repoet: 252 filer / 20 mapper.
- Ingen forskningsfiler eller evidens er slettet.
- Den gamle README, Study Ledger og Source Register er bevaret ordret som v0.26-snapshots.
- README er reduceret til navigation, kerneprincipper og aktuel status.
- \`REPO_MAP.md\` definerer ét ansvar pr. filtype.
- Studie- og debug-lag får egne indeksfiler.
- Legacy/kompakte modeller markeres som sådanne frem for at fremstå som parallelle masterfiler.
- Berceli 2014-dobbeltkort markeres som samme studie / alias.
- Coverage Plan og Gap Audit får eksplicit forskellige roller.
- Fremtidig versionshistorik skal ind i dette changelog, ikke spredes i README/Study Ledger/Source Register.

## v0.26 og tidligere

Se de bevarede snapshots:
- [README v0.26](09_DEBUG/ARCHIVE/README_v0.26_SNAPSHOT.md)
- [Study Ledger v0.26](09_DEBUG/ARCHIVE/STUDY_LEDGER_v0.26_SNAPSHOT.md)
- [Source Register v0.26](09_DEBUG/ARCHIVE/SOURCE_REGISTER_v0.26_SNAPSHOT.md)
