# FearPrime — emnekort

Version 0.31 · 2026-09-22

[Start her](START_HER.md) giver den korte indgang. [Dokumentindekset](DOKUMENTINDEKS.md) linker til samtlige Markdown-dokumenter, inklusive historik og specialkort.

## Hver dokumenttype har en opgave

| Spørgsmål | Hovedindgang | Fordybelse |
|---|---|---|
| Hvad er projektets formål? | [Manifest](00_MANIFESTO.md) | [Grundmodel](00_MANIFESTO/FEARPRIME_MODEL.md), [adaptiv model](05_MODELS/ADAPTIVE_PTSD_MODEL.md) |
| Hvordan hænger biokemien sammen? | [Fra signal til hukommelse](02_MECHANISMS/BIOKEMI_FRA_SIGNAL_TIL_HUKOMMELSE.md) | [Receptorer](02_MECHANISMS/RECEPTORER_OG_SIGNALVEJE.md), [kredsløb](02_MECHANISMS/FEAR_CIRCUIT_MASTER_MAP.md) |
| Hvordan ændres læring? | [Læringsmodul](03_EXTINCTION/EXTINCTION_ENGINE.md) | [Generalisering](03_EXTINCTION/GENERALIZATION_AND_SAFETY_LEARNING_ENGINE.md), [rekonsolidering](03_EXTINCTION/RECONSOLIDATION_BOUNDARY_CONDITIONS.md) |
| Hvad viser et præparats evidens? | [Kandidater](04_CANDIDATES/README.md) | Hoveddossier → specialmodul → studiekort |
| Hvordan forstås forventninger? | [ViolEx](05_MODELS/VIOLEX_2_EXPECTATION_UPDATE_MODEL.md) | [Forudsigelsesmodeller](05_MODELS/PREDICTIVE_PROCESSING_ACTIVE_INFERENCE_MODEL.md) |
| Hvad skal måles? | [Måleplan](06_MEASUREMENT/MEASUREMENT_PLAN.md) | [Sessionsark](06_MEASUREMENT/SESSION_TEMPLATE.md), CPTSD, mareridt og læring |
| Hvor er kilderne? | [Studieregister](07_STUDIES/STUDY_LEDGER.md) | [Kilderegister](07_STUDIES/SOURCE_REGISTER.md), individuelle kort |
| Hvad kan beregnes? | [Værktøjer](tools/README.md) | [Modelsammenligning](05_MODELS/COMPUTATIONAL_MODEL_COMPARISON.md), [data](data/README.md) |
| Hvor sikkert er et udsagn? | [Evidensregler](01_EVIDENCE_RULES.md) | [Vurderingsramme](09_DEBUG/CERTAINTY_FRAMEWORK.md), fejlkilder og usikkerhed |
| Hvad mangler? | [Dækningsplan](09_DEBUG/COVERAGE_PLAN.md) | [Mangelliste frem mod v1.0](09_DEBUG/FEARPRIME_V1_GAP_AUDIT.md) |
| Hvilke ressourcer findes? | [Ressourcer](08_RESOURCES/README.md) | Bøger, videoer, podcasts og [personlig musik](08_RESOURCES/MUSIK.md) |

## Sammenhæng uden dobbeltarbejde

Et **studiekort** beskriver en kilde. Et **dossier** samler evidensen om en kandidat. Et **mekanismemodul** forklarer biologiske forbindelser. En **model** opstiller spørgsmål og forudsigelser. En **måleskabelon** operationaliserer observationer. Et **metodedokument** beskriver kontrollen af konklusionerne.

Krydslinks forbinder lagene. Gentagen omtale af et studie er ikke en uafhængig replikation.

## Studier og data

Studiebiblioteket skelner mellem humane studier, dyreforsøg, mekanismer, oversigtsartikler, teori, kvalitativ forskning og protokoller. Mappenavnet `VERIFIED` er ikke i sig selv en kvalitetsgrad eller en garanti for fuldtekstkontrol; læs kortets kontrolniveau.

Markdown forklarer evidensen. CSV/YAML-filer gør udvalgte felter analyserbare. Dataregistret er endnu ikke et komplet spejl af alle studiekort. Syntetiske demodata er kun til afprøvning af beregninger.

## Beregninger

ViolEx-data kan føres til læringsberegneren eller bruges til sammenligning af modeller, som forudsiger samme mål: `post_threat_expectancy`. Se [værktøjsvejledningen](tools/README.md) for kommandoer og begrænsninger. Modeller med hukommelse om tidligere rækker afhænger af rækkefølgen; flere deltagere må ikke blandes i én sekvens.

## Bevarede oversigter og historik

- [Kompakt udslukningsmodel](models/FEAR_EXTINCTION_MODEL.md): ældre oversigt.
- [Kompakt mekanismekort](02_MECHANISMS/MECHANISM_MAP.md): ældre oversigt.
- [Berceli-kort](07_STUDIES/VERIFIED/2014_Berceli_TRE_Caregivers.md): samme studie som [pilotkortet](07_STUDIES/VERIFIED/2014_Berceli_TRE_Caregivers_Pilot.md).
- [Arkiv](09_DEBUG/ARCHIVE/README.md): historiske versioner; de aktuelle hovedindgange ovenfor bruges til projektstatus.
