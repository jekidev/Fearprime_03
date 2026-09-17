# FearPrime — insula og interoception

Version 0.20 · 2026-09-17

## Formål
Dette modul beskriver insula og interoception som et forbindelsesled mellem kropslige signaler, salience, prediction, emotionel betydning og handling. FearPrime antager ikke, at høj insulaaktivitet er en specifik PTSD-biomarkør eller at interoceptive signaler i sig selv er patologiske.

Se også:
- [Adaptiv PTSD-model](../05_MODELS/ADAPTIVE_PTSD_MODEL.md)
- [Fear Circuit Master Map](FEAR_CIRCUIT_MASTER_MAP.md)
- [Generalization & Safety Learning Engine](../03_EXTINCTION/GENERALIZATION_AND_SAFETY_LEARNING_ENGINE.md)
- [Learning Metrics](../06_MEASUREMENT/LEARNING_METRICS.md)

---

## 1. Arbejdsmodel

```text
kropsligt signal
   ↓
registrering
   ↓
insula + salience-netværk
   ↓
fortolkning / prediction
   ↓
"fare", "uklarhed" eller "sikker variation"
   ↓
attention + autonom respons + handling
   ↓
ny feedback
```

FearPrime skelner derfor mellem:
1. selve kropssignalet,
2. opmærksomhed på signalet,
3. præcision i perceptionen,
4. fortolkningen,
5. forventningen om konsekvens,
6. den handling signalet udløser.

## 2. Hvorfor interoception er relevant ved PTSD
Joshi, Aupperle & Khalsa (2023) gennemgår interoception i fear learning og PTSD. De fremhæver bl.a., at kropssignaler kan fungere som en del af traumets unconditioned response, senere blive conditioned cues, indgå i higher-order conditioning og påvirke konteksten for acquisition, consolidation og extinction.

- PMID `37404967`
- DOI `10.1176/appi.focus.20230007`

Det passer direkte med FearPrimes adaptive model: et kropssignal kan være korrekt registreret, mens betydningen af signalet generaliseres for bredt.

## 3. Insula er ikke én funktion
Anterior, mid og posterior insula bør ikke behandles som ét homogent område. De indgår forskelligt i integration af kropslige signaler, salience, emotionel betydning, sensoriske repræsentationer og netværksskift.

Nicholson et al. (2016) fandt ændrede forbindelser mellem insula-subregioner og basolateral amygdala ved PTSD og den dissociative subtype. Resultaterne illustrerer, at samme diagnostiske familie kan vise forskellige netværksmønstre.

- PMID `27042977`
- DOI `10.1016/j.pscychresns.2016.02.002`

## 4. Threat processing, generalisering og kontrol
Et fMRI-studie af fear generalization hos veteraner fandt et bias mod generaliserede fear associations ved PTSD med bl.a. ændret insularespons sammen med visuelle, thalamiske og locus-coeruleus-relaterede områder.

- PMID `26670285`

Ved emotionel attentional control er PTSD også blevet forbundet med relativt større insulaaktivitet og svagere rekruttering af dele af kontrolnetværket. Det støtter en salience/control-fortolkning, men er ikke direkte bevis for interoceptiv prediction error.

- PMID `31078834`

## 5. Behandlingsrelaterede signaler
Ved prolonged exposure hos veteraner var remission associeret med ændring i anterior-insula-aktivitet og connectivity i et affektivt anticipation-paradigme. Dette er et behandlingskorrelat, ikke bevis for at ændring i insula var den kausale mekanisme bag remission.

- PMID `24061484`

Andre studier har vist ændret anterior-insula directed connectivity efter trauma-memory-reactivation treatment og ændret insula-netværksconnectivity i behandlingsstudier. FearPrime registrerer disse som netværksmarkører, ikke som validerede behandlingsmål.

- PMID `35189456`
- PMID `32668087`

## 6. Interoceptiv generalisering
FearPrime tester følgende kæde:

```text
intern sensation
→ tidligere farebetydning
→ ny kontekst
→ forventning om skade
→ avoidance / scanning / kontrol
→ begrænset mulighed for korrigerende læring
```

Eksempel: høj puls kan være fysiologisk korrekt registreret, men dens betydning kan generaliseres fra “under denne hændelse var høj puls forbundet med fare” til “høj puls betyder fare i alle sammenhænge”.

## 7. Måling
Hold mindst følgende adskilt:
- interoceptive accuracy/performance,
- interoceptive sensibility/self-report,
- confidence/metacognition,
- symptomfortolkning,
- threat expectancy,
- autonom fysiologi,
- adfærd/avoidance,
- neural respons/connectivity.

Puls, HRV, respiration eller SCR er ikke direkte mål for “insula-funktion”.

## 8. Dissociation
Interoceptive over- og underrespons kan begge forekomme. Dissociation må derfor ikke defineres som blot “lav arousal”. Det dissociative PTSD-spor har egne netværksmønstre og skal analyseres separat fra klassisk hyperarousal.

## 9. Falsificerbare predictions
Modellen svækkes hvis:
- ændringer i kropsfortolkning ikke påvirker expectancy, avoidance eller funktion,
- insula/netværksmål ikke tilfører noget ud over generel negativ affekt,
- interoceptiv generalisering ikke kan adskilles fra generel sensitization,
- samme mønster forklares bedre af opmærksomhed eller respiratoriske/kardiovaskulære forskelle alene.

## 10. Debug
- Insulaaktivitet er ikke lig med “angstcenter”.
- BOLD-aktivitet viser ikke i sig selv excitatorisk/inhibitorisk neuronal retning.
- Interoception er ikke kun hjerteslag; respiration, visceral signalering, temperatur, smerte og andre kropslige signaler kan være relevante.
- Sammenhænge mellem insula og PTSD er heterogene og afhænger af opgave, subtype og kontrolgruppe.

## FearPrime-konklusion
Insula/interoception bør modelleres som et **body-to-threat-meaning interface**. Målet er ikke at dæmpe alle kropssignaler, men at forbedre kalibreringen mellem faktisk fysiologi, dens fortolkning, kontekst og efterfølgende handling.