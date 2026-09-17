# HDAC2-selektive hæmmere — FearPrime dossier
Version 0.22 · 2026-09-17

## Forskningsspørgsmål
Findes der farmakologiske værktøjer, som ligger tættere på FearPrimes prækliniske mål **HDAC2 → PV+-interneuroner → Acan/aggrecan → perineuronale net → extinction-retention** end brede HDAC-hæmmere som butyrat?

Kort svar: **ja, præklinisk**. BRD6688 er den mest direkte mekanistiske match, fordi den allerede er brugt i Lavertu-Jolin 2023 før extinction og reducerede senere spontan fear recovery. Nyere forbindelser har bedre selektivitets-/CNS-profiler, men mangler direkte fear-extinction-data.

Dette dokument fokuserer på **validerede eller mekanistisk relevante CNS/extinction-værktøjer**. Det er ikke en katalogliste over alle kræftkemiske analoger, patentforbindelser eller rent in-silico HDAC2-kandidater. Ingen af forbindelserne nedenfor er dokumenteret som behandling for PTSD hos mennesker.

## Evidensmatrix
| Forbindelse | HDAC-profil | CNS/in vivo | Fear-extinction-data | FearPrime-status |
|---|---|---|---|---|
| **BRD6688** | Kinetisk præference for HDAC2 over HDAC1; stærk HDAC1/2 vs HDAC3-separation | Brain-penetrant; histonacetylering i musehjerne | **Ja**: Lavertu-Jolin 2023, før extinction | **Tætteste direkte mekanistiske værktøj** |
| **BRD4884** | Kinetisk HDAC2-præference; HDAC1/2-biokemisk aktivitet | CNS-optimeret; øget histonacetylering og rescued memory i CK-p25-mus | Ikke direkte extinction fundet | Stærkt HDAC2/cognition-værktøj |
| **Compound 11 / HDAC2-IN-3** | Ny 2026 cellulært HDAC2-selektiv serie; sekundær annotation angiver ~14 nM HDAC2 | Oral, BBB-relevant; hippocampal H4K12Ac og LTP i APP/PS1-mus | Ingen extinction-data fundet | **Nyeste stærke CNS-HDAC2-kandidat** |
| **Compound 17 / HDAC2-IN-1** | HDAC2 ~0,5 µM; også HDAC8/HDAC1; lav isoform-selektivitet | Oral; Kp,uu ~0,36; øget H4K12Ac i musehjerne | Ingen extinction-data | CNS-proof-of-concept, men ikke ren HDAC2-probe |
| **Rodin-A** | Kompleks-selektiv HDAC1/2-hæmning i CoREST; ikke HDAC2-only | Oral; fri hippocampal eksponering, øget spinedensity og LTP | Ingen extinction-data | **Kompleks-selektiv neuronal comparator** |
| **KPZ560** | HDAC1/2-selektiv, slow-binding mod HDAC2 | Neurit-/spine-effekter; ikke dokumenteret som HDAC2-only | Ingen extinction-data | Comparator, ikke HDAC2-selektiv nok |
| **Cpd-60** | HDAC1/2; HDAC1 mere potent end HDAC2 | Brain-penetrant | Adfærd i mood-relaterede tests, ikke HDAC2-specifik extinction | Comparator |
| **RGFP963** | HDAC1/2/3 | Brain-penetrant | **Ja**: forbedret cued fear-extinction consolidation i mus | Direkte extinction-comparator, men kan ikke tilskrives HDAC2 |
| **Santacruzamate A / CAY10683** | Oprindeligt rapporteret picomolær HDAC2-selektivitet | Neuroinflammationsrapporter findes | Ingen valideret HDAC2-extinction-kæde | **Diskvalificeret som pålidelig HDAC2-probe pga. manglende replikation** |
| **Butyrat** | Bred klasse-I-præference HDAC1/2/3/8 | Formuleringsafhængig CNS-eksponering | Human extinction-retention signal med NaBut; ikke HDAC2-target engagement | Translationalt interessant, men mekanistisk bredt |

## 1. BRD6688 — den vigtigste FearPrime-reference
[Wagner et al. 2015](../07_STUDIES/PRECLINICAL/2015_Wagner_BRD6688_BRD4884_HDAC2.md) udviklede BRD6688 som et CNS-relevant ortho-aminoanilid. Dets særlige styrke er **kinetisk selektivitet**: den biokemiske ligevægts-potens favoriserer ikke HDAC2 over HDAC1, men residence time er omtrent seks gange længere på HDAC2 end HDAC1. HDAC3-potensen er langt svagere.

I [Lavertu-Jolin 2023](../07_STUDIES/PRECLINICAL/2023_Lavertu_Jolin_HDAC2_Acan_PNN_Extinction.md) blev BRD6688 administreret efter fear acquisition og seks timer før extinction. I voksne wild-type-mus reducerede interventionen senere spontan fear recovery og Acan-ekspression; effekten blev occluded ved PV+-specifikt Hdac2-tab.

Det gør BRD6688 til den **mest direkte farmakologiske bro** i FearPrime mellem:

`HDAC2-targeting → extinction-session → PV/Acan/PNN-spor → mindre senere return of fear`

Begrænsning: BRD6688 er et forskningsstof, musefund og ikke en human PTSD-intervention.

## 2. BRD4884
BRD4884 kommer fra samme medicinalkemiske program. Det hæmmer både HDAC1 og HDAC2 biokemisk, men har længere residence time på HDAC2 end HDAC1. Wagner-studiet viste CNS-farmakologi, histonacetylering i hippocampus og forbedring af hukommelsesdefekter i CK-p25-modellen.

FearPrime-status: bedre subtype-værktøj end butyrat, men **mindre direkte extinction-evidens end BRD6688**.

## 3. Compound 11 / HDAC2-IN-3 — 2026-generationen
[Suzuki et al. 2026](../07_STUDIES/PRECLINICAL/2026_Suzuki_HDAC2_Compound11.md) udviklede cellulære assays til at adskille HDAC2 fra HDAC1 og optimerede en serie til compound 11. Primærartiklens abstract beskriver in-vivo øget histonacetylering, forbedret hippocampal LTP og fravær af den hæmatologiske toksicitet, som forbindes med samtidig HDAC1/2-hæmning i deres humane blodcellemodel.

En kommerciel annotation af artiklen angiver HDAC2 IC50 omkring 14 nM og oral/BBB-permeabel profil; den eksakte tabelværdi er registreret som **sekundær annotation**, indtil primærtabellen er fuldt udtrukket.

FearPrime-status: den mest interessante nyere forbindelse, hvis spørgsmålet er **selektiv CNS-HDAC2 target engagement**, men den mangler endnu direkte extinction/PV/PNN-data.

## 4. Compound 17 / HDAC2-IN-1 — brain penetration uden stærk subtype-selektivitet
[Tamanini et al. 2022](../07_STUDIES/MECHANISTIC/2022_Tamanini_HDAC2_Compound17.md) udviklede en oral, brain-penetrant α-amino-amid-serie. Compound 17 hæmmer HDAC2 sub-mikromolært og giver H4K12/H3K9-acetylering i celler samt H4K12-acetylering i musehjerne.

Men forfatterne skriver eksplicit, at target-selectiviteten over nært beslægtede class-I-HDAC'er er begrænset. Derfor er det et godt **CNS delivery/PD proof-of-concept**, men ikke et bedre HDAC2-isolationsværktøj end BRD6688 eller compound 11.

## 5. Rodin-A — kompleks-selektivitet som alternativ strategi
Fuller et al. 2019 udviklede Rodin-A til at favorisere **HDAC1/2-aktivitet i CoREST-komplekset** frem for bred HDAC1/2-hæmning på tværs af alle corepressor-komplekser. HDAC2 associerer stærkt med CoREST i hjernen, så dette er en anden form for selektivitet end isoform-selectivity.

Rodin-A gav målelig fri hippocampal eksponering, øgede dendritisk spine density og forbedrede LTP i 5xFAD-mus. Studiet rapporterede samtidig en bedre præklinisk hæmatologisk sikkerhedsprofil end bredere comparators.

FearPrime-status: interessant fordi **kompleks/kontekst-selektivitet** måske kan være lige så biologisk vigtig som isoleret HDAC2-IC50. Men Rodin-A er ikke HDAC2-only og er ikke testet i fear extinction/PNN-sporet.

Kilde: Fuller NO et al. *CoREST Complex-Selective Histone Deacetylase Inhibitors Show Prosynaptic Effects and an Improved Safety Profile To Enable Treatment of Synaptopathies*. ACS Chem Neurosci. 2019;10:1729–1743. PMID 30496686. DOI 10.1021/acschemneuro.8b00620.

## 6. Santacruzamate A / CAY10683 — vigtig negativ kontrol
Den oprindelige rapport fra 2013 beskrev ~0,11 nM HDAC2-potens og tusindfold selektivitet over HDAC4/6. Senere uafhængig syntese kunne ikke reproducere HDAC2-hæmningen, og efterfølgende bred HDAC1-11-test placerede aktiviteten omkring 5–10 µM uden den oprindelige HDAC2-selektivitet.

Se [replikationskort](../07_STUDIES/MECHANISTIC/2013_2016_Santacruzamate_HDAC2_Replication.md).

**FearPrime-regel:** Catalog-labels som “HDAC2 selective” må ikke accepteres uden reproduceret target-engagement og isoformprofil.

## 7. Direkte extinction-comparator: RGFP963
[Bowers et al. 2015](../07_STUDIES/PRECLINICAL/2015_Bowers_RGFP963_Extinction.md) viste, at den brain-penetrante class-I-hæmmer RGFP963 forbedrede konsolidering af cued fear extinction i mus, mens den HDAC3-selektive RGFP966 ikke gjorde det ved samme forsøgsdosis.

Det er kompatibelt med en rolle for HDAC1 og/eller HDAC2, men **RGFP963 hæmmer HDAC1, HDAC2 og HDAC3**. Resultatet må derfor ikke bruges som HDAC2-specifikt bevis.

## 8. Butyrat versus selektive værktøjer
Butyrat hæmmer klasse-I-HDAC'er bredt. I Kilgore-assayet var HDAC3 mindst lige så følsom som HDAC2. Derfor er butyrat translationalt interessant på grund af menneskelige data, men et dårligt værktøj til at teste den smalle mekanisme:

`HDAC2 i PV+-celler → Acan/PNN → return of fear`

Til dét forskningsspørgsmål er BRD6688 langt mere informativt præklinisk.

## Mekanistisk konklusion
Der er nu fire forskellige spørgsmål, som FearPrime ikke må blande sammen:

1. **Virker en intervention på human extinction-retention?** — NaBut har et humant signal.
2. **Rammes HDAC2 mere selektivt end andre HDAC'er i CNS?** — BRD6688/BRD4884 og især nyere compound 11 er relevante prækliniske værktøjer.
3. **Kan neuronal kompleks-selektivitet være bedre end simpel isoform-selektivitet?** — Rodin-A/CoREST er et relevant præklinisk spor.
4. **Er HDAC2/PV/Acan/PNN den mediator, der forklarer forbedret extinction?** — Lavertu-Jolin 2023 støtter dette i mus med BRD6688/genetik, men den humane kæde er ikke vist.

## FearPrime-prioritering efter mekanistisk nærhed
Denne rækkefølge angiver **nærhed til den prækliniske HDAC2/PV/PNN-hypotese**, ikke klinisk anbefaling:

1. **BRD6688** — direkte brugt i extinction + Acan/PNN-studiet.
2. **Compound 11 / HDAC2-IN-3** — nyere, stærkere cellulær HDAC2-selektivitet + CNS/LTP, men ingen extinction-data.
3. **BRD4884** — robust CNS/cognition-værktøj med kinetisk HDAC2-præference.
4. **Rodin-A** — neuronalt relevant CoREST-HDAC1/2-selectivity + direct brain/spine/LTP, men ikke HDAC2-only.
5. **Compound 17** — brain penetrant, men for begrænset isoform-selektivitet.
6. **RGFP963** — direkte extinction-signal, men HDAC1/2/3-bredt.
7. **Butyrat** — mest relevant human translationalt, men bred HDAC-biokemi.
8. **Santacruzamate A/CAY10683** — ikke anvendelig som valideret HDAC2-probe efter replikationsproblemer.

## Nøglekilder
- Wagner et al. 2015. *Chemical Science*. DOI 10.1039/C4SC02130D · PMID 25642316.
- Bowers et al. 2015. *Learning & Memory*. DOI 10.1101/lm.036699.114 · PMID 25776040.
- Fuller et al. 2019. *ACS Chemical Neuroscience*. DOI 10.1021/acschemneuro.8b00620 · PMID 30496686.
- Tamanini et al. 2022. *ACS Med Chem Lett*. DOI 10.1021/acsmedchemlett.2c00272 · PMID 36262388.
- Lavertu-Jolin et al. 2023. *Molecular Psychiatry*. DOI 10.1038/s41380-023-02085-0 · PMID 37131076.
- Itoh et al. 2023. *J Med Chem*. DOI 10.1021/acs.jmedchem.3c01095.
- Suzuki et al. 2026. *J Med Chem*. DOI 10.1021/acs.jmedchem.5c02022 · PMID 41844374.
- Santacruzamate original report: PMID 24164245; subsequent non-replication/analogue work documented in the study card.
