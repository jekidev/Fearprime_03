# FearPrime — Predictive Processing / Bayesian / Active Inference Model

Version 0.29 · 2026-09-20

## Status

Dette er et **formelt arbejds- og hypoteselag** i FearPrime. Det kobler predictive processing, Bayesian belief updating, precision weighting, interoceptiv inference, active inference, ViolEx 2.0, inhibitory learning, safety behavior og generalisering.

Modellen er **ikke** en valideret samlet neurobiologisk teori om PTSD/CPTSD og er ikke en selvstændig behandlingsprotokol.

## 1. Minimal Bayesian kerne

~~~text
posterior ∝ likelihood × prior
P(H|D) ∝ P(D|H) × P(H)
~~~

Hvor H er en hypotese, D er nye data, prior er plausibiliteten før data, likelihood er hvor sandsynlige data er under hypotesen, og posterior er den opdaterede tro.

### FearPrime-eksempel

En tidligere trusselserfaring kan øge prioren for fare i beslægtede situationer. Ny sikkerhedsinformation ændrer kun modellen meget, hvis den faktisk observeres, vurderes som relevant og får tilstrækkelig vægt relativt til den eksisterende prior.

Dette er en beregningsmæssig fortolkning, ikke et direkte mål for neuronal Bayes-beregning.

## 2. Precision weighting

I predictive-processing-litteraturen betyder **precision** omtrent graden af sikkerhed/vægt, som systemet giver en informationskilde.

~~~text
belief update ≈ prediction error × precision-weight
~~~

Samme prediction error kan derfor føre til forskellig læring. FearPrime måler både størrelsen af expectation violation, hvor troværdig/relevant evidensen opleves, og ændringen i expectation bagefter.

En subjektiv confidence-score er **ikke** identisk med formel Bayesian precision.

## 3. ViolEx som belief-update layer

[ViolEx 2.0](VIOLEX_2_EXPECTATION_UPDATE_MODEL.md) kobles sådan:

~~~text
prior
→ prediction
→ observation
→ prediction error
→ precision/relevance-vurdering
→ accommodation ELLER immunization
→ posterior / bevaret prior
~~~

**Accommodation:** ny evidens får tilstrækkelig vægt til at ændre forventningen.

**Immunization:** ny evidens får lavere vægt eller omfortolkes, så den gamle forventning i høj grad bevares.

Det er en fortolkningsanalogi, ikke en påstand om, at ViolEx-processer allerede har en unik identificeret neuralligning.

## 4. Hierarkiske priors

FearPrime skelner mellem mindst tre niveauer:

1. **Konkret sensorisk prediction** — "denne lyd betyder X".
2. **Situationsmodel** — "denne type sted er farligt".
3. **Generaliseret model** — "verden/andre/min krop er generelt farlig eller upålidelig".

En sikker episode kan derfor opdatere niveau 1 uden at ændre niveau 3. Derfor måles både situationsspecifik expectancy, generaliseret expectancy og senere generalisering.

## 5. Interoceptiv inference

Kropslige signaler kan indgå som data:

~~~text
høj puls
→ observation
→ latent forklaring
→ "fare" / "anstrengelse" / "koffein" / "normal variation"
~~~

Forskningsspørgsmålet er ikke kun signalets størrelse, men hvilken årsag det tilskrives, hvor sikker fortolkningen er, og hvor meget den ændres af ny evidens.

Se [Insula / interoception](../02_MECHANISMS/INSULA_INTEROCEPTION.md).

## 6. Active inference

Active inference udvider modellen fra perception til **handling**:

~~~text
beliefs
→ forventede outcomes under mulige policies
→ policy selection
→ action
→ nye observationsdata
→ belief update
~~~

I active-inference-modeller beskrives policy selection ofte via forventet free energy. FearPrime bruger dette som et formelt sprog, ikke som dokumenteret klinisk mekanisme.

## 7. Pragmatic vs. epistemic value

En handling kan have:

- **pragmatic/extrinsic value** — søger et foretrukket udfald,
- **epistemic value** — søger information og reducerer relevant usikkerhed.

Kobling til ViolEx:

~~~text
assimilation / safety behavior
→ kan reducere ubehag eller risiko
→ men kan også reducere diagnostisk information

experimentation
→ søger observationer, der kan skelne mellem hypoteser
~~~

Safety behavior er ikke automatisk forkert. Ved reel fare kan beskyttelsesadfærd være rationel.

## 8. PTSD/CPTSD som arbejdshypotese

~~~text
traume / langvarig trussel
→ stærkere eller mere præcise threat priors
→ øget vægt på threat-congruent signaler
→ defensive policies
→ færre eller mindre diagnostiske disconfirming observations
→ immunization / lav accommodation
→ vedvarende threat posterior
~~~

Kæden kan brydes flere steder og er ikke bevist som én universel årsagsvej.

Kube et al. 2020 foreslog en predictive-processing model af PTSD; Putica & Agathos 2024 udvidede en beslægtet ramme til CPTSD og disturbances in self-organization.

## 9. FearPrime Exposure som Bayesian experiment

Definér før sessionen:

~~~text
H1 = threat-hypotese
H2 = alternativ/safety-hypotese
~~~

Registrér før: threat expectancy, prediction confidence, forventet outcome, observationer der ville støtte H1/H2 og planlagt safety behavior.

Registrér under: faktiske observationer, diagnostisk værdi, prediction error og action/policy.

Registrér efter: posterior threat expectancy, evidence credibility, accommodation, immunization subtype, generaliseret expectancy og næste prediction.

Se [ViolEx Exposure Measurement Sheet](../06_MEASUREMENT/VIOLEX_EXPOSURE_MEASUREMENT_SHEET.md).

## 10. Projektdeskriptive scores

~~~text
expectancy_update = post_expectancy - pre_expectancy
~~~

Eksplorativt:

~~~text
update_efficiency =
|expectancy_update| / max(|prediction_error|, epsilon)
~~~

Dette er **ikke** et neuralt mål og må ikke fortolkes som synaptisk learning rate, dopaminerg prediction error, Bayesian precision eller reconsolidation-index.

## 11. Computational model comparison

Når der findes nok trials, kan FearPrime teste:

1. Rescorla-Wagner / delta-rule.
2. Bayesian belief updating.
3. Hierarchical Gaussian Filter-lignende modeller.
4. Active-inference/POMDP-modeller.
5. Simpler heuristiske modeller.

**Regel:** En mere kompleks Bayesian/active-inference model skal forklare data bedre end enklere alternativer, ellers foretrækkes den enklere model.

## 12. Falsificerbare forudsigelser

Modellen svækkes, hvis fx:
- prior strength ikke forudsiger senere expectancy,
- evidence credibility/precision proxies ikke modererer learning,
- safety behavior ikke påvirker diagnostisk information,
- ViolEx accommodation ikke forudsiger senere belief change,
- en simpel delta-rule forklarer data lige så godt eller bedre,
- foreslåede computational parameters ikke replikerer.

## 13. Debug / begrænsninger

- Predictive processing er en teori-familie, ikke én verificeret mekanisme.
- Predictive coding og active inference er beslægtede, men ikke synonymer.
- "Bayesian brain" betyder ikke, at neuroner bogstaveligt udfører skolebogs-Bayes på en kendt måde.
- Precision bør ikke infereres direkte fra subjektiv confidence.
- Active inference kan fitte adfærdsdata, men teorien som helhed kræver stærkere model-comparison tests.
- PTSD/CPTSD er heterogene.
- Reel fare må ikke bortforklares som "forkert prior".

## 14. Kilder

- [Kube et al. 2020 — PTSD predictive processing](../07_STUDIES/THEORY/2020_Kube_PTSD_Predictive_Processing.md)
- [Putica & Agathos 2024 — CPTSD predictive processing](../07_STUDIES/THEORY/2024_Putica_Agathos_CPTSD_Predictive_Processing.md)
- [Hodson et al. 2024 — empirical status](../07_STUDIES/REVIEWS/2024_Hodson_Predictive_Coding_Active_Inference.md)
- [Panitz et al. 2021 — ViolEx 2.0](../07_STUDIES/THEORY/2021_Panitz_ViolEx_2_0.md)

## FearPrime-regel

**Prediction error er data. Learning afhænger af, hvordan data vægtes, fortolkes og generaliseres — og handling bestemmer delvist, hvilke data systemet får mulighed for at se.**
