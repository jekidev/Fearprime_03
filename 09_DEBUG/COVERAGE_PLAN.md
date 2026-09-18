# FearPrime — Coverage Plan

**Version 0.27 · 2026-09-18**

## Rolle

Denne fil svarer kun på:

> **Hvilke forskningsområder er dækket, delvist dækket eller åbne?**

Den er **ikke** changelog, search log eller v1-readiness audit.

- Versionshistorik: [CHANGELOG](../CHANGELOG.md)
- v1-readiness: [FEARPRIME_V1_GAP_AUDIT.md](FEARPRIME_V1_GAP_AUDIT.md)
- Historisk v0.26 coverage: [arkiv](ARCHIVE/COVERAGE_PLAN_v0.26_SNAPSHOT.md)

## Statussymboler

- ✅ dækket på framework-/dossierniveau
- 🟡 delvist dækket / kræver mere evidens
- 🔬 eksplorativ hypotese
- 🔴 åbent hul

## P0 — framework-kerne

| Domæne | Status | Kanonisk indgang |
|---|---|---|
| Funktionel/adaptiv PTSD-model | ✅ | [Adaptive PTSD Model](../05_MODELS/ADAPTIVE_PTSD_MODEL.md) |
| CPTSD-model | ✅ | [CPTSD Model](../05_MODELS/CPTSD_MODEL.md) |
| Extinction / inhibitory learning | ✅ | [Extinction Engine](../03_EXTINCTION/EXTINCTION_ENGINE.md) |
| Generalization / safety learning | ✅ | [Generalization Engine](../03_EXTINCTION/GENERALIZATION_AND_SAFETY_LEARNING_ENGINE.md) |
| Reconsolidation boundary conditions | ✅ | [Boundary Conditions](../03_EXTINCTION/RECONSOLIDATION_BOUNDARY_CONDITIONS.md) |
| Klinisk + learning measurement | ✅ | [Measurement Index](../06_MEASUREMENT/README.md) |
| Evidensregler | ✅ | [Evidence Rules](../01_EVIDENCE_RULES.md) |

## P1 — mekanismer

| Domæne | Status | Kanonisk indgang |
|---|---|---|
| Fear circuits | ✅ | [Master Map](../02_MECHANISMS/FEAR_CIRCUIT_MASTER_MAP.md) |
| Hippocampus / context | ✅ | [Context Discrimination](../02_MECHANISMS/HIPPOCAMPUS_CONTEXT_DISCRIMINATION.md) |
| Insula / interoception | ✅ | [Insula](../02_MECHANISMS/INSULA_INTEROCEPTION.md) |
| HPA / stress-memory | ✅ | [HPA](../02_MECHANISMS/HPA_STRESS_MEMORY.md) |
| NMDA / AMPA | ✅ | [NMDA/AMPA](../02_MECHANISMS/NMDA_AMPA_GLUTAMATE_PLASTICITY.md) |
| HDAC / BDNF / dopamine / 5-HT7 | ✅/🟡 | [Mechanism Module](../02_MECHANISMS/HDAC_BDNF_5HT7_DOPAMINE.md) |
| PNN / critical-period plasticity | ✅/🟡 | [PNN Module](../02_MECHANISMS/PNN_CRITICAL_PERIOD_REOPENING.md) |

## P1 — kandidater

| Kandidat | Status | Kanonisk dossier |
|---|---|---|
| Butyrat | ✅/🟡 | [Butyrate](../04_CANDIDATES/BUTYRATE_DOSSIER.md) |
| DCS | ✅ | [DCS](../04_CANDIDATES/DCS_DOSSIER.md) |
| FAAH / CB1 | ✅ | [FAAH/CB1](../04_CANDIDATES/ENDOCANNABINOID_FAAH_CB1_DOSSIER.md) |
| L-DOPA | ✅/🟡 | [L-DOPA](../04_CANDIDATES/LDOPA_DOSSIER.md) |
| Lurasidon | ✅/🟡 | [Lurasidone](../04_CANDIDATES/LURASIDONE_DOSSIER.md) |
| Oxytocin | ✅/🟡 | [Oxytocin](../04_CANDIDATES/OXYTOCIN_DOSSIER.md) |
| Propranolol | ✅ | [Propranolol](../04_CANDIDATES/PROPRANOLOL_DOSSIER.md) |
| HDAC2-selective tools | ✅/🟡 | [HDAC2 Dossier](../04_CANDIDATES/HDAC2_SELECTIVE_INHIBITOR_DOSSIER.md) |

Tværgående certainty ligger i [Candidate Certainty Profile](CANDIDATE_CERTAINTY_PROFILE.md).

## P1 — specialspor

| Domæne | Status | Indgang |
|---|---|---|
| TRE | ✅/🟡 | [TRE Dossier](../03_EXTINCTION/TRE_DOSSIER.md) |
| Sleep / nightmares | ✅/🟡 | [Nightmare/Sleep Dossier](../03_EXTINCTION/PTSD_NIGHTMARE_SLEEP_DOSSIER.md) |
| Interoceptive challenge | ✅/🟡 | [Interoception](../02_MECHANISMS/INSULA_INTEROCEPTION.md) |
| Nightmare + cannabinoid/butyrate | 🔬 | [Hypothesis](../05_MODELS/PTSD_NIGHTMARE_THC_BUTYRATE_HYPOTHESIS.md) |
| Butyrate × dopaminergic interoception design | 🔬 | [Preregistration](INTEROCEPTIVE_AUGMENTATION_PREREGISTRATION.md) |

## P2 — evidensarkitektur

| Lag | Status | Indgang |
|---|---|---|
| Risk of Bias | ✅/🟡 | [RoB Template](RISK_OF_BIAS_TEMPLATE.md) |
| Effect sizes / CI | ✅/🟡 | [Extraction Standard](EFFECT_SIZE_EXTRACTION_STANDARD.md) |
| Participant overlap | ✅/🟡 | [Overlap Register](PARTICIPANT_OVERLAP_REGISTER.md) |
| Reproducible search | ✅/🟡 | [Search Protocol](SYSTEMATIC_SEARCH_PROTOCOL.md) |
| Claim-level certainty | ✅/🟡 | [Certainty Framework](CERTAINTY_FRAMEWORK.md) |
| Machine-readable evidence | ✅/🟡 | [data/README](../data/README.md) |
| Native PubMed / PRISMA-complete export | 🟡 | [Reconsolidation Export Status](PUBMED_RECONSOLIDATION_EXPORT_2026-09-18.md) |

## Næste coverage-opgaver

1. Udvid study-level RoB/effect-size/CI til flere centrale humane studier.
2. Udvid reproducerbare searches ud over reconsolidation.
3. Valider Nightmare Measurement Engine mod etablerede instrumenter.
4. Færdiggør power/precision-plan for interoceptive factorial research design.
5. Afklar publication bias og reviewer-status før nogen claim kan løftes til HIGH certainty.

## Regel

Når et område bliver “dækket”, betyder det kun, at FearPrime har en struktureret fil/ramme og et identificeret evidensgrundlag. Det betyder **ikke**, at hypotesen eller interventionen er bevist.
