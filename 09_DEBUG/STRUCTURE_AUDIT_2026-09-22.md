# Struktur- og indholdskontrol — 2026-09-22

## Omfang

Ved start blev 291 versionsstyrede tekstfiler scannet for struktur, interne links og relevante tekstmønstre. De centrale navigations- og mekanismedokumenter blev gennemgået redaktionelt. Dette er ikke en ny fuldtekstkontrol af alle studier i biblioteket.

## Fund og rettelser

| Fund | Rettelse |
|---|---|
| 576 fejlende relative links i fem historiske snapshots | Stier er genberegnet fra filernes oprindelige placering til den aktuelle arkivplacering; fagligt indhold og historiske datoer er bevaret |
| Forsiden blandede grundforståelse og avancerede værktøjer | Kort startside, tre læseveje og danske emneindekser |
| Biokemiske begreber var spredt på specialkort | Sammenhængende grundmodul, receptorguide og udvidet ordbog |
| Kredsløbskortet beskrev allerede eksisterende specialkort som fremtidige opgaver | Links og status rettet |
| CSV-kontrollen opdagede ikke forskudte datafelter | Rækkebredde og ugyldige anførselstegn valideres nu |
| To rækker i `data/effects.csv` havde 15 felter under 16 kolonneoverskrifter | Det manglende tomme p-værdifelt er indsat, så retning, justering, kilde og noter ligger i de korrekte kolonner |
| Fire DOI-advarsler | Dokumenteret som gentagne omtaler/aliaser i [overlapregistret](PARTICIPANT_OVERLAP_REGISTER.md); advarsler skjules ikke |
| Strukturkontrollen var kun en CI-rapport | `--strict` aktiveret i arbejdsgangen |

Ingen eksisterende fil er slettet. Studiekort og historik er bevaret. Ændrede tekstfelter angiver ikke nye uafhængige faglige vurderinger.

## Kildekontrol for nye forklaringer

| Kilde | Kontrolleret niveau og anvendelse |
|---|---|
| Ribbens 2026 | Tilgængelig primærartikel; population, læringsbetingelser, udfald og afgrænsning fra central mekanismemåling |
| Guan 2009 | Primærkildens resumé/indekserede artikeltekst; HDAC2, synapser og hukommelse i mus |
| Lavertu-Jolin 2023 | Primærkildens resumé/indekserede artikeltekst; Acan, PV+-celler og senere tilbagekomst af frygt |
| Peters 2010 | Primærtekst/resumé; lokal BDNF, infralimbisk cortex og betinget frygt i rotter |
| Andres 2024 | Tilgængelig primærartikel; negativ replikation af samlet L-DOPA-effekt |
| Kusek 2021 | Primærkildens resumé; 5-HT7 og hæmmende input i muse-amygdala |
| Minichiello 2002 | Resumé; TrkB-koblingssteder og hippocampal LTP |
| Zhou 2007 | Resumé/forlagstekst; Gq-/Gi-signalering i perifere rotteceller |
| Chen 2024 | Tilgængelig artikeltekst/resumé; receptorophobning i umodne dyrkede neuroner |
| IUPHAR/BPS | Indekserede receptorbeskrivelser; fulde databasevisninger krævede login ved opslag |

Kildelinks findes ved de relevante afsnit og på [studiekortene](../07_STUDIES/README.md). Grundlæggende definitioner er undervisningsforklaringer; der er ikke foretaget en systematisk litteratursøgning eller ny fuld risikovurdering af hvert historisk studie.

## Resterende begrænsninger

Den automatiske kontrol validerer lokale linkmål, versioner og CSV-struktur. Den afgør ikke, om et eksternt link stadig er tilgængeligt, om et Markdown-anker eksisterer, om YAML følger skemaet, eller om et forskningsudsagn er korrekt.

Fire kendte DOI-advarsler er gennemgået på dokumentniveau. En fuld kontrol af kohorteoverlap, effektstørrelser, konfidensintervaller og systematiske fejlkilder er stadig uafsluttet. Se [mangellisten](FEARPRIME_V1_GAP_AUDIT.md).
