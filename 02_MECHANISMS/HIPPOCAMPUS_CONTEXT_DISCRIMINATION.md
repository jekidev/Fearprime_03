# FearPrime — hippocampus, kontekst og diskrimination

Version 0.20 · 2026-09-17

## Formål
Dette modul beskriver hippocampus som en del af et distribueret system for **kontekstkodning, pattern separation/discrimination, retrieval og generalisering**. FearPrime bruger ikke modellen “lille hippocampus = PTSD”. Struktur, aktivitet, connectivity og adfærd måles og fortolkes separat.

Se også:
- [Fear Circuit Master Map](FEAR_CIRCUIT_MASTER_MAP.md)
- [Generalization & Safety Learning Engine](../03_EXTINCTION/GENERALIZATION_AND_SAFETY_LEARNING_ENGINE.md)
- [Learning Metrics](../06_MEASUREMENT/LEARNING_METRICS.md)

---

## 1. Arbejdsmodel

```text
sensoriske/sociale/interoceptive cues
            +
       aktuel kontekst
            ↓
 hippocampal kontekstrepræsentation
            ↓
lighed vs forskel fra tidligere situationer
            ↓
pattern completion  ↔  pattern separation
            ↓
"samme fare"       ↔  "ny/sikker kontekst"
            ↓
retrieval + vmPFC/amygdala/striatum
            ↓
trussels- eller sikkerhedsrespons
```

Hippocampus er derfor relevant for FearPrimes spørgsmål om, **hvornår en tidligere korrekt faremodel generaliseres til en ny situation, hvor den ikke længere passer**.

## 2. PTSD og kontekst
Garfinkel et al. (2014) viste i et to-dages fMRI/psykofysiologisk paradigme nedsat kontekstuel modulation af extinction retention/fear renewal ved PTSD. Kilden understøtter et kontekstproblem, men dokumenterer ikke én isoleret hippocampal årsag.

- PMID `25274821`
- DOI `10.1523/JNEUROSCI.4287-13.2014`

Steiger et al. (2015) fandt i et cue-context paradigme mindre differentiering mellem threat- og safe-contexts i PTSD samt afvigende hippocampal respons. Det støtter, at kontekstuel contingency learning og neural respons kan dissociere.

- PMID `26149734`
- DOI `10.1016/j.ijpsycho.2015.06.009`

Liberzon & Abelson (2016) formulerede en bredere context-processing model, hvor hippocampal-prefrontal-thalamiske kredsløb hjælper med at give cues situationsspecifik betydning. FearPrime bruger dette som teori/review, ikke som bevist monokausal forklaring.

- PMID `27710783`
- DOI `10.1016/j.neuron.2016.09.039`

## 3. Generalisering og diskrimination
Levy-Gigi et al. (2015) rapporterede overgeneralisering af negativ kontekst ved PTSD og en association med bilateral hippocampal volumen. Associationen er relevant, men korrelation mellem volumen og adfærd identificerer ikke retningen på kausalitet.

- PMID `25068667`
- DOI `10.1037/neu0000131`

I raske deltagere viste de Voogd et al. (2020), at styrken af hippocampale rumlige kontekstrepræsentationer hang sammen med, hvor meget frygt generaliserede til en safe context; vmPFC var samtidig involveret i context-dependent fear expression.

- PMID `31669410`

Webler et al. (2024) brugte hippocampal-network-targeted TMS hos personer med posttraumatiske symptomer. Interventionen forbedrede ikke diskrimination generelt, men viste et betinget signal hos deltagere med mindre ikke-associativ sensitization. Det er et vigtigt modargument mod en enkel “mere hippocampusaktivitet = bedre diskrimination”-model.

- PMID `38690260`

## 4. Nyere kontekstdata
Siehl et al. (2023) anvendte virtual-reality cue/context conditioning og fandt bl.a. lavere hippocampal aktivitet i en uforudsigelig kontekst hos PTSD sammenlignet med trauma-exposed controls, mens selvrapport og SCR ikke viste tilsvarende gruppeforskelle.

- PMID `36601857`
- DOI `10.1017/S0033291722003695`

Et 2026-studie af Leri et al. undersøger kontekstuel threat/safety discrimination på tværs af PTSD, trauma-exposed, anxiety og healthy controls med multivariat fMRI. Det er vigtigt for FearPrime, fordi flere kontrolgrupper hjælper med at skelne PTSD-specifikke fund fra traumeeksponering eller generel angst.

- PMID `42067061`

## 5. FearPrime-variabler
Et hippocampus/context-spor bør ikke reduceres til symptomscore. Registrér så vidt muligt:

1. threat-context expectancy,
2. safe-context expectancy,
3. context discrimination = threat − safe,
4. cue discrimination inden for hver kontekst,
5. renewal ved kontekstskift,
6. extinction-context reinstatement,
7. generalisering til novel contexts,
8. associative generalization versus ikke-associativ sensitization.

## 6. Falsificerbare predictions
FearPrime-context-modellen svækkes hvis:
- kontekstdiskrimination ikke relaterer sig til generalisering eller renewal,
- hippocampale mål ikke tilfører forklaringskraft ud over generel arousal/sensitization,
- forbedret kontekstrepræsentation ikke hænger sammen med bedre safety retrieval,
- samme mønster forklares bedre af amygdala/salience eller generelle opmærksomhedsmål alene.

## 7. Debug
- Hippocampal volumen, BOLD-aktivitet, multivariat repræsentation og connectivity er forskellige mål.
- “Pattern separation” er en mekanistisk fortolkning og bør ikke påstås direkte ud fra enhver diskriminationsopgave.
- Overgeneralisering kan være perceptuel, semantisk, social, interoceptiv eller kontekstuel; hippocampus behøver ikke dominere alle former.
- PTSD-fund skal sammenlignes med trauma-exposed controls, ikke kun aldrig-traumatiserede kontroller.

## FearPrime-konklusion
Hippocampus er mest nyttig i frameworket som del af en **context/discrimination engine**: systemet skal afgøre, om den aktuelle situation er “samme fare” eller “tilstrækkeligt forskellig til at opdatere modellen”. Evidensen støtter relevansen af hippocampal-kontekstuelle processer, men ikke en enkel én-region-forklaring på PTSD.