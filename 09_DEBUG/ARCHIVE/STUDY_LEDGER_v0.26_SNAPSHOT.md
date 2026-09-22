# FearPrimes samlede studieregister
Version 0.26 · 2026-09-18

Dette er indgangen til alle registrerede studiekort og kilder. Den maskinlæsbare parallel findes i [`data/studies.csv`](../../data/studies.csv), med separate effect-, RoB-, overlap-, PubMed-screening- og certainty-tabeller beskrevet i [`data/README.md`](../../data/README.md). Den tidligere hovedliste indeholdt gentagne litteraturpakker; dens kilder er bevaret, mens beskrivelserne er samlet tematisk og redigeret på dansk.

**Kontrolstatus:** Historiske VERIFIED-mærker betyder ikke, at hele litteraturen er kontrolleret på ny. Det enkelte kort angiver design, udfald og kontrolniveau. Nye bibliografiske spor holdes adskilt fra kontrollerede resultater.

## Evidenstyper
A: kliniske udfald i forsøg/sammenfatninger. B: raske menneskers eksperimentelle frygtlæring. C: dyreforsøg med adfærdsmål. D: mekanismer og biomarkører. E: projektets hypotese. Kliniske observations- og pilotdesign navngives særskilt; bogstavet er ikke en kvalitetskarakter.

## FearPrime R0–R4: robusthed og replikation
R-scoren er et **internt robusthedsindeks** og må ikke forveksles med evidenstype A–E, klinisk effektstørrelse eller behandlingsanbefaling. Scoren gælder den konkrete påstand, som kortet bruges til at støtte.

- **R0 — ukontrolleret spor:** citation/hypotese eller fund uden tilstrækkelig kontrol til robusthedsvurdering.
- **R1 — tidligt signal:** verificeret enkeltstudie/pilot, men lille, indirekte, ukontrolleret eller stærkt begrænset for den relevante påstand.
- **R2 — kontrolleret enkeltfund:** direkte og relevant kontrolleret primærstudie, men uden stærk uafhængig replikation eller med væsentlige boundary-/generaliseringsproblemer.
- **R3 — replikations-/konvergensniveau:** preregistreret eller stærk direkte replikation, eller flere uafhængige kontrollerede fund. R3 kan være et **positivt eller negativt/modstridende** fund.
- **R4 — robust konvergens:** flere uafhængige replikationer og/eller stærk meta-analytisk konvergens i relevant population, paradigme og outcome. R4 bruges restriktivt.

Et negativt replikationsstudie kan således være R3, hvis det robust tester en påstand. R-scoren siger ikke, om effekten er ønskværdig; den siger hvor robust den konkrete evidenspåstand er.

### Reconsolidation-audit — claim-specific R-score
| Studie/spor | Type | Retning | R | FearPrime-fortolkning |
|---|---:|---|---:|---|
| Nader 2000, præklinisk fear memory | C | positiv mekanistisk | R3 | Stærkt fundament for retrieval-afhængig restabilisering i dyremodel; ikke direkte human PTSD |
| [Kindt 2009](../../07_STUDIES/VERIFIED/2009_Kindt_Propranolol_Human_Fear_Reconsolidation.md) | B | positiv | R2 | Humant propranolol proof-of-concept; outcome- og paradigmespecifikt |
| [Schiller 2010](../../07_STUDIES/VERIFIED/2010_Schiller_Retrieval_Extinction.md) | B | positiv | R2 | Klassisk retrieval-extinction-signal; robustheden reduceres af senere direkte replikation |
| [Sevenster 2012](../../07_STUDIES/VERIFIED/2012_Sevenster_Retrieval_Not_Sufficient.md) | B | boundary | R2 | Retrieval alene var utilstrækkelig i paradigmet |
| [Sevenster 2013](../../07_STUDIES/VERIFIED/2013_Sevenster_Prediction_Error.md) | B | boundary | R2 | Prediction error relevant, men ikke universel biomarkør for destabilisering |
| [Sevenster 2014](../../07_STUDIES/VERIFIED/2014_Sevenster_PE_Retrieval_Reconsolidation_New_Learning.md) | B | boundary | R2 | Foreslog overgang retrieval → reconsolidation → new learning afhængigt af PE |
| [Wood 2015](../../07_STUDIES/VERIFIED/2015_Wood_Negative_Reconsolidation.md) | A | negativ | R2 | Tre små kliniske PTSD-forsøg uden forventet effekt; vigtige modfund, men små samples |
| [Brunet 2018](../../07_STUDIES/VERIFIED/2018_Brunet_Propranolol_Reactivation_RCT.md) | A | positiv | R2 | Kontrolleret klinisk signal; mekanismen er ikke isoleret fra øvrige treatment/retrieval-effekter |
| [Chalkia 2020](../../07_STUDIES/VERIFIED/2020_Chalkia_Retrieval_Extinction_Replication.md) | B | negativ replikation | R3 | Registreret direkte replikation fandt ingen retrieval-extinction-fordel |
| [Bos 2019](../../07_STUDIES/VERIFIED/2019_Bos_Acute_Not_Permanent_Propranolol.md) | B | negativ/null | R2 | Ingen varig post-reactivation propranolol-effekt; akut performance-effekt skal adskilles fra memory change |
| [Roullet 2021](../../07_STUDIES/VERIFIED/2021_Roullet_Propranolol_Placebo.md) | A | blandet/negativ samlet | R3 | Større klinisk RCT fandt ikke samlet propranololfordel; begrænser Brunet-generalisation |
| [Stemerding 2022](../../07_STUDIES/VERIFIED/2022_Stemerding_Boundary_Replication_Failure.md) | B | negativ replikation | R3 | Kunne ikke reproducere det præcise single-PE boundary-mønster |
| [Gerlicher 2022](../../07_STUDIES/VERIFIED/2022_Gerlicher_PE_Reconsolidation_Null.md) | B | negativ replikation | R3 | Ingen propranolol-disruption efter value-, identity- eller no-PE; begrænser simple PE-regler |
| Propranolol-metaanalyser 2022 | review | konflikt | R3 | Meta-analyser når forskellige konklusioner pga. inklusion/outcomes; ingen R4-konvergens |

**Nuværende reconsolidation-konklusion:** reconsolidation som biologisk memory-proces har et stærkt præklinisk fundament, men specifikke humane procedurer til pålideligt at åbne og manipulere et reconsolidation-vindue har ikke R4-robusthed. Kliniske symptomændringer må ikke bruges som direkte mekanismebevis.

## Hvad den samlede litteratur ændrer i modellen
- Akut ro, indlæring, konsolidering, genkaldelse og klinisk funktion er forskellige mål.
- Butyrat har et afgrænset positivt humant laboratoriefund; hverken PTSD-effekt eller central HDAC-mediation følger automatisk.
- L-DOPA, oxytocin, DCS, hydrokortison, CBD og hormontilførsel har betingede eller modstridende resultater.
- Motion og søvn har relevante humane fund, men ingen enkelt biomarkør forklarer nødvendigvis effekten.
- FAAH/anandamid, døgnrytme og metabolisk tilstand er direkte humane forskningsspor; klinisk overførsel kræver egne data.
- Lurasidon, GLP-1, mitokondrier, laktat og receptorhypoteser skal vurderes på deres faktiske forsøgsniveau.
- HDAC-subtyper kan have forskellige funktioner: HDAC2- og HDAC4-fund må ikke reduceres til én generel "HDAC-hæmning = mere plasticitet"-regel.
- Lavertu-Jolin 2023 gør HDAC2-sporet celletypespecifikt og direkte relevant for præklinisk fear extinction: PV+-interneuroner, Acan/aggrecan og perineuronale net er koblet til senere return of fear i voksne mus.
- Cao 2024 viser, at SerBut-formuleringen kan øge systemisk og CNS-relateret butyrateksponering i mus; dette må ikke overføres direkte til humant natriumbutyrat eller fortolkes som dokumenteret HDAC2-målaktivering.
- Klinisk symptomlettelse med et præparat er ikke automatisk dokumenteret forbedret udslukning.
- [Klinisk rekonsolidering](../../03_EXTINCTION/CLINICAL_PTSD_RECONSOLIDATION.md) rummer både positive og negative forsøg.

De tidligere »systemligninger« læses som begrebslister: læringsindhold, timing, neuromodulation, hormoner, immuntilstand, energi, søvn og kontekst kan samvirke. De er ikke validerede multiplicative modeller eller grundlag for at beregne en personlig stofkombination.

## Alle studiekort
Antallet af kort er ikke antallet af uafhængige forsøg. Ét kort kan rumme flere publikationer, og flere kort kan beskrive samme studie.

| Studiekort | Registreret område |
|---|---|
| [Epigenetik, frygtudslukning og PTSD](../../07_STUDIES/MECHANISTIC/2012_2026_Epigenetics_FKBP5_COMT_HDAC_Extinction.md) | Mekanismer |
| [Mitokondrier og energistofskifte](../../07_STUDIES/MECHANISTIC/2016_2026_Mitochondria_Energy_Metabolism_PTSD_Extinction.md) | Mekanismer |
| [Kusek 2021 — 5-HT7 og hæmmende input](../../07_STUDIES/MECHANISTIC/2021_Kusek_5HT7_Inhibition.md) | Mekanismer |
| [Amisulprid: D2/D3-belægning og lavdosishypotesen](../../07_STUDIES/MECHANISTIC/AMISULPRIDE_D2D3_OCCUPANCY.md) | Mekanismer |
| [Laktat, motion og frygtudslukning](../../07_STUDIES/MECHANISTIC/Lactate_BDNF_Extinction_Audit.md) | Mekanismer |
| [Kilder til mekanismekortet](../../07_STUDIES/MECHANISTIC/MECHANISM_SOURCE_INDEX.md) | Mekanismer |
| [Mitokondrier, laktat og BDNF: kritisk vurdering](../../07_STUDIES/MECHANISTIC/Mitochondria_Lactate_BDNF_Extinction_Audit.md) | Mekanismer |
| [Nader 2000 — genkaldelse og restabilisering](../../07_STUDIES/PRECLINICAL/2000_Nader_Reconsolidation.md) | Prækliniske studier |
| [Bredy 2007 — HDAC, BDNF og udslukning](../../07_STUDIES/PRECLINICAL/2007_Bredy_HDAC_BDNF.md) | Prækliniske studier |
| [Guan 2009 — HDAC2, synaptisk plasticitet og hukommelse](../../07_STUDIES/PRECLINICAL/2009_Guan_HDAC2_Plasticity.md) | Prækliniske studier |
| [Peters 2010 — lokal BDNF og frygt](../../07_STUDIES/PRECLINICAL/2010_Peters_BDNF.md) | Prækliniske studier |
| [Kim 2012 — HDAC4, LTP og hukommelse](../../07_STUDIES/PRECLINICAL/2012_Kim_HDAC4_Plasticity.md) | Prækliniske studier |
| [Luoni 2013: kronisk lurasidon i en rottemodel](../../07_STUDIES/PRECLINICAL/2013_Luoni_Lurasidone.md) | Prækliniske studier |
| [Salinas-Hernández 2018 — uventet udeblivelse af fare](../../07_STUDIES/PRECLINICAL/2018_Salinas_Dopamine_Omission.md) | Prækliniske studier |
| [de Assis Brasil 2019: lokal 5-HT7-blokade og udslukning](../../07_STUDIES/PRECLINICAL/2019_5HT7_BLA_extinction.md) | Prækliniske studier |
| [Lavertu-Jolin 2023 — HDAC2, Acan/PNN og return of fear](../../07_STUDIES/PRECLINICAL/2023_Lavertu_Jolin_HDAC2_Acan_PNN_Extinction.md) | Prækliniske studier |
| [Cao 2024 — SerBut, oral bioavailability og CNS-eksponering](../../07_STUDIES/PRECLINICAL/2024_Cao_SerBut_Bioavailability_Neuroinflammation.md) | Prækliniske studier |
| [Psilocybin, 5-HT2A og frygtudslukning](../../07_STUDIES/PRECLINICAL/2024_Psilocybin_5HT2A_Fear_Extinction.md) | Prækliniske studier |
| [Zhang 2025 — dopamins retning afhænger af kredsløbet](../../07_STUDIES/PRECLINICAL/2025_Zhang_Dopamine_Circuits.md) | Prækliniske studier |
| [GLP-1: kritisk vurdering af PTSD- og læringsevidens](../../07_STUDIES/PRECLINICAL/2026_GLP1_Liraglutide_PTSD_Audit.md) | Prækliniske studier |
| [Liraglutid i en PTSD-lignende musemodel](../../07_STUDIES/PRECLINICAL/2026_GLP1_Liraglutide_PTSD_Model.md) | Prækliniske studier |
| [Haaker 2014: genaktivering og tilbagevendende frygt](../../07_STUDIES/REVIEWS/2014_Haaker_Human_Reinstatement.md) | Litteraturoversigter |
| [Propranolol: modstridende metaanalyser fra 2022](../../07_STUDIES/REVIEWS/2022_Propranolol_Reconsolidation_Conflicting_MetaAnalyses.md) | Litteraturoversigter |
| [Farmakologisk forbedring af frygtudslukning: oversigt fra 2026](../../07_STUDIES/REVIEWS/2026_Pharmacological_Enhancement_of_Fear_Extinction.md) | Litteraturoversigter |
| [Eksponering for kropslige fornemmelser ved PTSD](../../07_STUDIES/VERIFIED/2005_2007_2010_Interoceptive_Exposure_PTSD.md) | Humane/kliniske studier |
| [Testosteron: akut frygt og varig læring](../../07_STUDIES/VERIFIED/2005_2018_Testosterone_Human_Fear_Audit.md) | Humane/kliniske studier |
| [Guanfacin ved kronisk PTSD: to negative forsøg](../../07_STUDIES/VERIFIED/2006_2008_Guanfacine_PTSD_RCTs.md) | Humane/kliniske studier |
| [Brunet 2008: propranolol efter genkaldelse](../../07_STUDIES/VERIFIED/2008_Brunet_Propranolol_Physiology.md) | Humane/kliniske studier |
| [Kindt 2009: propranolol og human fear reconsolidation](../../07_STUDIES/VERIFIED/2009_Kindt_Propranolol_Human_Fear_Reconsolidation.md) | Humane/kliniske studier |
| [Schiller 2010 — genkaldelse før udslukning](../../07_STUDIES/VERIFIED/2010_Schiller_Retrieval_Extinction.md) | Humane/kliniske studier |
| [Sevenster 2012 — retrieval alene er ikke nok](../../07_STUDIES/VERIFIED/2012_Sevenster_Retrieval_Not_Sufficient.md) | Humane/kliniske studier |
| [Endocannabinoider: CB1-genetik og FAAH-hæmning](../../07_STUDIES/VERIFIED/2012_2019_Endocannabinoid_CB1_FAAH_Human_Extinction.md) | Humane/kliniske studier |
| [Østradiol, progesteron og PTSD-læring](../../07_STUDIES/VERIFIED/2012_2023_Estradiol_Progesterone_PTSD_Extinction.md) | Humane/kliniske studier |
| [Naturlige hormonniveauer og akut hormontilførsel](../../07_STUDIES/VERIFIED/2012_2024_Estradiol_Progesterone_Fear_Extinction.md) | Humane/kliniske studier |
| [CBD: blandede humane lærings- og terapifund](../../07_STUDIES/VERIFIED/2013_2023_CBD_Human_Extinction_Exposure.md) | Humane/kliniske studier |
| [Acheson 2013: oxytocin og senere genkaldelse](../../07_STUDIES/VERIFIED/2013_Acheson_Oxytocin.md) | Humane/kliniske studier |
| [Døgnrytme, testosteron/kortisol og udslukning](../../07_STUDIES/VERIFIED/2013_Circadian_Testosterone_Cortisol_Extinction.md) | Humane/kliniske studier |
| [Felmingham 2013: BDNF-genotype og eksponeringsrespons](../../07_STUDIES/VERIFIED/2013_Felmingham_BDNF_Val66Met_PTSD_exposure.md) | Humane/kliniske studier |
| [Haaker 2013: L-DOPA og kontekstafhængighed](../../07_STUDIES/VERIFIED/2013_Haaker_LDOPA.md) | Humane/kliniske studier |
| [Sevenster 2013 — forudsigelsesfejl som betingelse](../../07_STUDIES/VERIFIED/2013_Sevenster_Prediction_Error.md) | Humane/kliniske studier |
| [Smits 2013: D-cycloserin og sessionens udfald](../../07_STUDIES/VERIFIED/2013_Smits_DCS_session_quality.md) | Humane/kliniske studier |
| [Sevenster 2014 — PE og procesovergang](../../07_STUDIES/VERIFIED/2014_Sevenster_PE_Retrieval_Reconsolidation_New_Learning.md) | Humane/kliniske studier |
| [Ketamin: PTSD-symptomer og læringsmekanismer](../../07_STUDIES/VERIFIED/2014_2026_Ketamine_PTSD_and_Extinction_Audit.md) | Humane/kliniske studier |
| [Hydrokortison ved eksponering: pilot og større forsøg](../../07_STUDIES/VERIFIED/2015_2021_Hydrocortisone_PE_PTSD.md) | Humane/kliniske studier |
| [Motion som tillæg til læring og eksponering](../../07_STUDIES/VERIFIED/2015_2026_Exercise_BDNF_AEA_PTSD_Extinction.md) | Humane/kliniske studier |
| [Wood 2015: tre negative rekonsolideringsforsøg](../../07_STUDIES/VERIFIED/2015_Wood_Negative_Reconsolidation.md) | Humane/kliniske studier |
| [Vagusnervestimulation gennem huden](../../07_STUDIES/VERIFIED/2016_2019_tVNS_Human_Fear_Extinction.md) | Humane/kliniske studier |
| [Søvn, REM og hukommelse for udslukning](../../07_STUDIES/VERIFIED/2016_2026_Sleep_REM_Circadian_Extinction.md) | Humane/kliniske studier |
| [Memantin og associativ udslukningslæring](../../07_STUDIES/VERIFIED/2017_Golisch_Memantine_Extinction.md) | Humane/kliniske studier |
| [Mataix-Cols 2017: DCS og individuelle deltagerdata](../../07_STUDIES/VERIFIED/2017_MataixCols_DCS_IPD_meta.md) | Humane/kliniske studier |
| [Brunet 2018: propranolol før traumegenaktivering](../../07_STUDIES/VERIFIED/2018_Brunet_Propranolol_Reactivation_RCT.md) | Humane/kliniske studier |
| [Faste natten over, ghrelin og frygtudslukning](../../07_STUDIES/VERIFIED/2018_Fasting_Ghrelin_Human_Fear_Extinction.md) | Humane/kliniske studier |
| [Felmingham 2018: BDNF-genotype og eksperimentel PTSD-læring](../../07_STUDIES/VERIFIED/2018_Felmingham_BDNF_Val66Met_fear_extinction_PTSD.md) | Humane/kliniske studier |
| [Gerlicher 2019: L-DOPA og vellykket udslukning](../../07_STUDIES/VERIFIED/2019_Gerlicher_LDOPA.md) | Humane/kliniske studier |
| [PTSD, DNA-methylering og epigenetik](../../07_STUDIES/VERIFIED/2020_2024_PTSD_Epigenome_Evidence.md) | Humane/kliniske studier |
| [Chalkia 2020 — registreret replikation](../../07_STUDIES/VERIFIED/2020_Chalkia_Retrieval_Extinction_Replication.md) | Humane/kliniske studier |
| [Roullet 2021: genaktivering med propranolol eller placebo](../../07_STUDIES/VERIFIED/2021_Roullet_Propranolol_Placebo.md) | Humane/kliniske studier |
| [Stemerding 2022 — mislykket boundary-condition-replikation](../../07_STUDIES/VERIFIED/2022_Stemerding_Boundary_Replication_Failure.md) | Humane/kliniske studier |
| [MDMA og human frygtudslukning](../../07_STUDIES/VERIFIED/2022_MDMA_Human_Fear_Extinction.md) | Humane/kliniske studier |
| [Akut inflammation og kropslig trusselslæring](../../07_STUDIES/VERIFIED/2023_Inflammation_Endotoxin_Interoceptive_Extinction.md) | Humane/kliniske studier |
| [Andres 2024: registreret L-DOPA-replikation](../../07_STUDIES/VERIFIED/2024_Andres_LDOPA_replication.md) | Humane/kliniske studier |
| [Mikroglia og neuroimmun funktion ved PTSD](../../07_STUDIES/VERIFIED/2024_Microglia_Neuroimmune_PTSD.md) | Humane/kliniske studier |
| [Rashidi 2025: oxytocin og forringet udslukning](../../07_STUDIES/VERIFIED/2025_Rashidi_Oxytocin.md) | Humane/kliniske studier |
| [Ribbens 2026: natriumbutyrat og senere genkaldelse](../../07_STUDIES/VERIFIED/2026_Ribbens_NaBu.md) | Humane/kliniske studier |

## Kilder fra den tidligere hovedliste uden selvstændigt studiekort
Disse blev tidligere registreret i hovedlisten. Beskrivelserne nedenfor viderefører den eksisterende vurdering; de er ikke ny fuldtekstkontrol.

| Spor og kilde | Registreret fund eller anvendelse | Begrænsning |
|---|---|---|
| Butyrat i SPS-rotter, PMID 33883448 | Forbedret udslukning og ændrede hippocampale HDAC/acetylkolinesterase-mål | Dyreforsøg |
| HDAC-oversigt, PMID 24646280 | Histonacetylering, BDNF/NMDA og langvarig udslukning | Overvejende præklinisk |
| Haaker 2015, PMID 26238968 | L-DOPA efter udslukning; test efter én uge. Ingen klar hudledningseffekt, men ændret frygtrelateret/vmPFC-aktivitet | Neurale og adfærdsmæssige mål er forskellige |
| Forsøgsparadigme, PMID 24116095 | Multimodal senere genkaldelse og genaktivering ved signal-/kontekstbetingning | Metodekilde |
| Eckstein 2015, PMID 25542304 | 62 raske mænd; oxytocin, dobbeltblindet randomiseret fMRI. Større tidlig hudreaktion og senere fald | Ikke klinisk PTSD |
| Oxytocin og frygtkonsolidering, PMID 31922086 | Relevant kilde til oprindelig frygtindlæring | Ingen detaljeret effektudtrækning i den tidligere liste |
| Norberg 2008, PMID 18313643 | Tidlig DCS-metaanalyse med støtte til lærings-/eksponeringstillæg | Senere studier nuancerer billedet |
| McGuire 2017, PMID 27314661 | 20 forsøg, 957 deltagere med angst/OCD/PTSD; små, generelt ikke-signifikante tillægseffekter | Diagnoser og protokoller varierer |
| DCS og PTSD-moderation, PMID 26121495 | Læring relateret til udfald; ikke konsistent DCS×læringsmoderation | Adskil prognose og interaktion |
| BDNF/TrkB, PMID 21639804, 22530815, 21798604, 31900428, 32845430 | Genetik, kredsløb, amygdala og plasticitet | BDNF er ikke i sig selv en anti-frygt-mekanisme |
| Lurasidonfarmakologi, PMID 20404009, 27722855, 22675261, 27203278 | D2/5-HT2A/5-HT7-antagonisme, delvis 5-HT1A-agonisme og farmakokinetik | Ikke direkte human udslukningsdokumentation |
| Amisulpridfarmakologi, PMID 12404702, 9218165, 8996184, 8996185 | Præ-/postsynaptiske og regionale farmakologiske forskelle | Ikke ækvivalent med L-DOPA eller rent præsynaptisk lavdosisvirkning |
| Brede udslukningsoversigter, PMID 24374101, 24254958 | Farmakologiske/adfærdsmæssige fund og klinisk overførsel | Oversigt, ikke et selvstændigt forsøg |

Originale titler og identifikatorer findes i [kilderegistret](../../07_STUDIES/SOURCE_REGISTER.md). Senere kort og dossierer supplerer hovedlisten, herunder Dalile 2024, receptorgrundlag og nye kliniske rekonsolideringsforsøg.

## Fuld kildebevarelse og videre dækning
[Kilderegistret](../../07_STUDIES/SOURCE_REGISTER.md) indeholder alle tidligere identificerede PMID'er og DOI'er og henvisninger til deres anvendelse. [Dækningsplanen](../COVERAGE_PLAN.md) viser huller i præparater, modeller og teorier. Der hævdes ikke udtømmende dækning af al relevant forskning.

## Skabelon for fremtidige udtræk
Registrér citation, DOI/PMID, art, population, antal randomiserede/analyserede, design, intervention/formulering, forsøgsdosis, timing, kontrol, primært udfald, akutte/senere resultater, tilbagekomstformer, bivirkninger, frafald, effektstørrelse med usikkerhed, forfatternes konklusion, projektets fortolkning, alternative forklaringer og replikationsstatus.

Forsøgsdoser er litteraturmetadata. Negative studier, protokoller og ukontrollerede forsøg slettes ikke; deres status skal fremgå.

## Teorikilder — version 0.7
Disse er teori-/oversigtsartikler og tælles ikke som nye effektforsøg:
- [Foa og Kozak 1986: følelsesmæssig bearbejdning](../../07_STUDIES/THEORY/1986_Foa_Kozak.md) — PMID 2871574.
- [Brewin, Dalgleish og Joseph 1996: dobbeltrepræsentation](../../07_STUDIES/THEORY/1996_Brewin_Dual_Representation.md) — PMID 8888651.
- [Ehlers og Clark 2000: oplevelsen af aktuel trussel](../../07_STUDIES/THEORY/2000_Ehlers_Clark.md) — PMID 10761279.
- [Craske 2014: hæmmende læring ved eksponering](../../07_STUDIES/THEORY/2014_Craske_Inhibitory_Learning.md) — PMID 24864005.

[Samlet teorisammenligning](../../05_MODELS/PTSD_THEORIES.md) · [Søgelog og yderligere spor](../THEORY_SEARCH_LOG.md).

## Empiriske teoriprøver — version 0.8
Tre observationsartikler, ikke randomiserede behandlingsforsøg:

- [Rubin, Boals og Berntsen 2008 — selvbiografisk hukommelse](../../07_STUDIES/VERIFIED/2008_Rubin_Autobiographical_Memory.md)
- [Lancaster, Rodriguez og Weston 2011 — kognitiv model](../../07_STUDIES/VERIFIED/2011_Lancaster_Cognitive_Model.md)
- [Rubin, Dennis og Beckham 2011 — klinisk hukommelsesundersøgelse](../../07_STUDIES/VERIFIED/2011_Rubin_Clinical_Memory.md)

Deltagergrupper og kildekontrol fremgår af hvert kort. Resultaterne indgår i [teorisammenligningen](../../05_MODELS/PTSD_THEORIES.md).

## Præparatudvidelse — version 0.9
- [Dalile 2024 — kolonfrigivet butyrat](../../07_STUDIES/VERIFIED/2024_Dalile_Colonic_Butyrate.md): DOI 10.1016/j.pnpbp.2024.110939; PMID 38199487.
- [Guillen-Burgos 2025 — lurasidon og barndomstraumer](../../07_STUDIES/VERIFIED/2025_Guillen_Burgos_Lurasidone_Trauma.md): DOI 10.1093/ijnp/pyaf020; PMID 40156897.
- [Cisler 2020 — L-DOPA hos kvinder med PTSD](../../07_STUDIES/VERIFIED/2020_Cisler_LDOPA_PTSD.md): DOI 10.1038/s41398-020-00975-3.
- [Eckstein — oxytocin under udslukning](../../07_STUDIES/VERIFIED/2015_Eckstein_Oxytocin.md): DOI 10.1016/j.biopsych.2014.10.015.

Dalile og Guillen-Burgos var tidligere omtalt i dossierer og er nu selvstændige kort; de tælles ikke som nye uafhængige forsøg. Cisler er et laboratorieforsøg i en PTSD-population. Kontrolniveau og åbne spor fremgår af [søgeloggen](../CORE_DRUG_SEARCH_LOG.md).

## Version 0.11: optagelse, central mekanisme og receptorbelægning
- [Boets 2017 — systemisk tilgængelighed af kolonfrigivet butyrat](../../07_STUDIES/MECHANISTIC/2017_Boets_Butyrate_Availability.md): DOI 10.1113/JP272613; PMID 27510655.
- [Wong 2013 — lurasidon og D2-belægning](../../07_STUDIES/MECHANISTIC/2013_Wong_Lurasidone_D2_PET.md): DOI 10.1007/s00213-013-3103-z; PMID 23649882.
- [Mohammadi-Farani 2022 — lokal butyratindgift og BDNF](../../07_STUDIES/PRECLINICAL/2022_Mohammadi_Farani_Local_Butyrate.md): DOI 10.22038/ijbms.2022.65000.14312.

Kortene vedrører forskellige evidensniveauer. [Kontrolstatus](../TRANSLATION_SEARCH_LOG.md).

## Version 0.12: opfølgning på to åbne primærkilder
- [Mohammadi-Farani 2021](../../07_STUDIES/PRECLINICAL/2021_Mohammadi_Farani_Systemic_Butyrate.md): PMID 33883448; DOI 10.1097/FBP.0000000000000633. Præklinisk forsøg.
- [Potkin 2014](../../07_STUDIES/MECHANISTIC/2014_Potkin_Lurasidone_Patient_PET.md): DOI 10.1017/S109285291300059X. Human receptorundersøgelse, online 2013.

Begge var allerede identificerede litteraturspor. Nye kort er ikke nye uafhængige replikationer. Resumé og metadata er kontrolleret; fuld metodevurdering udestår.

## TRE og somatiske interventioner — version 0.13
TRE er registreret som en kropslig/somatisk kandidatintervention, ikke som dokumenteret fear-extinction- eller rekonsolideringsmekanisme.

- [Kent 2018 — kontrolleret TRE-forsøg ved stress/PTSD](../../07_STUDIES/VERIFIED/2018_Kent_TRE_PTSD_Controlled_Trial.md): teknisk slutrapport. TRE-gruppen forbedredes over tid, men PTSD Group × Time var ikke signifikant; rapporten dokumenterer derfor ikke TRE-specifik overlegenhed på PTSD-symptomer.
- [Lynning et al. 2021 — TRE ved MS, pilot](../../07_STUDIES/VERIFIED/2021_Lynning_TRE_MS_Pilot.md): n=9, enkeltgruppe; positive selvrapporterede signaler, men ingen kontrolgruppe og ikke PTSD.
- [Parker et al. 2024 — TRE hos østafrikanske flygtninge](../../07_STUDIES/VERIFIED/2024_Parker_TRE_Refugees.md): positivt traumesymptomsignal mod delayed-treatment/control; kræver uafhængig replikation.
- [Skovgaard et al. 2025 — TRE ved MS, RCT](../../07_STUDIES/VERIFIED/2025_Skovgaard_TRE_MS_RCT.md): n=28; ujusteret primæranalyse ikke signifikant, justeret MFIS-total signifikant; ikke PTSD-population.
- [Roos, van Niekerk & Tönsing 2026 — TRE scoping review](../../07_STUDIES/REVIEWS/2026_Roos_TRE_Scoping_Review.md): 22 studier/24 rapporter; lovende signaler, men heterogen og ofte metodisk svag litteratur.

- [Berceli et al. 2014 — TRE/SUTT caregiver-pilot](../../07_STUDIES/VERIFIED/2014_Berceli_TRE_Caregivers_Pilot.md): n=21 gennemførere; ukontrolleret 10-ugers feasibility/QoL-signal; PMID 25568824.
- [Johnson & Naidoo 2017 — lærer-stress og burnout](../../07_STUDIES/VERIFIED/2017_Johnson_Naidoo_TRE_Teacher_Stress.md): mixed-method pilot med TRE-relateret kropslig coping; ikke et rent TRE-RCT.
- [Thommessen & Fougner 2020 — dramastuderende](../../07_STUDIES/VERIFIED/2020_Thommessen_Fougner_TRE_Drama_Students.md): kvalitativt case-studie, n=12; kropsbevidsthed og oplevet funktion.
- [Oh & Shin 2021 — akut state anxiety](../../07_STUDIES/VERIFIED/2021_Oh_Shin_TRE_Anxiety_Pilot.md): n=25, ukontrolleret før/efter-pilot; akut angstsignal, ikke langtidseffekt.

Samlet fortolkning og mekanismehypoteser: [TRE-forskningsdossier](../../03_EXTINCTION/TRE_DOSSIER.md).

### TRE-protokol uden effektresultater
- [Zhao et al. 2024 — TRE ved emotionelle lidelser hos unge](../../07_STUDIES/PROTOCOLS/2024_Zhao_TRE_Adolescent_RCT_Protocol.md): RCT-protokol, 140 mor–unge-par, ChiCTR2100044553. Protokollen tælles ikke som positiv eller negativ effekt-evidens.
- [Samlet TRE-litteraturkort](../../07_STUDIES/TRE_LITERATURE_MAP.md) bevarer 2023-korpus, nyere kilder og grå litteratur med kontrolstatus.

## Kvalitativ forskning om coping, kontekst og resiliens — version 0.15
- [Harnisch 2016 — forced resilience, krigserfaringer og vanskelig demobilisering](../../07_STUDIES/QUALITATIVE/2016_Harnisch_Forced_Resilience_PhD.md): ph.d.-afhandling, DPU/Aarhus Universitet, 337 sider. Bruges som kvalitativ/kontekstuel evidens, ikke som behandlingseffektstudie.
- [Harnisch & Montgomery 2017 — avoidant coping efter tvangsrekruttering](../../07_STUDIES/QUALITATIVE/2017_Harnisch_Montgomery_Avoidant_Coping_Uganda.md): 36 tidligere tvangsrekrutterede personer; ca. 10 måneders etnografisk feltarbejde; PMID 28738316; DOI 10.1016/j.socscimed.2017.07.007.

FearPrime-fortolkning: Studierne støtter behovet for at skelne mellem **funktionel, kontekstafhængig coping** og rigid generaliseret undgåelse. De dokumenterer ikke, at “fortrængning” generelt er bedre end evidensbaseret PTSD-behandling.

## Harnisch-sporet — samlet udvidelse, version 0.16
- [Samlet Harnisch-dossier](../../07_STUDIES/QUALITATIVE/HARNISCH_DOSSIER.md)
- [Harnisch & Pfeiffer 2018 — appetitiv aggression](../../07_STUDIES/QUALITATIVE/2018_Harnisch_Pfeiffer_Appetitive_Aggression.md): PMID 29151235; DOI 10.1007/s11013-017-9557-4.
- [Harnisch 2018 — “The Additional Past”](../../07_STUDIES/QUALITATIVE/2018_Harnisch_Additional_Past.md): bogkapitel om demobilisering, tavshed, fortælling og hjemkomst.
- [Harnisch, Montgomery & Knoop 2020 — Forced Resilience](../../07_STUDIES/THEORY/2020_Harnisch_Forced_Resilience.md): DOI 10.1093/acrefore/9780190236557.013.546.
- [Harnisch 2022 — “The Third Time Janus Died”](../../07_STUDIES/QUALITATIVE/2022_Harnisch_Third_Time_Janus_Died.md): DOI 10.1080/13698249.2022.2092687.

Samlet fortolkning: Harnisch-sporet understøtter et funktionelt/kontekstuelt forskningsspørgsmål om coping, resiliens og kontekstskifte. Det er primært kvalitativt/teoretisk og bruges ikke som komparativ behandlingsevidens.

## Integreret adaptiv model — version 0.17
Følgende nyere review-/teorikilder er tilføjet som grundlag for [Adaptive PTSD Model](../../05_MODELS/ADAPTIVE_PTSD_MODEL.md):

- [Coimbra et al. 2023 — tonic immobility og PTSD](../../07_STUDIES/REVIEWS/2023_Coimbra_Tonic_Immobility_PTSD_Meta.md): systematisk review/meta-analyse, PMID 37229971.
- [Putica & Agathos 2024 — predictive processing og CPTSD](../../07_STUDIES/THEORY/2024_Putica_Agathos_CPTSD_Predictive_Processing.md): teori/review, PMID 39084584.
- [Leech et al. 2024 — interoception og PTSD](../../07_STUDIES/REVIEWS/2024_Leech_Interoception_PTSD_Scoping.md): scoping review med 43 inkluderede studier, PMID 38840943.
- [Misitano et al. — dissociativ PTSD-subtype](../../07_STUDIES/REVIEWS/2024_Misitano_Dissociative_PTSD_Subtype.md): systematisk review af latent-profile-studier, PMID 36062756.
- [Chen et al. 2025 — fear-memory update](../../07_STUDIES/REVIEWS/2025_Chen_Fear_Memory_Update.md): nyere review af extinction og reconsolidation, PMID 40205305.
- [Smits et al. 2026 — pharmacological augmentation](../../07_STUDIES/REVIEWS/2026_Smits_Pharmacological_Augmentation_Extinction.md): kritisk translationelt review, PMID 41349549.

Disse kilder dækker forskellige forklaringsniveauer og tælles ikke som seks direkte kliniske effektforsøg.

## Version 0.19: HDAC2/PV/PNN og SerBut
- [Lavertu-Jolin 2023](../../07_STUDIES/PRECLINICAL/2023_Lavertu_Jolin_HDAC2_Acan_PNN_Extinction.md): PMID 37131076; DOI 10.1038/s41380-023-02085-0. Direkte præklinisk fear-extinction/return-of-fear-studie, der forbinder HDAC2 i PV+-interneuroner med Acan/aggrecan, perineuronale net og senere spontan fear recovery.
- [Cao 2024](../../07_STUDIES/PRECLINICAL/2024_Cao_SerBut_Bioavailability_Neuroinflammation.md): PMID 38561491; DOI 10.1038/s41551-024-01190-x. Præklinisk formulering/biodistribution: SerBut øgede systemisk og CNS-relateret butyrateksponering i mus og påvirkede autoimmune/neuroinflammatoriske modeller.

De to kilder må ikke kædes sammen som dokumentation for, at oral natriumbutyrat hos mennesker selektivt rammer HDAC2/PV/PNN-sporet. De udfylder forskellige led i en fortsat uprøvet translationel kæde.

## Version 0.20: neurobiologi og reconsolidation-robusthed
Tre nye mekanismemoduler er tilføjet: [hippocampus/context discrimination](../../02_MECHANISMS/HIPPOCAMPUS_CONTEXT_DISCRIMINATION.md), [insula/interoception](../../02_MECHANISMS/INSULA_INTEROCEPTION.md) og [HPA/stress-memory](../../02_MECHANISMS/HPA_STRESS_MEMORY.md).

Reconsolidation-sporet har nu individuelle kort for Kindt 2009, Sevenster 2012, Sevenster 2014 og Stemerding 2022 samt den claim-specifikke R0–R4-matrix ovenfor. Den vigtigste ændring er, at negative replikationer tælles som evidens om robusthed i stedet for at blive forklaret væk som fravær af effekt.

## Version 0.23: reconsolidation update-search og kvantitativ P2-udtrækning

### Nye humane laboratorie-/review-kilder
- [Chen et al. 2025 — kvantificeret prediction error](../../07_STUDIES/VERIFIED/2025_Chen_Quantified_Prediction_Error_Reconsolidation.md): PMID 40570716; DOI 10.1016/j.cognition.2025.106224. **B, R2, M2**. PE behandles som gradueret/modelafhængig moderator, ikke som universel binær destabiliseringsmarkør.
- [Paul & Asthana 2025 — memory strength × prediction error](../../07_STUDIES/VERIFIED/2025_Paul_Memory_Strength_PE_Retrieval_Extinction.md): PMID 40653191; DOI 10.1016/j.neuroscience.2025.07.014. **B, R1–R2, M2** indtil fuld RoB/effect extraction. Ikke klinisk PTSD-evidens.
- [Li et al. 2025 — propranolol/PTSD meta-analyse](../../07_STUDIES/REVIEWS/2025_Li_Propranolol_PTSD_Meta.md): PMID 39944616; DOI 10.3389/fphar.2025.1545493. Positiv bred symptom-meta, men bredere spørgsmål end reconsolidation og i konflikt med 2022-sporet.
- [Xia et al. 2026 — systematisk review af farmakologi og human aversiv hukommelse](../../07_STUDIES/REVIEWS/2026_Xia_Pharmacological_Human_Aversive_Memory.md): PMID 41513054; DOI 10.1016/j.neubiorev.2026.106548. R3 for bred human laboratoriekonvergens omkring propranolol/reconsolidation; **ikke klinisk PTSD R4**.

### Effect-size/RoB-opdatering
[data/effects.csv](../../data/effects.csv) rummer nu:
- Brunet 2018: mellemgruppe CAPS-estimat 11.50 og FearPrime-beregnet normal-approksimeret 95% CI 1.23–21.77; PCL-S-estimat 14.58, beregnet 95% CI 8.11–21.05.
- Roullet 2021: samlet treatment partial η² ≈ 0.0048, treatment×session partial η² ≈ 0.0297; 3-måneders raw mean difference +3.68 med beregnet 95% CI −7.20 til 14.56.
- Wood 2015: `not_derivable_from_verified_data`; manglende summary-data bliver ikke udfyldt ved gæt.
- Schiller 2010 verification: group×time partial η² ≈ 0.07, p=.091; reanalyse af originaldata, ikke ny sample.
- Chalkia 2020: negativ preregistreret replikation bevaret; observeret standardiseret effect/CI markeres endnu som `not_extracted`.

Alle FearPrime-beregnede CI'er/effekter er markeret som beregnede og må ikke forveksles med originalartiklens rapporterede CI'er.

### Aktuel fortolkning
Nyere boundary-data gør PE/memory strength-modellen mere nuanceret, men **ophæver ikke** Chalkia- og Stemerding-type replication failures. Klinisk propranolol for PTSD forbliver et konfliktfyldt evidensspor, mens human laboratorieevidens for aversiv-memory reconsolidation er stærkere end den kliniske translation.
## Version 0.24: screening/export og claim-level certainty

- 30 PubMed-indekserede records er samlet i et verificeret export-set og screenet med inclusion/exclusion + dedup/sample-overlap status.
- Dette er **ikke** PubMeds totale search hit count; native ESearch/bulk export var ikke tilgængeligt i den aktuelle retrievalflade.
- [Certainty framework](../CERTAINTY_FRAMEWORK.md) holder certainty adskilt fra R0–R4 og M0–M4.
- [Reconsolidation certainty profile](../RECONSOLIDATION_CERTAINTY_PROFILE.md) giver de første claim-level vurderinger.

Foreløbig profil:
- human propranolol/reconsolidation laboratory effect: **MODERATE**
- clinical PTSD propranolol superiority: **LOW**
- reliable retrieval-extinction prevention of return of fear: **LOW**
- prediction error as relevant moderator: **LOW**
- universal single-PE trigger claim: **VERY LOW**
- memory-strength moderation: **VERY LOW**
- symptom improvement as proof of reconsolidation mechanism: **VERY LOW**

Disse er GRADE-informerede FearPrime-ratings og ikke formel GRADE.
## Version 0.25: candidate certainty + nightmare/interoception-spor

### Candidate certainty
[Candidate certainty profile](../CANDIDATE_CERTAINTY_PROFILE.md) udvider claim-level certainty fra reconsolidation til:
- DCS
- FAAH/CB1
- butyrat
- L-DOPA
- oxytocin
- lurasidon.

Maskinlæsbare ratings ligger i [data/certainty.csv](../../data/certainty.csv).

### Vigtige nye translations-/modfund
- [Mayo 2025 FAAH PTSD RCT](../../07_STUDIES/VERIFIED/2025_Mayo_FAAH_PTSD_CBT_RCT.md): AEA target engagement uden ekstra CAPS-5/sekundær clinical benefit over CBT.
- [2025 cannabis/sleep meta](../../07_STUDIES/REVIEWS/2025_Cannabis_Sleep_Architecture_Meta.md): ingen konsistent simpel THC→REM-suppression-regel; withdrawal/sleep disturbance mere konsistent.
- [2026 cannabis/PTSD scoping review](../../07_STUDIES/REVIEWS/2026_Cannabis_PTSD_Scoping_Review.md): nabilone nightmare-signal, men almindelig cannabis/THC ikke stabilt superior på PTSD.
- [Jamison respiratory RCT](../../07_STUDIES/VERIFIED/2022_Jamison_Respiratory_Training_PTSD.md): respiratory-rate ændring uden signifikant PTSD-hyperarousal benefit.

### Nye hypoteser
- [PTSD nightmare + THC/cannabinoider + butyrat + drømmearbejde](../../05_MODELS/PTSD_NIGHTMARE_THC_BUTYRATE_HYPOTHESIS.md).
- [Butyrat → interoceptiv challenge → L-DOPA/oxytocin](../../05_MODELS/INTEROCEPTIVE_BUTYRATE_LDOPA_OXYTOCIN_HYPOTHESIS.md).

Begge er eksplicit hypotesegenererende og må ikke læses som personlige doserings-/selvforsøgsprotokoller.
## Version 0.26: operationalisering af nightmare- og interoception-hypoteser

### Nightmare Measurement Engine
- [Nightmare Measurement Engine](../../06_MEASUREMENT/NIGHTMARE_MEASUREMENT_ENGINE.md) adskiller nightmare burden, dream recall, sleep continuity, content, next-day state og later learning/function.
- [nightmare_schema.yaml](../../data/nightmare_schema.yaml) og [nightmare_log_template.csv](../../data/nightmare_log_template.csv) er maskinlæsbare tomme skabeloner.

### Interoceptiv factorial preregistration
- [Interoceptiv augmentation preregistration](../INTEROCEPTIVE_AUGMENTATION_PREREGISTRATION.md) formaliserer H0/H1, 2×2 butyrat × dopaminerg faktorstruktur, delayed recall, generalization, falsifikation og stopping rules.
- Oxytocin behandles som separat Stage C frem for automatisk tredje faktor.
- [interoceptive_factorial_schema.yaml](../../data/interoceptive_factorial_schema.yaml) og [interoceptive_trial_template.csv](../../data/interoceptive_trial_template.csv) gør designet maskinlæsbar.

Dette er **research-design infrastructure**, ikke ny efficacy-evidens.
