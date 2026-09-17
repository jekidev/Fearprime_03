# FearPrime — NMDA / AMPA / glutamaterg plasticitet

Version 0.21 · 2026-09-17

## Formål
Dette modul beskriver glutamaterg læring og plasticitet i FearPrime med fokus på **NMDA-receptorer, AMPA-receptorer, LTP/LTD og extinction learning**.

Det er et mekanismemodul, ikke et argument for at "mere glutamat" er bedre.

Se også:
- [Learning metrics](../06_MEASUREMENT/LEARNING_METRICS.md)
- [Fear Circuit Master Map](FEAR_CIRCUIT_MASTER_MAP.md)
- [D-cycloserin-dossier](../04_CANDIDATES/DCS_DOSSIER.md)
- [HDAC/BDNF/5-HT7/dopamin](HDAC_BDNF_5HT7_DOPAMINE.md)

---

## 1. Grundmodel
Glutamat er den primære excitatoriske transmitter i hjernen, men FearPrime modellerer ikke systemet som en global "glutamat-balance". Receptor-type, synapse, timing, kredsløb og læringsfase er afgørende.

```text
presynaptisk glutamat
        ↓
AMPA-receptor → hurtig depolarisering
        ↓
NMDA-receptor åbnes ved passende glutamat + depolarisering
        ↓
Ca2+-signalering
        ↓
CaMKII / kinase- og genekspressionskaskader
        ↓
synaptisk plasticitet
        ↓
ændret læring / konsolidering / extinction memory
```

## 2. NMDA-receptoren
NMDA-receptorer fungerer som centrale coincidence detectors for aktivitetsafhængig plasticitet. De kræver både ligandbinding og passende membranforhold for stærk kanalaktivering.

I fear/extinction-litteraturen er NMDA-receptoraktivering gentagne gange koblet til:
- acquisition,
- extinction learning,
- konsolidering af extinction,
- synaptisk plasticitet i amygdala–mPFC–hippocampus-kredsløb.

Review: PMID `36983000`.

## 3. AMPA-receptoren
AMPA-receptorer medierer hurtig excitatorisk transmission og ændrer synaptisk styrke gennem trafficking, insertion, removal og subunit-sammensætning.

Fear learning kan øge synaptisk AMPAR-trafik; extinction involverer ikke nødvendigvis simpel reversal, men kan kræve specifik receptortrafik og LTD/LTP-lignende processer.

Præklinisk evidens viser bl.a., at manipulation af AMPAR-endocytose kan ændre extinction uden at have samme effekt på acquisition eller recall.

PMID `18046303`.

## 4. NMDA og AMPA arbejder sammen
Forenklet:

```text
AMPA = hurtig transmission / depolarisering
NMDA = plasticitetsport / Ca2+-afhængig læringssignalering
```

Men dette er kun en undervisningsmodel. I levende kredsløb findes mange receptor-subunits, interneuron-effekter, metabotrope glutamatreceptorer og homeostatisk plasticitet.

## 5. LTP og LTD
FearPrime skelner mellem:
- **LTP-lignende styrkelse** af synaptiske associationer,
- **LTD-lignende svækkelse/reorganisering**,
- **ny inhibitorisk læring**, som kan konkurrere med den oprindelige fear association.

Extinction er derfor ikke lig med global synaptisk depression eller "sletning".

## 6. D-cycloserin som NMDA-probe
D-cycloserin (DCS) er en partiel agonist ved glycin-modulatorisk site på NMDA-receptoren og er den bedst undersøgte humane farmakologiske translation af NMDA-extinction-hypotesen.

DCS-data viser samtidig en vigtig FearPrime-regel:

```text
plasticity enhancer + god læring → mulig forstærkning af extinction
plasticity enhancer + dårlig læring → kan forstærke den forkerte læring / give ingen fordel
```

Derfor er session quality og tidspunkt centralt.

## 7. AMPA-PAM-sporet
Positive allosteriske modulatorer af AMPA-receptorer kan øge excitatorisk transmission og i nogle prækliniske systemer påvirke BDNF og LTP.

Men direkte human fear-extinction/PTSD-evidens for AMPA-PAMs er væsentligt svagere end for DCS/NMDA-sporet. Humant target engagement i andre indikationer er ikke det samme som klinisk FearPrime-evidens.

TAK-653 har fx humane CNS-farmakodynamiske data, men det dokumenterer ikke PTSD/extinction-effekt. PMID `36153330`.

## 8. Plasticitet er bidirektionel
FearPrime afviser:

```text
mere NMDA/AMPA plasticitet = automatisk mindre PTSD
```

Stærkere plasticitet kan potentielt støtte:
- threat acquisition,
- fear generalization,
- reconsolidation,
- extinction,
- safety learning.

Resultatet afhænger af **hvilken information der er aktiv**, hvornår manipulationen gives, og hvad der konsolideres.

## 9. Fase-specifik model
| Fase | Mulig glutamaterg rolle | FearPrime-måling |
|---|---|---|
| acquisition | association + LTP-lignende plasticitet | CS+/CS− discrimination |
| extinction | ny læring, NMDA-afhængig plasticitet | extinction slope |
| consolidation | stabilisering af ny læring | delayed recall |
| generalization | stimulus/context transfer | GS gradient |
| reconsolidation | updating efter retrieval under visse betingelser | M-score + delayed outcomes |
| reacquisition | genindlæring efter extinction | reacquisition slope |

## 10. Human translation
Et 2025-review af PTSD-behandlinger afledt fra fear-extinction forskning vurderer NMDA-modulation som et relevant translationalt spor, men litteraturen om farmakologiske augmenters er blandet og ofte outcome-/timingafhængig.

PMID `39032727` · DOI `10.1016/j.biopsych.2024.07.010`.

Et 2025 Trends in Cognitive Sciences-review understreger tilsvarende, at farmakologiske extinction-enhancers ofte giver null eller modstridende humane resultater. PMID `40634208`.

## 11. Testbare predictions
Hvis en NMDA/AMPA-manipulation faktisk forbedrer safety/extinction learning, bør den:

1. påvirke delayed recall, ikke kun akut distress,
2. være afhængig af kvaliteten af den læring, der sker under vinduet,
3. kunne adskilles fra generel sedation/stimulering,
4. vise fase- og timingafhængighed,
5. ikke nødvendigvis forbedre alle modaliteter (SCR/startle/expectancy kan divergere).

## 12. Evidensstatus
| Påstand | Status |
|---|---|
| NMDA-receptorer er centrale for fear/extinction plasticitet | ✅ stærk præklinisk + human translational støtte |
| DCS kan modulere exposure/extinction outcomes hos mennesker | ✅/🟡 blandet human evidens |
| DCS giver robust klinisk PTSD-fordel | 🟡/konflikt |
| AMPA trafficking er relevant for fear/extinction | ✅ præklinisk |
| AMPA-PAM er etableret human PTSD/extinction augmentation | 🔴 |

## 13. Debug
Glutamatsporet er biologisk stærkt, men translationen fra receptorplasticitet til klinisk effekt er begrænset af timing, task-design, session quality og population. FearPrime bruger derfor DCS som et eksempel på, hvorfor stærk mekanistisk plausibilitet ikke automatisk giver stor eller konsistent behandlingseffekt.
