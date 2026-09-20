# FearPrime — Computational Model Comparison

Version 0.30 · 2026-09-20

## Formål

Dette lag operationaliserer den tidligere regel:

> En kompleks predictive-processing / active-inference forklaring skal sammenlignes med enklere alternativer.

Værktøjet ligger i [`tools/fearprime_model_compare.py`](../tools/fearprime_model_compare.py).

## Fælles target

Alle belief-update modeller evalueres på:

```text
post_threat_expectancy
```

ud fra pre-expectancy, observeret outcome og eventuelle evidens-/safety-behavior felter.

Det gør AIC/BIC/RMSE-sammenligningen mere meningsfuld, fordi modellerne forsøger at forklare samme output.

## Model 0 — no-update baseline

```text
prediction_post = pre_expectancy
```

Hvis en kompleks model ikke slår denne, er der meget lidt grundlag for at hævde læringsmodellering.

## Model 1 — Rescorla–Wagner / delta rule

```text
post_hat = pre + alpha × (observed - pre)
```

Én parameter: `alpha`.

Denne model er vigtig, fordi en simpel læringsrate ofte kan forklare meget uden hierarkisk Bayes eller active inference.

## Model 2 — soft-evidence Bayesian update

FearPrime bruger en enkel Beta-lignende soft-count update:

```text
posterior =
(prior × kappa + observation × evidence_weight)
/
(kappa + evidence_weight)
```

`kappa` fungerer som prior concentration.

`evidence_weight` afledes af evidence credibility og relevance.

Dette er en **forenklet computational comparator**, ikke en fuld generativ PTSD-model.

## Model 3 — HGF-like adaptive volatility

Den nuværende v0.1 er **ikke canonical Hierarchical Gaussian Filter**.

Den bruger tidligere squared prediction errors til en løbende volatility proxy, som kan ændre læringsraten:

```text
volatility_t = decay × volatility_(t-1)
             + (1-decay) × PE_(t-1)^2

alpha_t = logistic(logit(base_alpha)
                   + volatility_gain × sqrt(volatility_t))
```

Formålet er at teste, om en enkel volatility-sensitive model forklarer mere end konstant alpha.

Hvis sporet bliver lovende, bør næste version implementere en verificeret HGF-formulering fra en etableret reference/softwarepakke frem for at kalde denne approximation "HGF".

## Model 4 — active-inference-inspired precision/policy

Denne model er ligeledes **ikke canonical active inference eller POMDP/FEP**.

Den lader evidence credibility/relevance øge effektiv learning rate og safety behavior reducere epistemisk vægt:

```text
alpha_t =
logistic(
  logit(base_alpha)
  + evidence_gain × evidence
  - safety_gain × safety_behavior
)
```

Derefter:

```text
post_hat = pre + alpha_t × prediction_error
```

Det er en testbar approximation af FearPrime-idéen om, at handling/policy kan ændre, hvor diagnostisk ny information bliver.

## Model selection

V0.1 rapporterer:

- SSE,
- MAE,
- RMSE,
- Gaussian negative log-likelihood,
- AIC,
- BIC,
- ΔBIC.

BIC bruges som standard sortering, fordi den straffer ekstra parametre. Men et lavere BIC er **ikke** bevis for en neurobiologisk teori.

## Minimum data

Scriptet kræver mindst 3 komplette rækker, men 3 rækker er kun teknisk minimum.

For 3-parameter modeller er små datasæt ekstremt ustabile. Reelle model-comparison claims kræver væsentligt flere trials/sessions, preregistrerede analyser og helst out-of-sample validation.

## Næste metodiske niveauer

1. Participant-ID og hierarkiske modeller.
2. Train/test eller leave-one-session-out validation.
3. Parameter recovery på simulerede data.
4. Model recovery / confusion matrix.
5. Canonical HGF-implementation.
6. Proper generative active-inference/POMDP model med hidden states, observations, policies og preferences.
7. Posterior predictive checks.
8. Comparison mod model-free reinforcement learning og simple heuristikker.

## Falsifikation

Predictive-processing-sporet får mindre støtte, hvis:

- simple delta-rule modeller er lige så gode eller bedre,
- evidence/safety-behavior parametre ikke replikerer,
- HGF-like volatility ikke forbedrer out-of-sample prediction,
- parameter recovery er dårlig,
- modeller ikke kan identificeres fra hinanden på simulerede data.

## Sikker fortolkning

Disse scripts modellerer **observerede ratings**. De må ikke automatisk oversættes til:

- dopamin,
- synaptisk plasticitet,
- neuronal precision,
- amygdala prediction error,
- memory reconsolidation,
- klinisk recovery.

Se også [Predictive Processing / Bayesian / Active Inference Model](PREDICTIVE_PROCESSING_ACTIVE_INFERENCE_MODEL.md).
