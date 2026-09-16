# FP-BL-01 — test- og analyseplan
Version 0.10 · 2026-09-16 · Projektforslag, ikke et valideret forsøgsprogram.

## Det præcise spørgsmål
Giver butyrat en relevant ekstra forsinket læringsgevinst under stabil lurasidonbehandling? Dette kan undersøges som tillægseffekt. Synergi kræver yderligere sammenligningsgrupper. Se [hypotesen](../04_CANDIDATES/BUTYRATE_LATUDA_HYPOTHESIS.md).

## To forskellige forskningsdesign
| Design | Sammenligning | Kan konkludere | Kan ikke alene konkludere |
|---|---|---|---|
| Randomiseret tillæg | Butyrat versus placebo under stabil lurasidon, samme planlagte træning | Gennemsnitlig tillægseffekt i den inkluderede population | At lurasidon er nødvendigt for effekten |
| Randomiseret 2×2-design | Ingen stofkomponent, butyrat, lurasidon, begge; samme planlagte træning | Stofeffekter og interaktion på valgt skala | Molekylær årsag eller effekt i alle PTSD-grupper |

Det faktorielle design forudsætter, at begge behandlingstildelinger er klinisk passende i målpopulationen. Det er ikke en instruktion om at afbryde eksisterende behandling. Gentagen læring har overførsel; et simpelt skifteforsøg kan ikke antage, at første læringsperiode er slettet.

## Mål og tidspunkter — foreslåede valg
| Tidspunkt | Mål | Formål |
|---|---|---|
| Før træning | Udgangsniveau for trusselsforventning, funktion og symptomer | Beskriv population og prædefinerede kovariater |
| Under træning | Forventning, faktisk udfald, opgaveudførelse og træningsmængde | Dokumentér læringshændelsen |
| Samme dag | Ubehag, vågenhed, bevægetrang og kvalme som separate mål | Adskil aktivering, tolerabilitet og læring |
| Efter 24 timer | Tidlig fastholdelse, sekundært | Undersøg tidsforløb |
| Efter syv dage | Ét prædefineret forsinket læringsmål, primært | Test den afgrænsede fastholdelseshypotese |
| Efter syv dage i ny kontekst | Observerbar handling, sekundært | Test generalisering |
| Efter fire uger | Funktion og passende valideret symptomskala, sekundært | Undersøg klinisk relevans og holdbarhed |

Tidspunkterne er projektvalg, ikke påvist optimale intervaller. En mulig laboratorieoperationalisering er differentiel forventning om ubehag ved de første testpræsentationer; antal præsentationer, retning og aggregering fastlægges før data ses. Senere testpræsentationer kan allerede indeholde ny læring.

Projektets egne 0–10-felter er observationsfelter, ikke validerede kliniske skalaer. Symptommål følger [måleplanen](MEASUREMENT_PLAN.md). Fysiologi analyseres separat; lav hudledning er ikke nødvendigvis bedre trusselsdiskrimination.

## Hvad tæller som synergi?
Lad Y være et udfald vendt, så højere værdi betyder større gevinst. Lad μ00, μ10, μ01 og μ11 være de estimerede gruppemiddelværdier for henholdsvis ingen stofkomponent, butyrat alene, lurasidon alene og begge.

**Interaktionskontrast: I = μ11 − μ10 − μ01 + μ00.**

På denne additive skala betyder I > 0 en mere end additiv effekt. Konfidensinterval, relevant mindstegevinst og den valgte skala skal følge resultatet. Interaktion på én skala er ikke automatisk interaktion på en anden eller molekylær synergi. I tillægsdesignet kan kun μ11 − μ01 estimeres direkte.

## Analyse uden at vælge forklaringen bagefter
- Definér primært udfald, analysepopulation, relevansgrænse og håndtering af manglende data før forsøgsstart.
- Estimér den randomiserede totale effekt efter tildeling; begrund model og eventuel justering for udgangsniveau.
- Træningsmængde, døsighed og sessionens slutniveau kan selv være påvirket af behandlingen. Justér ikke automatisk for dem i hovedanalysen: det kan fjerne en reel virkningsvej eller indføre selektionsbias.
- En analyse blandt dem, der gennemførte træningen eller opnåede lav slut-frygt, er derfor ikke lig den randomiserede hovedeffekt.
- Undersøg mediation særskilt med tidsrækkefølge og eksplicitte antagelser. En korrelation mellem biomarkør og gevinst er ikke tilstrækkelig.
- Rapportér frafald og manglende målinger pr. gruppe og årsag. Manglende data tælles ikke som nul symptomer eller behandlingssvigt uden begrundelse.
- Prædefinér korrektion eller fortolkningshierarki for sekundære mål. Moderatorer kræver en direkte interaktionstest.
- Beregn stikprøvestørrelse ud fra valgt udfald, forventet variation, relevant effekt og frafald. Et interaktionsforsøg skal dimensioneres til interaktionen; et lille positivt hovedstudie giver ikke et tilstrækkeligt deltagerantal.

## Beslutning efter data
**Støtte:** Reproducerbar, relevant forsinket gevinst med tilstrækkelig præcision og en forståelig profil for funktion og tolerabilitet.

**Svækker:** Præcist fravær af relevant gevinst, vedvarende dårligere funktion eller effekt begrænset til akut præstationsændring.

**Uafklaret:** Brede intervaller, væsentligt frafald, utilstrækkelig læring i kontrolgruppen eller modstridende mål.

Dette er forslag til test af hypotesen. De foreliggende separate stofstudier er ikke data fra dette design.
