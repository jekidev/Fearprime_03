# Butyrat: fra formulering til mulig hjernevirkning
Version 0.20 · 2026-09-17

> **Specialmodul.** Denne fil svarer kun på formulering → eksponering → mulig CNS-bro. Den samlede evidensstatus for butyrat ligger i [BUTYRATE_DOSSIER.md](BUTYRATE_DOSSIER.md); direkte formulering-sammenligning ligger i [BUTYRATE_FORMULATION_HEAD_TO_HEAD.md](BUTYRATE_FORMULATION_HEAD_TO_HEAD.md).

Se også den nye [head-to-head-analyse: natriumbutyrat vs. tributyrin vs. SerBut](BUTYRATE_FORMULATION_HEAD_TO_HEAD.md).

## Hvilket led er faktisk målt?
| Led | Holdepunkt | Åbent spørgsmål |
|---|---|---|
| Frigivelse i tarmen | Kolonlevering i [Boets](../07_STUDIES/MECHANISTIC/2017_Boets_Butyrate_Availability.md) og [Dalile](../07_STUDIES/VERIFIED/2024_Dalile_Colonic_Butyrate.md) | Samme profil for et andet produkt? |
| Systemisk eksponering | NaBut: variabel human eksponering; tributyrin: [human PK](../07_STUDIES/VERIFIED/1998_2003_Tributyrin_Human_PK.md); SerBut: større systemisk eksponering end NaBut i mus | Samme koncentrationskurve omkring en extinction-session? |
| Central eksponering | Frit butyrat: meget lav primat-PET-optagelse; SerBut: målbar hjerne/rygmarv i mus; tributyrin: human PET target-engagement-signal | Hvilken fri intracellulær koncentration opnås i relevante neuroner? |
| Central HDAC/BDNF-påvirkning | [Lokal indgift i rotter](../07_STUDIES/PRECLINICAL/2022_Mohammadi_Farani_Local_Butyrate.md) | Samme påvirkning efter oral human indgift? |
| HDAC1/2/3-potens | [Kilgore 2010](../07_STUDIES/PRECLINICAL/2010_Kilgore_Class_I_HDAC_Selectivity.md): butyrat hæmmer klasse I ved lave µM i rekombinante assays | Opnås relevant fri intracellulær koncentration i human hjerne? |
| HDAC2/PV+/PNN ved extinction | [Lavertu-Jolin 2023](../07_STUDIES/PRECLINICAL/2023_Lavertu_Jolin_HDAC2_Acan_PNN_Extinction.md) viser et direkte HDAC2/PV/Acan/PNN-spor i mus, men med genetisk manipulation/BRD6688 | Rammer oral butyrat dette mål i relevant grad? |
| Forsinket læring | [Ribbens](../07_STUDIES/VERIFIED/2026_Ribbens_NaBu.md) | Replikation og forbindelse til målaktivering |
| Klinisk funktion | Ikke etableret for PTSD | PTSD-resultater og holdbarhed |

Kæden er et kontrolskema, ikke en påvist samlet mekanisme. Adfærdsændring alene identificerer ikke en central molekylær årsag.

## Tre produktbegreber skal holdes adskilt
- **Kemisk form:** natriumbutyrat, andre salte, tributyrin, SerBut og andre prodrugs er forskellige kemiske former.
- **Formulering:** overtræk, matrix, lipid/prodrug og hjælpestoffer kan ændre frigivelse og distribution.
- **Eksponering:** faktisk koncentration over tid skal måles. Samme butyratækvivalent beviser ikke samme plasma-, vævs- eller CNS-eksponering.

Tributyrin kan ikke tildeles samme kliniske eller farmakokinetiske evidens som natriumbutyrat alene ud fra indholdet af butyratgrupper. Tilsvarende kan SerBut-data ikke automatisk flyttes til natriumbutyrat.

## Head-to-head-status
### Natriumbutyrat
**Styrke:** den mest direkte humane FearPrime-adfærdsevidens via Ribbens 2026.

**Svaghed:** central eksponering er ikke direkte målt i Ribbens. [Kim 2013](../07_STUDIES/MECHANISTIC/2013_Kim_Butyrate_PET_Brain_Uptake.md) viste, at mærket frit butyric acid havde meget lav hjerneoptagelse i primater (<0,006 %ID/cc) i et intravenøst PET-paradigme.

### Tributyrin
**Styrke:** dokumenteret human systemisk PK og nu et første humant CNS-target-engagement-signal. [Bohnen 2026](../07_STUDIES/VERIFIED/2026_Bohnen_Tributyrin_PET_Target_Engagement.md) fandt ændret regional [11C]butyrat-PET efter ca. 30 dages oral tributyrin.

**Svaghed:** det var et lille åbent Parkinson-pilotstudie; PET-fortolkningen er indirekte, og der blev ikke målt HDAC2 eller extinction.

### SerBut
**Styrke:** [Cao 2024](../07_STUDIES/PRECLINICAL/2024_Cao_SerBut_Bioavailability_Neuroinflammation.md) er den stærkeste direkte prækliniske NaBut-vs-prodrug CNS-biodistributionssammenligning i dette spor. SerBut gav højere systemisk butyrat og målbar butyrat i hjerne/rygmarv tre timer efter indgift, hvor NaBut ikke gav detekterbart signal i de samme CNS-væv ved dette tidspunkt.

**Svaghed:** ingen tilsvarende human PK/CNS/extinction-dokumentation er etableret i den gennemgåede litteratur.

## HDAC: leveringsformen er ikke lig en ny selektiv inhibitor
[Kilgore 2010](../07_STUDIES/PRECLINICAL/2010_Kilgore_Class_I_HDAC_Selectivity.md) målte følgende IC50 for butyric acid:

```text
HDAC3  4,8 µM
HDAC2  7,0 µM
HDAC1  8,3 µM
HDAC8 10,4 µM
HDAC4 ~5725 µM
```

Det er derfor forkert at beskrive butyrat som en **selektiv HDAC2-hæmmer**. Den relevante model er klasse-I-præferent hæmning, hvor HDAC1/2/3/8 alle potentielt kan påvirkes.

Tributyrin og SerBut skal primært ses som **leveringsformer for butyrat**. Cao 2024 viste, at SerBut bevarede HDAC-relateret biologisk aktivitet i celleassay, men ved ækvivalent koncentration var effekten svagere end NaBut og blev fortolket som afhængig af hydrolyse/frigivelse af butyrat. Ingen robust rekombinant HDAC1/2/3-selektivitetsprofil for intakt SerBut eller tributyrin er identificeret i denne gennemgang.

## Cao 2024: SerBut viser, at kemisk levering kan ændre CNS-eksponering
[Cao 2024](../07_STUDIES/PRECLINICAL/2024_Cao_SerBut_Bioavailability_Neuroinflammation.md) udviklede **O-butyryl-L-serine (SerBut)**, en serin-konjugeret butyrat-prodrug. Ideen var at udnytte aminosyretransport og dermed mindske det tab, der normalt følger hurtig håndtering/metabolisme af frit butyrat i tarm og lever.

I mus gav SerBut større systemisk butyrat-tilgængelighed og højere målte butyratniveauer i blandt andet **hjerne og rygmarv**. Det er et vigtigt korrektiv til den tidligere formulering "central eksponering er ukendt": central eksponering er nu **vist præklinisk for denne specifikke prodrug**.

Det ændrer dog ikke den humane FearPrime-bro:

```text
SerBut i mus → målbar CNS-butyrateksponering
        ≠
oral natriumbutyrat hos mennesker → dokumenteret HDAC2-målaktivering i fear-extinction-kredsløb
```

Cao-studiet målte autoimmune/inflammatoriske sygdomsmodeller, ikke fear extinction eller PTSD. Det kan derfor bruges til farmakokinetik/formuleringslogik, ikke som direkte evidens for FearPrime-effekt.

## Tributyrin 2026: første humane CNS-target-engagement-signal
[Bohnen 2026](../07_STUDIES/VERIFIED/2026_Bohnen_Tributyrin_PET_Target_Engagement.md) er et vigtigt nyt led. Efter 500 mg tributyrin tre gange dagligt i omtrent 30 dage ændrede regional [11C]butyrat-PET sig i en lille Parkinson-gruppe. Forfatterne fortolkede lavere radiotracerbinding som konkurrence fra øget ikke-radioaktivt butyrat.

Det gør human CNS-tilgængelighed for tributyrin mere plausibel end før, men det er **ikke** en direkte kemisk måling af neuronal butyratkoncentration og ikke måling af HDAC2-hæmning.

## Massekontrol — kemisk beregning, ikke dosisforslag
For rent vandfrit natriumbutyrat er molmassen cirka 110,09 g/mol; smørsyre cirka 88,11 g/mol. Derfor svarer 1 g salt kemisk til cirka 0,800 g smørsyreækvivalent. Selve butyrat-anionens masse er cirka 0,791 g pr. g salt. Beregningen angiver stofmængde, ikke optagelse.

En etiket med »180 mg smørsyre« kan ikke afklares uden at vide, om tallet angiver syreækvivalent, salt eller blanding. Renhed, vandindhold og hjælpestoffer skal med. Der udledes ikke kapselantal af en uafklaret etiket.

## Hvad ville gøre broen stærkere? — projektets krav
1. Dokumenteret kemisk indhold og frigivelsesprofil.
2. Human plasma-PK for netop formuleringen omkring det relevante læringsvindue.
3. Direkte eller valideret human CNS-eksponering/target engagement.
4. Relevant central målaktivering; samlet butyratniveau er ikke lig HDAC2-target engagement.
5. HDAC1/2/3 skal adskilles, hvis mekanismen hævdes at være subtype-specifik.
6. Tidsmæssig sammenhæng mellem målaktivering og senere læring.
7. Design, der skelner HDAC2/PV/PNN-, BDNF-, immunologiske og andre forklaringer fra hinanden.
8. Replikation med extinction-, return-of-fear- og kliniske funktionsmål.

**Status:** SerBut har den stærkeste direkte prækliniske CNS-formuleringsdemonstration; tributyrin har nu et humant CNS-target-engagement-signal; NaBut har den mest direkte humane extinction-evidens. Ingen form dokumenterer endnu hele kæden til HDAC2/PV/PNN hos mennesker.

## Opfølgning, version 0.12: tidspunktet er en del af mekanismen
[Studiekortet fra 2021](../07_STUDIES/PRECLINICAL/2021_Mohammadi_Farani_Systemic_Butyrate.md) udfylder det tidligere åbne spor. Forbehandling skal registreres særskilt fra indgift omkring udslukning.

**Projektets kontrolregel:** Klassificér hvert forsøg efter, om interventionen kan påvirke oprindelig indlæring, udslukning, konsolidering eller testadfærd. Et forbedret slutmål er ikke alene tilstrækkeligt til at identificere fasen.

## Version 0.20: formulering × CNS × HDAC-subtype
FearPrime skal fremover registrere tre adskilte akser for ethvert butyratstudie:

`formulering/PK × CNS target engagement × HDAC/celletype target engagement`

Et positivt resultat på én akse udfylder ikke automatisk de andre.
