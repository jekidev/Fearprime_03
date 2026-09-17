# Plasticity Window Engine — FearPrime
Version 0.25 · 2026-09-17

## Formål
Plasticity Window Engine (PWE) samler FearPrimes vigtigste biologiske og læringsmæssige spor i én **testbar arbejdsmodel** for, hvornår ny safety/extinction-learning har størst chance for at blive stabil og generaliserbar.

Modellen er **ikke** en valideret matematisk ligning, en behandlingsprotokol eller en begrundelse for at kombinere forsøgsstoffer. Den er et kausalt kort, der tvinger projektet til at måle de forskellige led separat.

Se også:
- [Exposure/extinction engine](../03_EXTINCTION/EXTINCTION_ENGINE.md)
- [PNN/critical-period reopening](../02_MECHANISMS/PNN_CRITICAL_PERIOD_REOPENING.md)
- [HDAC/BDNF/TrkB-mekanismekort](../02_MECHANISMS/HDAC_BDNF_5HT7_DOPAMINE.md)
- [Human critical-period translation](../04_CANDIDATES/HUMAN_CRITICAL_PERIOD_TRANSLATION.md)
- [FP-BL-01 testplan](../06_MEASUREMENT/FP_BL_01_TEST_PLAN.md)

---

# Grundidé
En stærk plasticitetstilstand er ikke i sig selv terapeutisk.

```text
PLASTICITY WINDOW
        +
DET, DER FAKTISK LÆRES
        +
KONSOLIDERING
        +
GENERALISERING
        =
senere adfærd
```

Hvis læringsindholdet er forkert, uklart eller præget af overvældelse/sikkerhedsadfærd, kan øget plasticitet i princippet styrke **uønsket** læring.

Derfor arbejder PWE med seks separate gates.

---

# Gate 0 — baseline og stabilitet
## Spørgsmål
Er hjernen/kroppen i en tilstand, hvor dagens data overhovedet kan fortolkes?

Relevante variable:
- søvn og døgnrytme;
- eksisterende behandling/medicin og ændringer siden sidst;
- akut sygdom, smerte, koffein/stimulering eller anden markant state-change;
- forventningsniveau før sessionen;
- tidligere exposure samme dag/uge;
- kontekst og sikkerhedsadfærd.

### Hvorfor gate 0 findes
En session efter alvorlig søvnfragmentering eller stor ændring i behandlingsstate kan ikke uden videre sammenlignes med en stabil session. FearPrime skal derfor behandle **state** som en forsøgsvariabel, ikke støj der bare ignoreres.

---

# Gate 1 — åbning af plasticitetsvinduet
## Biologiske spor
PWE samler flere mekanismer, der kan ændre, hvor let kredsløb remodeleres:

```text
HDAC2 / chromatin
        ↓
Acan / PNN / PV maturation
        ↓
structural constraint

BDNF → TrkB
        ↓
activity-dependent synaptic plasticity

NMDA signaling
        ↓
learning-dependent plasticity

MMP / ECM remodeling
        ↓
structural synapse / PNN remodeling

NgR1 / myelin brakes
        ↓
constraint on adult remodeling
```

Disse spor er **ikke ækvivalente**. De kan åbne forskellige biologiske dele af vinduet og kan have forskellige risici.

## Evidensankre
- HDAC2/PV/Acan/PNN: Lavertu-Jolin 2023.
- PNN/critical-period: Gogolla 2009, Bhagat 2016, Poli 2023 m.fl.
- PV-TrkB/iPlasticity: Karpova 2011; Umemori 2023.
- Human epigenetic critical-period proof-of-principle: Gervain 2013/valproat.
- Human fear-learning ECM probe: doxycyclin/MMP-forsøg.

## Måleprincip
Gate 1 må aldrig estimeres alene ud fra, at et stof "burde øge plasticitet". Registrér i stedet:
1. hvilken mekanisme der påstås påvirket;
2. om central target engagement faktisk er dokumenteret;
3. om dokumentationen er human eller præklinisk;
4. hvor længe den formodede window-state varer.

---

# Gate 2 — teaching signal / prediction error
## Den centrale læringshændelse
Fear extinction starter ikke med et molekyle, men med en **forudsigelse der bliver testet**.

```text
forventning:
"X vil ske"
      ↓
meningsfuld kontakt med situationen
      ↓
faktisk udfald ≠ forventet udfald
      ↓
prediction error / expectancy violation
      ↓
ny information kan læres
```

Salinas-Hernández 2018 viste i mus et VTA-dopaminsignal ved den uventede udeblivelse af en forventet aversiv hændelse. Humane exposure-modeller og FearPrimes eksisterende extinction-engine understreger tilsvarende, at **hvad der bliver afkræftet** er vigtigere end blot at opnå ro.

## Gate 2 kan fejle når
- forventningen aldrig er skrevet/operationaliseret;
- sikkerhedsadfærd gør udfaldet tvetydigt;
- situationen stoppes før relevant information opstår;
- sessionen er så overvældende, at konklusionen bliver "jeg overlevede kun fordi jeg slap væk";
- ingen forskel findes mellem forventet og faktisk udfald.

## Primære målinger
- forventet udfald før trial;
- sikkerhed på forventningen;
- faktisk udfald;
- ændring i forventning efter trial;
- sikkerhedsadfærd;
- observerbar approach/avoidance.

---

# Gate 3 — synaptisk selektion: hvad bliver plasticiteten brugt til?
Plasticity-openeren er kun nyttig, hvis de aktive kredsløb under læringen er de kredsløb, man ønsker at ændre.

BDNF/TrkB-sporet er særligt relevant her. Moliner 2023 viste præklinisk, at psychedelics kan facilitere **endogen, aktivitet-afhængig BDNF-TrkB-signalering** frem for bare at tænde TrkB globalt. Det giver et nyttigt princip til PWE, selv om interventionen ikke er etableret som human fear-extinction-mekanisme:

> Plasticitet bør forstås som aktivitet-afhængig selektion, ikke bare "mere BDNF".

### PWE-konsekvens
Sessionens **indhold og timing** er potentielt lige så vigtigt som størrelsen af den biologiske plasticitetsændring.

---

# Gate 4 — konsolidering efter sessionen
Ny læring skal overleve efter at sessionen er slut.

## Centrale spor
### Søvn
Humane studier og reviews forbinder sleep/REM/SWS med konsolidering og recall af extinction/safety-learning, selv om resultaterne er heterogene. Søvnfragmentering er derfor en mulig svækkende faktor.

### Motion
Human PTSD/laboratoriedata viser, at moderat aerob motion efter extinction kan forbedre senere threat expectancy og at stigninger i perifert BDNF/anandamid statistisk kan mediere en del af denne relation.

### Dopamin efter learning
L-DOPA-litteraturen illustrerer, at en biologisk plausibel konsolideringsintervention ikke nødvendigvis giver robust human effekt. Andres 2024 reproducerede ikke en universel L-DOPA-fordel på extinction recall.

## Gate 4-regel
PWE registrerer **learning og consolidation separat**:

```text
god session + dårlig consolidation
            ≠
stabil memory
```

---

# Gate 5 — generalisering og retrieval
En extinction-memory kan være stærk i ét rum og stadig fejle i en anden kontekst.

Derfor måler PWE mindst fire forskellige former for senere udfald:

- **retention:** huskes safety-learning senere?
- **renewal:** kommer fear tilbage i ny kontekst?
- **reinstatement:** kommer fear tilbage efter en ny aversiv hændelse?
- **spontaneous recovery:** kommer fear tilbage med tiden?

Det er biologisk vigtigt, fordi Lavertu-Jolin/PNN-sporet især handler om **senere return of fear**, ikke bare hvor hurtigt freezing falder under selve extinction-sessionen.

---

# Gate R — risiko for forkert eller for bred plasticitet
Dette er en separat gate, ikke en fodnote.

## R1. Maladaptive learning amplification
En stærk plasticity-state kan teoretisk konsolidere:
- hjælpeløshed;
- ny avoidance;
- state-dependent safety;
- konklusionen "jeg klarede det kun på grund af stof/person/sikkerhedsadfærd".

## R2. Stabilitetsomkostning
PNN og PV+-modning er ikke kun "bremser". Cramer 2026 viste i en præklinisk visual-cortex-model, at PNN-loss og øget plasticitet også kunne ledsages af øget oxidativ stress i PV+-celler.

## R3. Memory-phase mismatch
Doxycyclin/MMP-data hos mennesker viser, at samme biologiske system kan give forskellig retning afhængigt af acquisition, reminder/reconsolidation og memory-type.

## R4. Off-target biology
Butyrat påvirker flere klasse-I-HDAC'er; valproat og ketamin er brede farmakologiske interventioner; fluoxetin har mange downstream-effekter. En adfærdsændring identificerer derfor ikke mekanismen automatisk.

---

# Engine-logik — ikke en matematisk score
PWE bruger et **gate-princip**: et svagt led kan begrænse det samlede resultat.

| Window | Learning | Consolidation | Generalisering | Forventet fortolkning |
|---|---|---|---|---|
| Lav | God | God | God | Ny læring kan ske, men biologisk augmentation er måske begrænset |
| Høj | Dårlig | God | God | Risiko for at gøre dårlig/uklar læring mere stabil |
| Høj | God | Dårlig | — | God akut session, svag senere retention |
| Høj | God | God | Dårlig | Stærk men kontekstbundet extinction-memory |
| Høj | God | God | God | Den komplette PWE-hypotese er opfyldt; skal stadig testes mod kontrol |

Det er **ikke** tilladt at konvertere tabellen til et selvopfundet numerisk "plasticity score" uden valideringsdata.

---

# PWE-session som forskningsobjekt
## Før session
Registrér:
- søvn/state;
- præcis frygtet forudsigelse;
- forventningsstyrke;
- planlagt sikkerhedsadfærd;
- biologiske interventioner/medicin som forsøgsmetadata, ikke forklaring.

## Under session
Registrér trial-by-trial:
- forventning;
- faktisk udfald;
- prediction error;
- approach/avoidance;
- sikkerhedsadfærd;
- om ny information faktisk kunne læres.

## Umiddelbart efter
Registrér:
- hvad deltageren mener blev lært;
- ændring i prediction;
- state/tolerabilitet;
- om sessionen sluttede efter reel læring eller efter escape.

## Efter 24 timer
Test retention uden at gøre testen unødigt lang, fordi selve testen kan skabe ny extinction-learning.

## Efter cirka 7 dage
Primært forsinket recall/retention-mål; test eventuelt ny kontekst separat.

## Senere
Mål funktion, spontaneous recovery, renewal og eventuelt reinstatement adskilt.

---

# Testbare PWE-hypoteser
### H1 — Window × learning interaction
En plasticity-opener bør kun give varig gevinst, hvis sessionen indeholder tydelig prediction error/ny safety-information.

### H2 — Consolidation mediation
Hvis en post-session intervention virker gennem konsolidering, bør den ændre **senere retention** mere end den akutte session.

### H3 — PNN/HDAC2 signature
Hvis HDAC2/PV/Acan/PNN-sporet er den relevante mediator, bør en mere selektiv HDAC2-manipulation og en bred HDAC-hæmmer ikke nødvendigvis give samme profil på return-of-fear-mål.

### H4 — Generalization is separable
En intervention kan forbedre retention i træningskonteksten uden at forbedre renewal i ny kontekst.

### H5 — Sleep as moderator
Dårlig post-session sleep bør kunne svække senere retention selv efter en god akut læringssession.

### H6 — Too much opening is not monotonic benefit
Mere biologisk plasticitet bør ikke antages at give lineært bedre outcome; risiko- og stabilitetsomkostninger skal måles.

---

# Hvordan PWE ændrer FearPrime
Den tidligere arbejdshypotese kunne let læses som:

`stof → plasticitet ↑ → exposure virker bedre`

PWE erstatter den med:

```text
BASELINE/STATE
      ↓
WINDOW OPENNESS
      ↓
PREDICTION ERROR + LEARNING CONTENT
      ↓
ACTIVITY-DEPENDENT SYNAPTIC SELECTION
      ↓
CONSOLIDATION
      ↓
GENERALIZATION / RETURN-OF-FEAR TESTS
      ↓
FUNCTION

med RISK/STABILITY som parallel akse gennem hele kæden
```

Det gør modellen kompatibel med både positive og negative data og giver konkrete steder, hvor en intervention kan fejle.

## Evidensstatus
- **Gate 1:** stærk præklinisk mekanistik, begrænset direkte human target engagement.
- **Gate 2:** stærk læringsteoretisk og præklinisk støtte; human exposure-litteratur relevant.
- **Gate 3:** stærk mechanistic plausibility, især TrkB; direkte human fear-circuit måling begrænset.
- **Gate 4:** human støtte for søvn og motion; stofdata blandede.
- **Gate 5:** human/præklinisk return-of-fear litteratur, men protokoller varierer.
- **Gate R:** biologisk velbegrundet; størrelsen af risikoen for specifikke interventioner skal måles, ikke antages.

## Projektregel
FearPrime må fremover aldrig kalde en intervention en "extinction enhancer" alene fordi den øger en plasticitetsmarkør. Der kræves mindst:

1. dokumenteret læringshændelse;
2. forsinket retention;
3. separat return-of-fear/generaliseringsmål;
4. tolerabilitet/funktion;
5. korrekt evidensniveau for den foreslåede mekanisme.
