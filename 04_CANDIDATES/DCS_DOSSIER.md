# FearPrime — D-cycloserin (DCS)-dossier

Version 0.21 · 2026-09-17

## Formål
Dette dossier samler FearPrimes humane evidens for **D-cycloserin (DCS)** som NMDA-relateret augmentation af exposure/extinction learning, med særskilt fokus på PTSD.

DCS er et nyttigt translationalt eksempel, fordi mekanismen er plausibel, men den kliniske effekt er **lille, heterogen og stærkt afhængig af læringskontekst**.

Se også:
- [NMDA/AMPA/glutamaterg plasticitet](../02_MECHANISMS/NMDA_AMPA_GLUTAMATE_PLASTICITY.md)
- [Learning metrics](../06_MEASUREMENT/LEARNING_METRICS.md)
- [Risk-of-bias template](../09_DEBUG/RISK_OF_BIAS_TEMPLATE.md)
- [Mataix-Cols 2017 IPD-meta](../07_STUDIES/VERIFIED/2017_MataixCols_DCS_IPD_meta.md)

---

## 1. Farmakologisk idé
DCS er en partiel agonist ved glycin-site på NMDA-receptoren. Arbejdshypotesen er ikke akut anxiolyse, men augmentation af den plasticitet, der stabiliserer ny læring omkring exposure/extinction.

FearPrime-regel:

```text
DCS forstærker ikke nødvendigvis "sikkerhed".
DCS kan potentielt forstærke den læring, der faktisk sker i sessionen.
```

Hvis sessionen ender med stærk threat expectancy eller mislykket exposure, kan et generelt plasticitetsfremmende stof derfor teoretisk være neutralt eller ufordelagtigt.

## 2. Tidlige meta-analyser
En tidlig meta-analyse rapporterede augmentation af fear extinction/exposure og foreslog størst nytte ved begrænset antal administrationer tæt på extinction/exposure.

PMID `18313643`.

En senere human meta-analyse fra 2014 fandt en lille samlet fordel af DCS-augmented exposure på tværs af anxiety disorders, Cohen d omkring `-0.34` (95% CI `-0.54 til -0.14`).

PMID `24991926`.

Dette er ikke et rent PTSD-estimat.

## 3. PTSD: de Kleine 2012
67 personer med primær PTSD blev randomiseret dobbeltblindet til 50 mg DCS eller placebo før exposure-sessioner.

DCS forbedrede ikke den samlede treatment effect i primary overall analysis, men exploratory analyser antydede større fordel hos deltagere med sværere baseline-PTSD og længere behandlingsbehov.

PMID `22480663` · DOI `10.1016/j.biopsych.2012.02.033`.

**FearPrime:** R2; overordnet nul/mixed med eksplorative moderator-signaler.

## 4. PTSD: Litz 2012
I combat-related PTSD gav exposure + DCS **mindre symptomreduktion** end exposure + placebo i dette randomiserede dobbeltblinde forsøg.

PMID `22694905` · DOI `10.1016/j.jpsychires.2012.05.006`.

Dette er vigtigt, fordi det viser, at en putativ learning enhancer ikke automatisk forbedrer outcome.

**FearPrime:** R2 negativt/modsat fund.

## 5. PTSD: Difede et al. pilot
25 patienter med kronisk PTSD fik virtual-reality exposure med DCS eller placebo.

Rapporterede mellemgruppe-effektstørrelser:
- post-treatment `d = 0.68`
- 6 måneder `d = 1.13`

Remission:
- post-treatment: `46%` vs `8%`
- 6 måneder: `69%` vs `17%`

PMID `24217129` · DOI `10.1038/npp.2013.317`.

### Begrænsning
Meget lille pilot (13 vs 12); store estimates kan være ustabile og kræver større replikation.

**FearPrime:** R1–R2 positivt signal.

## 6. PTSD: Rothbaum et al. 2014
156 Iraq/Afghanistan-veteraner blev randomiseret til virtual-reality exposure augmented med DCS, alprazolam eller placebo.

- PTSD-symptomer faldt i alle grupper.
- DCS havde ingen samlet symptomfordel over placebo.
- secondary analysis viste, at between-session extinction learning var treatment-specific enhancer i DCS-gruppen.
- alprazolam-gruppen havde dårligere enkelte outcomes end placebo.

PMID `24743802` · DOI `10.1176/appi.ajp.2014.13121625`.

**FearPrime:** R2; vigtig støtte til "session-quality / learning-state moderation" frem for simpel main effect.

## 7. 2017 individual-participant-data meta-analyse
21 af 22 eligible trials, 1047 deltagere på tværs af anxiety/OCD/PTSD, blev analyseret.

DCS gav en lille ekstra forbedring ved post-treatment:
- mean difference `-3.62`
- 95% CI `-6.43 til -0.81`
- `d = -0.25`

Follow-up-effekten var mindre og grænsenære (`d ≈ -0.19`).

PMID `28122091`.

### Fortolkning
Det understøtter en **lille** gennemsnitlig augmentationseffekt på tværs af diagnoser, ikke en stor eller PTSD-specifik effekt.

**Robusthed:** R3 for en lille transdiagnostisk gennemsnitseffekt.

## 8. PTSD-review 2018
Et review af syv PTSD-studier konkluderede, at evidensen ikke tilstrækkeligt understøttede DCS som generisk add-on: exposure-studier omfattede positive, negative og inkonklusive resultater.

PMID `29955504`.

## 9. Multisite PTSD RCT 2022
192 militære deltagere med PTSD blev randomiseret i et multisite dobbeltblindet forsøg med virtual reality exposure eller prolonged imaginal exposure og DCS eller placebo.

DCS gav ingen samlet augmentationseffekt:
- augmentation main effect `p = .774`
- augmentation × time `p = .422`
- symptomforbedring: DCS `18.88` CAPS-point, placebo `22.14`
- model-estimeret post-treatment forskel `3.80` point (95% CI `0.03–7.57`) i retning af bedre placebo-resultat i den rapporterede parameterisering.

Hos deltagere med baseline depression viste moderatoranalysen større forbedring med placebo; ikke-deprimerede havde praktisk talt ingen forskel.

PMID `35896533` · DOI `10.1038/s41398-022-02066-x`.

**FearPrime:** R3 negativt samlet main-effect fund.

## 10. Hvorfor kan DCS-resultater variere?
Mulige moderatorer:

1. kvaliteten af exposure-sessionen,
2. tidspunkt for administration,
3. antal doser/sessioner,
4. baseline symptomsværhedsgrad,
5. comorbid depression,
6. type exposure (VR vs imaginal/in vivo),
7. outcome-timepoint,
8. samtidig medicin og forventninger,
9. hvor stærkt sessionen faktisk skaber expectancy violation/safety learning.

## 11. Session-quality modellen
FearPrime bruger DCS som prototype for denne model:

```text
høj kvalitet af ny læring
        +
plasticitetsaugmentation
        ↓
kan give bedre consolidation/recall

svag/ambivalent eller threat-forstærkende session
        +
plasticitetsaugmentation
        ↓
neutral eller potentielt dårligere effekt
```

Dette er en plausibel forklaringsmodel; ikke alle kliniske moderatorfund er preregistrerede eller replikerede.

## 12. Målekrav
DCS-studier bør mindst registrere:

```yaml
pre_session_expectancy: null
end_session_expectancy: null
prediction_error: null
within_session_extinction: null
between_session_change: null
delayed_recall: null
return_of_fear: null
clinical_symptoms: null
function: null
```

## 13. RoB-fokus
- små samples i flere tidlige positive trials,
- multiple moderator/subgroup analyses,
- timing og exposure-protokoller varierer,
- diagnosesammensætning varierer i meta-analyser,
- publication/small-study bias kan påvirke tidlige estimates,
- main effects skal vægtes højere end uforudsete subgrupper uden replication.

## 14. Samlet evidensstatus
| Påstand | Status |
|---|---|
| NMDA-modulation er relevant for extinction plasticitet | ✅ |
| DCS kan give lille gennemsnitlig exposure-augmentation på tværs af diagnoser | ✅/🟡 R3 |
| DCS giver konsistent klinisk PTSD-fordel | 🔴/🟡 konflikt |
| Session quality kan moderere DCS-effekt | 🟡 plausibel + enkelte humane signaler |
| DCS er en generel anxiolytisk behandling | ❌ ikke modellens mekanisme |

## 15. Debug
DCS-sporet er et eksempel på FearPrimes hovedregel: stærk mekanistisk plausibilitet og positive tidlige trials er ikke nok. Større PTSD-studier viser ingen stabil main effect, og klinisk nytte ser ud til at afhænge af læringens kvalitet, population og timing.
