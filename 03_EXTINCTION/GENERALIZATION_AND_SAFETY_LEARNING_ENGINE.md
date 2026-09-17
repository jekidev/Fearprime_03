# FearPrime — Generalization & Safety Learning Engine

Version 0.18 · 2026-09-17

## Formål
Dette modul gør **fear generalization, threat/safety discrimination og safety learning** til selvstændige FearPrime-processer.

FearPrime antager ikke, at problemet nødvendigvis er “for meget frygt”. Et centralt problem kan være, at et system anvender en korrekt tidligere faresignalregel for bredt:

```text
oprindelig fare
      ↓
læring af cues og kontekst
      ↓
ny cue ligner gammel fare
      ↓
respons generaliseres
      ↓
for få sikre mod-eksempler får fuld vægt
```

Målet er derfor bedre **kalibrering og diskrimination**, ikke blind reduktion af defensive responser.

## Grundbegreber

### CS+ og CS−
- **CS+**: stimulus der har været forbundet med aversivt udfald.
- **CS−**: stimulus der signalerer fravær af det aversive udfald i et conditioning-paradigme.

I virkeligheden er mennesker sjældent omgivet af perfekte laboratorie-CS'er. FearPrime bruger derfor begreberne som modeller for threat/safety learning — ikke som påstand om at komplekse traumer kan reduceres til én tone og ét chok.

### Generalization stimulus (GS)
En ny stimulus der deler egenskaber med den oprindeligt lærte stimulus.

### Generaliseringsgradient
Sammenhængen mellem hvor meget en ny stimulus ligner det lærte faresignal og hvor stærk threat response/forventning den udløser.

En bred gradient kan betyde, at mange relativt forskellige stimuli behandles som mulige trusler.

## Fire former for generalisering

### 1. Perceptuel generalisering
Lighed i lyd, ansigt, sted, lugt, bevægelse osv.

### 2. Kontekstuel generalisering
En sikker situation behandles som farlig, fordi den deler sted-, tids- eller miljøelementer med tidligere fare.

### 3. Semantisk/kategoriel generalisering
En regel overføres konceptuelt:

```text
én person → en gruppe → "mennesker er farlige"
```

### 4. Interoceptiv generalisering
Et kropssignal bliver cue for fare:

```text
høj puls under trauma
        ↓
høj puls = fare
        ↓
træning / koffein / stress → threat prediction
```

## Safety learning er ikke det samme som akut ro
Et safety signal er information om fravær af forventet trussel. Safety learning kræver derfor, at systemet lærer noget om **relationen mellem cue, kontekst og outcome**.

Akut anxiolyse kan ske uden denne læring.

FearPrime adskiller:
- mindre subjektiv angst,
- mindre autonom respons,
- ændret threat expectancy,
- bedre CS+/CS−-diskrimination,
- senere safety recall,
- generalisering af sikkerhed til nye kontekster.

## Safety cues versus safety behaviours
De to begreber må ikke blandes sammen.

### Safety cue
Et signal eller en kontekst, der faktisk giver information om lavere risiko.

### Safety behaviour
En handling personen udfører for at forhindre eller reducere frygtet udfald.

Safety behaviours kan være funktionelle ved reel risiko, men i eksperimentelle eller terapeutiske læringssituationer kan de gøre outcome tvetydigt:

```text
"Der skete ikke noget"
        ↓
var situationen sikker?
eller
blev katastrofen kun undgået på grund af sikkerhedsadfærden?
```

Derfor registrerer FearPrime sikkerhedsadfærd som potentiel mediator/confounder frem for automatisk at kalde den god eller dårlig.

## FearPrime learning loop

### Trin 1 — Definér prediction
Prediction skal være observerbar.

Eksempel:
`P(negativt udfald) = 80%`

### Trin 2 — Definér cue og kontekst
Notér:
- stimulus,
- sted,
- tidspunkt,
- social kontekst,
- interoceptive signaler,
- safety behaviours.

### Trin 3 — Observer outcome
Klassificér:
- forventet negativt udfald,
- sikkert udfald,
- uklart udfald.

### Trin 4 — Beregn learning signal
Et simpelt projektmål kan være:

```text
prediction error ≈ forventet sandsynlighed − observeret udfald
```

Det er ikke identisk med dopaminerg prediction error på neuralt niveau; det er et adfærdsmæssigt observationsmål.

### Trin 5 — Test opdatering
Mål prediction igen senere.

### Trin 6 — Test generalisering
Skift kun én eller få dimensioner ad gangen:
- sted,
- person,
- tidspunkt,
- sensorisk lighed,
- kropslig tilstand.

Spørgsmålet er:

> Flytter sikkerhedslæringen sig med til den nye situation?

## Extinction-generalization
Extinction til ét cue kan generalisere til beslægtede stimuli, men nyere litteratur viser, at generalisering ikke kan antages automatisk. Især når kliniske eksponeringer bruger generalization stimuli frem for det oprindelige trauma-cue, kan læringen blive mere lokal end forventet.

FearPrime måler derfor mindst tre ting separat:
1. læring til den trænede stimulus,
2. læring til lignende nye stimuli,
3. læring i nye kontekster.

## Return of fear
Safety/extinction memory konkurrerer med ældre threat memory. Derfor kan frygt vende tilbage gennem:

- **spontaneous recovery** — tid,
- **renewal** — kontekstskift,
- **reinstatement** — ny aversiv hændelse,
- **rapid reacquisition** — ny læring om fare.

Return of fear betyder ikke nødvendigvis, at al tidligere læring er slettet.

Se også [EXTINCTION_RECONSOLIDATION_RETURN.md](EXTINCTION_RECONSOLIDATION_RETURN.md).

## Multiple-context learning
En systematisk review/meta-analyse fra 2024 af renewal i human conditioning fandt bl.a. støtte for, at extinction i flere kontekster og større lighed mellem acquisition- og extinction-kontekst kan reducere renewal.

FearPrime-hypotese:

```text
én sikker kontekst
   → stærk kontekstbinding

flere relevante sikre kontekster
   → mere robust retrieval / mindre kontekstafhængighed
```

Dette er en hypotese om læringsdesign, ikke et løfte om klinisk effekt i alle PTSD/CPTSD-populationer.

## Threat/safety discrimination som kernemål
FearPrime ønsker ikke blot lavere respons på CS+.

Et system der reagerer lavt på alt kan have dårlig diskrimination på en anden måde.

Derfor måles forskellen mellem threat og safety:

```text
Discrimination = response(CS+) − response(CS−)
```

Afhængigt af mål kan response være:
- expectancy,
- valence,
- SCR,
- startle,
- adfærd.

En opdateret 2025-meta-analyse af angst- og stressrelaterede lidelser fandt gruppeforskelle i acquisition, extinction og recall, men ikke en simpel konsistent forskel i CS+/CS−-differentiering på tværs af alle mål. FearPrime skal derfor ikke bygge en universel “dårlig discrimination”-påstand uden målspecifik evidens.

## Social safety learning
CPTSD kræver et udvidet spor.

Eksempler på målbare sociale predictions:
- sandsynlighed for afvisning,
- sandsynlighed for aggression,
- sandsynlighed for bedrag,
- forventning om hjælp,
- opdatering efter neutral eller positiv respons.

FearPrime undersøger både:
- korrekt detektion af reel social risiko,
- overgeneralisering fra tidligere relationer,
- underopdatering efter nye sikre erfaringer.

## Interoceptiv safety learning
Kropssignaler kan bruges som cues i læring.

Eksempel:
```text
puls ↑
↓
"fare kommer"
↓
ny sikker erfaring med puls ↑ uden fare
↓
interoceptiv prediction update
```

Målet er ikke at ignorere kropslige signaler, men at skelne signalets fysiologi fra den lærte betydning.

## Falsificerbare FearPrime-forudsigelser
1. bedre prediction calibration bør hænge sammen med bedre funktion mindst i nogle domæner.
2. læring i flere kontekster bør i relevante paradigmer reducere kontekstbundet return of fear.
3. sikkerhedslæring målt umiddelbart bør ikke automatisk forudsige senere generalisering.
4. nogle safety behaviours bør kunne svække inferensen “situationen var sikker”, men effekten bør afhænge af type og funktion.
5. social generalisering bør kunne variere uafhængigt af perceptuel generalisering.

## Nøglekilder
- Kausche FM et al. *Fear and safety learning in anxiety- and stress-related disorders: An updated meta-analysis*. Neurosci Biobehav Rev. 2025;169:105983. PMID: 39706234. DOI: 10.1016/j.neubiorev.2024.105983.
- Laing PAF et al. *Pavlovian safety learning: An integrative theoretical review*. Psychon Bull Rev. 2025. PMID: 39167292. DOI: 10.3758/s13423-024-02559-4.
- Wong AHK. *Spreading the reduction of fear: A narrative review of generalization of extinction learning in human fear conditioning*. Clin Psychol Rev. 2025;118:102580. PMID: 40184732. DOI: 10.1016/j.cpr.2025.102580.
- Craske MG et al. *Maximizing exposure therapy: An inhibitory learning approach*. Behav Res Ther. 2014;58:10-23. PMCID: PMC4114726.
- Haaker J et al. *Renewal in human fear conditioning: A systematic review and meta-analysis*. Neurosci Biobehav Rev. 2024;159:105606. PMID: 38431150. DOI: 10.1016/j.neubiorev.2024.105606.
- Wong AHK, Pittig A, Engelhard IM. *The generalization of threat beliefs to novel safety stimuli induced by safety behaviors*. Behav Brain Res. 2024;470:115078. PMID: 38825020. DOI: 10.1016/j.bbr.2024.115078.
- van Well S et al. *Fear generalization predicts post-traumatic stress symptoms: A two-year follow-up study in Dutch fire fighters*. 2024. PMID: 38484507.

## Debug
Generalization kan være adaptiv: når verden er usikker, er det rationelt at reagere på noget der ligner tidligere fare. Problemet er ikke generalisering i sig selv, men forholdet mellem sensitivitet, specificitet, kontekst og omkostning. FearPrime skal derfor måle både falske alarmer og oversete faresignaler.
