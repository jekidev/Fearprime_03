# Klinisk adfærdsevidens ved PTSD — studieoversigt

## Formål og afgrænsning

Denne oversigt samler kliniske humanstudier og systematiske synteser, som hjælper med at skelne mellem dokumenterede behandlingsoutcomes og hypoteser om adfærdsmæssige læringsprocesser. Den er ikke en selvstændig behandlingsprotokol eller en komplet systematisk review.

**Hovedregel:** evidens for et manualiseret behandlingsforløb beviser ikke automatisk, at en bestemt komponent — eksempelvis expectancy violation, eksponering uden sikkerhedsadfærd eller fald i angst under en session — er den aktive årsag til forbedring.

## Studievis oversigt

| Kilde | Design og population | Resultat relevant for adfærd | Begrænsning / evidensfortolkning |
|---|---|---|---|
| Schnurr et al. (2022), [PE vs CPT](../07_STUDIES/VERIFIED/2022_Schnurr_PE_CPT_Multisite_RCT.md) | Multisite RCT; 916 amerikanske veteraner med militærrelateret PTSD; 10–14 individuelle sessioner | Begge grupper forbedredes. PE havde større gennemsnitlig CAPS-5-forbedring end CPT, men forskellen (2,42 point; 95% CI 0,53–4,31) lå under den prædefinerede kliniske betydningstærskel. Frafald var højere ved PE (55,8%) end CPT (46,6%). | Aktiv sammenligning uden ubehandlet kontrol. Klinisk effekt af hele terapierne; mekanismen er ikke isoleret. |
| Kooistra et al. (2025), [forventningsbrud i en eksponeringssession](../07_STUDIES/VERIFIED/2025_Kooistra_Expectancy_Violation_Exposure_PTSD.md) | Randomiseret forsøg; 60 behandlingssøgende voksne med PTSD; én 90-minutters eksponeringssession, med eller uden eksplicit fokus på forventningsbrud | Begge betingelser viste gennemsnitlig forbedring ved én uges opfølgning; eksplicit fremhævelse af forventningsbrud gav ikke bedre udfald end sammenligningsbetingelsen. | Lille studie, enkelt session og kort opfølgning. Tester ikke effekten af et fuldt PE/CPT-forløb eller om eksponering som behandlingsklasse virker. |
| Yunitri et al. (2023), [netværksmetaanalyse](https://doi.org/10.1017/S0033291722003737) | 98 RCT'er, 5.567 deltagere; søgning i seks databaser til marts 2021 | Flere terapier, herunder CPT, EMDR, PE, kognitiv terapi, NET og PCT, var forbundet med lavere PTSD-symptomer efter behandling. | Evidenssikkerhed varierede fra meget lav til høj. Netværksrangeringer afhænger af sammenlignelighed på tværs af studier; søgningen er ikke ajour efter marts 2021. |
| Wright et al. (2024), [EMDR versus andre terapier, IPD-metaanalyse](https://doi.org/10.1017/S0033291723003446) | Systematisk review fandt 15 RCT'er; 8 bidrog med individuelle deltagerdata (346 deltagere) | Ingen signifikant forskel mellem EMDR og de inkluderede psykologiske terapier for symptomsværhedsgrad, respons, remission eller frafald. | Lille IPD-undergruppe suhteutettuna 15 relevante forsøg; abstractets betaestimater mangler 95 %-konfidensintervaller. Ikke evidens for ækvivalens. |

## RoB-screening: Schnurr et al. (2022)

Foreløbig, domænebaseret screening er udført ud fra rapporten og registreret i `data/risk_of_bias.csv`. Den erstatter ikke en fuld RoB 2-vurdering.

| Domæne | Vurdering | Hvad begrunder vurderingen |
|---|---|---|
| Randomiseringsproces | LOW | Central computer-genereret randomisering inden for sites. |
| Allokering skjult | UNCLEAR | Ikke verificeret tilstrækkeligt i denne extraction. |
| Blinding af deltagere/behandlere | HIGH | Kan ikke blindes for modtagelse/levering af psykoterapi. |
| Outcome-bedømmer | LOW | Central maskering af CAPS-5 outcome-bedømmelsen. |
| Manglende outcome-data | SOME | Betydeligt behandlingsfrafald; højere i PE end CPT. |
| Outcome-måling | SOME | Klinikerbedømt primært mål med maskering, men sekundære selvrapporter kan påvirkes af forventninger. |
| Selektiv rapportering / fleksibilitet | SOME | Registrering og prespecificerede hypoteser er beskrevet; fuld protokol-versus-rapport-audit mangler. |
| Samlet | SOME | Stor RCT og maskeret primært outcome styrker evidensen; ublindbar terapi, frafald og resterende audit-usikkerhed begrænser den. |

## Hvad adfærdssporet kan konkludere

1. Traumefokuserede, strukturerede terapiforløb har kliniske symptomoutcomes, som anbefales i større retningslinjer. Det er evidens for behandlingsforløbene.
2. Tilnærmelse, undgåelse, funktion, gennemførlighed og forventninger kan registreres som særskilte mål. De er nyttige for at beskrive proces og hverdagsændring.
3. Nærvær af en foreslået proces sammen med behandlingsgevinst dokumenterer ikke, at processen forårsagede gevinsten. Mekanismeclaims kræver design, der tester mediation eller komponenter med passende sammenligning.
4. Ikke-signifikant forskel mellem aktive terapier betyder ikke, at de er ækvivalente.
5. Den næste evidensopgave er at udtrække RCT'ernes præspecificerede funktion-/undgåelsesoutcomes og følge dem over tid. Resultater skal knyttes til sample-ID, så reanalyser ikke tælles som nye kohorter.

## Kilder

- VA/DoD. (2023). [PTSD Clinical Practice Guideline](https://www.healthquality.va.gov/guidelines/MH/ptsd/).
- Schnurr, P. P. et al. (2022). [PE vs CPT RCT](https://doi.org/10.1001/jamanetworkopen.2021.36921). JAMA Network Open, 5(1), e2136921. PMID: 35044471.
- Schnurr, P. P. et al. (2024). [Session-level symptom analysis](https://pubmed.ncbi.nlm.nih.gov/38546622/). Reanalysis of the same parent RCT cohort; not an independent sample.
- Kooistra, M. J. et al. (2025). [Expectancy violation and exposure outcomes](https://doi.org/10.1080/20008066.2024.2447183). European Journal of Psychotraumatology, 16(1), 2447183. PMID: 39773369.
- Yunitri, N. et al. (2023). [Network meta-analysis](https://doi.org/10.1017/S0033291722003737). Psychological Medicine, 53(13), 6376–6388. PMID: 36628572.
- Wright, S. L. et al. (2024). [EMDR individual participant data meta-analysis](https://doi.org/10.1017/S0033291723003446). Psychological Medicine, 54(8), 1580–1588. PMID: 38173121.
