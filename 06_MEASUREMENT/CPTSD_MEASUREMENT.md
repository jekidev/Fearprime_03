# FearPrime — CPTSD measurement

Version 0.19 · 2026-09-17

## Formål
Dette modul gør CPTSD-sporet målbart uden at blande **PTSD-symptomer**, **disturbances in self-organization (DSO)**, **funktion** og **FearPrime-læringsmål** sammen.

Modulet er et forsknings- og dokumentationslag. Et selvrapporteret spørgeskema er ikke i sig selv en klinisk diagnose.

Se også:
- [CPTSD-modellen](../05_MODELS/CPTSD_MODEL.md)
- [Måleplanen](MEASUREMENT_PLAN.md)
- [Learning metrics](LEARNING_METRICS.md)
- [Adaptiv PTSD-model](../05_MODELS/ADAPTIVE_PTSD_MODEL.md)

---

## 1. Primært instrument: International Trauma Questionnaire (ITQ)

ITQ er udviklet som et kort selvrapporteringsmål for ICD-11 PTSD og kompleks PTSD (CPTSD).

FearPrime bruger **ikke kopierede spørgsmålstekster** i repoet. Brug altid den autoriserede/aktuelle version af instrumentet og den tilhørende scoringvejledning.

### Kerneopdeling

ITQ operationaliserer to overordnede symptomdomæner:

### PTSD
Tre klynger:
1. re-experiencing i nutiden,
2. avoidance,
3. sense of current threat.

### DSO
Tre klynger:
1. affective dysregulation,
2. negative self-concept,
3. disturbances in relationships.

Denne opdeling passer til FearPrime, fordi den forhindrer, at ændring i eksempelvis hypervigilans automatisk fortolkes som ændring i negativt selvkoncept eller relationel funktion.

**Primær reference:** Cloitre et al. (2018), *The International Trauma Questionnaire: development of a self-report measure of ICD-11 PTSD and complex PTSD*. Acta Psychiatr Scand. PMID: 30178492. DOI: `10.1111/acps.12956`.

Dansk klinisk validering: Vang et al. (2021), fem danske kliniske samples. PMID: 33968325. DOI: `10.1080/20008198.2021.1894806`.

---

## 2. Scoringprincipper

FearPrime registrerer to slags ITQ-output **separat**:

### A. Dimensional symptom severity
Registrér:
- PTSD-symptomscore,
- DSO-symptomscore,
- de seks underklynger hver for sig, når datastrukturen tillader det.

På den almindelige ITQ-model består PTSD- og DSO-symptomdelen hver af seks kernesymptomer vurderet på en 0–4-skala. Det giver et almindeligt dimensionalt spænd på:

```text
PTSD symptom severity: 0–24
DSO symptom severity:  0–24
```

Funktionsitems holdes uden for disse symptomsummer.

### B. Probable diagnostic scoring
Når den officielle scoringsalgoritme bruges, skal cluster-krav og funktionspåvirkning være opfyldt efter instrumentets regler.

FearPrime kalder dette:

```text
ITQ probable PTSD
ITQ probable CPTSD
```

og **ikke** “diagnose”.

PTSD og CPTSD behandles som alternative diagnostiske klassifikationer i ICD-11-algoritmen; CPTSD kræver både PTSD- og DSO-kriterier.

### Vigtig versionsregel
ITQ og relaterede scoringstilgange kan blive opdateret. Dokumentér derfor altid:
- version,
- sprog,
- dato,
- scoringvejledning,
- referenceperiode,
- om kliniske checks blev brugt.

Nyere forskning har undersøgt ekstra “clinical checks”, fordi rene selvrapporter kan overvurdere symptombekræftelse. Se Shevlin et al. (2025), PMID: 40122678, DOI: `10.1111/acps.13799`.

---

## 3. FearPrime-datastruktur

Minimum ved en CPTSD-måling:

```yaml
date: YYYY-MM-DD
instrument: ITQ
version: documented
language: da/en/other
reference_period: documented
ptsd_symptom_score: null
dso_symptom_score: null
ptsd_clusters:
  re_experiencing: null
  avoidance: null
  current_threat: null
dso_clusters:
  affect_dysregulation: null
  negative_self_concept: null
  relationship_disturbance: null
functional_impairment:
  ptsd: null
  dso: null
probable_classification:
  ptsd: null
  cptsd: null
clinical_checks_used: null
notes: null
```

Personidentificerende eller udfyldte helbredsdata skal ikke pushes til dette offentlige repo.

---

## 4. FearPrime-mål må ikke erstattes af ITQ

ITQ fortæller ikke direkte:
- hvor præcist en person diskriminerer threat vs safety,
- hvor stærkt en prediction error var,
- om extinction generaliserede,
- om fear returnerede via renewal eller reinstatement,
- hvor hurtigt autonom recovery sker,
- om en bestemt biologisk intervention forbedrede læring.

Derfor bruges ITQ parallelt med [LEARNING_METRICS.md](LEARNING_METRICS.md).

En mulig struktur er:

```text
Klinisk symptomlag
    ↓
ITQ PTSD + DSO

Læringslag
    ↓
expectancy + discrimination + extinction + recall + generalization

Funktionslag
    ↓
konkrete hverdagsmål

Fysiologisk lag
    ↓
HR/HRV/SCR/startle/respiration hvis målt
```

Ingen af lagene må alene stå som proxy for de andre.

---

## 5. Funktion som separat akse

FearPrime registrerer funktion særskilt fra symptomseverity.

Eksempler på funktionsmål:
- gennemførte meningsfulde aktiviteter,
- social deltagelse,
- arbejde/studie,
- søvnrelateret funktion,
- evne til at blive i en sikker, men tidligere undgået situation,
- recovery-tid efter aktivering.

Et symptomfald uden funktionsændring og en funktionsforbedring uden stort symptomfald er begge informative resultater.

---

## 6. Longitudinel brug

Ved gentagen måling registreres mindst:

```text
T0 = baseline
T1 = efter defineret periode/intervention
T2 = retention/follow-up
```

Rapportér:
- absolut ændring,
- procentuel ændring kun som deskriptivt supplement,
- PTSD og DSO separat,
- funktionsændring separat.

Undgå at kalde procentvis scoreændring for “procent helbredt”.

### Eksempel

```text
PTSD: 18 → 12
DSO: 20 → 18
funktion: 3/10 → 6/10
```

Fortolkning: PTSD-symptomer ændrede sig mere end DSO, mens funktion samtidig steg. Det er mere informativt end én samlet “traumescore”.

---

## 7. DSO som forskningssignal

FearPrime bruger de tre DSO-domæner som forskellige forskningsmål:

### Affect dysregulation
Mulige koblinger:
- autonom recovery,
- interoception,
- state regulation,
- dissociation/hyperarousal.

### Negative self-concept
Mulige koblinger:
- autobiografisk memory,
- predictive self-model,
- skam/selvfortolkning,
- social prediction.

### Relationship disturbance
Mulige koblinger:
- social threat learning,
- trust/safety discrimination,
- attachment-relaterede forventninger,
- social generalization.

Disse koblinger er **FearPrime-hypoteser** og må ikke fremstilles som komponenter i ITQ's validerede scoring.

---

## 8. Dissociation holdes separat

CPTSD og dissociation må ikke behandles som synonymer.

Hvis dissociation undersøges, registreres den med et særskilt valideret mål eller en eksplicit observationsvariabel. Dette gør det muligt at teste state-dependent learning uden at indbygge dissociation i DSO-scoren.

---

## 9. Centrale metodiske forbehold

1. **Selvrapport ≠ klinisk diagnose.**
2. Scoreændring kan skyldes regression mod middelværdi, kontekst, behandling, forventning eller måleusikkerhed.
3. ITQ's psykometri kan variere mellem populationer og sprog.
4. Dansk validering støtter PTSD/DSO-strukturen på tværs af flere samples, men ikke alle delpopulationer viste identisk model-fit.
5. Cross-cultural comparability skal ikke antages automatisk.
6. En CPTSD-score siger ikke hvilken neurobiologisk mekanisme der har ændret sig.

Se også Hyland et al. (2024), PMID: 38007852, om fortolkning og begrænsninger ved ITQ.

---

## 10. Falsificerbare FearPrime-forudsigelser

CPTSD-modellen styrkes, hvis data viser, at:

1. PTSD- og DSO-domæner kan ændre sig delvist uafhængigt over tid.
2. threat/safety-learning-mål korrelerer stærkere med bestemte PTSD-domæner end med alle DSO-domæner ensartet.
3. social-learning-mål forklarer yderligere variation i relationelle DSO-problemer efter kontrol for generel symptomseverity.
4. funktion ikke kan reduceres til én PTSD/DSO-sumscore.

Modellen svækkes, hvis de separate målelag konsekvent ikke tilfører information ud over en enkel samlet symptomscore.

---

## 11. Referencer

- Cloitre M, Shevlin M, Brewin CR, et al. 2018. *The International Trauma Questionnaire: development of a self-report measure of ICD-11 PTSD and complex PTSD.* Acta Psychiatr Scand. PMID 30178492. DOI `10.1111/acps.12956`.
- Vang ML, Dokkedahl SB, Løkkegaard SS, et al. 2021. *Validation of ICD-11 PTSD and DSO using the International Trauma Questionnaire in five clinical samples recruited in Denmark.* Eur J Psychotraumatol. PMID 33968325. DOI `10.1080/20008198.2021.1894806`.
- Hyland P, Brewin CR, Cloitre M, Karatzias T, Shevlin M. 2024. *Responding to concerns related to the measurement of ICD-11 complex posttraumatic stress disorder using the International Trauma Questionnaire.* PMID 38007852. DOI `10.1016/j.chiabu.2023.106563`.
- Shevlin M, Hyland P, Brewin CR, Cloitre M, Karatzias T, Redican E. 2025. *Testing the Use of “Clinical Checks” With the International Trauma Questionnaire to Measure PTSD and Complex PTSD.* PMID 40122678. DOI `10.1111/acps.13799`.

## Status
**v0.19:** CPTSD har nu et separat measurement-layer. Næste opgave er at koble longitudinal ITQ-data til FearPrimes standardiserede learning metrics uden at sammenblande konstrukterne.
