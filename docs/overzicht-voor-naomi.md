# Claude als hulp bij NPO-verslagen – overzicht

*Stand van zaken 30/09/2026, na de eerste testcasus (NPO A.B.)*

## 1. Het idee in één zin

Jij levert per patiënt een map aan op Drive. Claude maakt daaruit een
**conceptverslag in jouw eigen sjabloon**: anamnese, observaties, bespreking
per domein, besluit en de bijlagetabellen met alle scores. Jij controleert,
past aan en ondertekent.

## 2. Wat Claude per patiënt doet

1. **Map inlezen**: intakegesprek, scan van het testonderzoek, jouw
   `Normen.xlsx`, BDI en SCL-90.
2. **Ruwe scores aflezen van de scan**, ook het handschrift: woorden per
   AVLT-poging, CFT-items, cijferreeksen, Tower-items, COWAT, VAT, tekeningen
   en opmerkingen in de kantlijn.
3. **Controleren**: elke score in `Normen.xlsx` wordt vergeleken met de scan.
   Bij een verschil kiest Claude niet zelf. Het verschil wordt gemeld en in het
   verslag geel gemarkeerd.
4. **Scoren tegen de juiste normgroep** (geslacht, leeftijd, opleiding). Dat
   gebeurt altijd met code, nooit "uit het hoofd". Hiervoor werden jouw eigen
   formules uit `Normen.xlsx` nagebouwd. Als test werden alle 17 waarden die
   jouw bestand al berekend had exact teruggevonden, inclusief afronding.
5. **Geen passende normgroep?** Dan stopt Claude en vraagt het aan jou.
6. **Verslag schrijven in jouw stijl**, op basis van je voorbeeldverslagen en
   je vaste zinnen ("Psychometrisch onderzoek toont dat, wat aandacht
   betreft, …"). De classificatiewoorden volgen jouw Scorehulpmiddel
   (zeer laag … zeer hoog).
7. **Invullen in `NPO verslag SJABLOON.docx`**: logo, opmaak en voettekst
   blijven behouden.
   - **Geel** = nog te controleren of aan te vullen door jou.
   - **[CONCEPT]** = diagnose en advies. Dat is altijd jouw beslissing.
8. **Opleveren**: een Google Docs-versie in de patiëntenmap en het
   Word-bestand.

## 3. Wat er in een patiëntenmap moet zitten

| Bestand | Nodig? | Waarvoor |
|---|---|---|
| `Intakegesprek.docx` | ja | (hetero)anamnese. **Zet bovenaan: geslacht, leeftijd, opleiding** (bv. "Man, 53 jaar, opleiding ≤ 12 j"). Ook handig: verwijzer, datum consult en onderzoek, lateraliteit. |
| `Testonderzoek <initialen>.pdf` | ja | scan van alle scoreformulieren en tekeningen |
| `Normen.xlsx` | ja | jouw scorebestand met de ingevulde ruwe scores (o.a. Bourdon-regeltijden) |
| `BDI-II-NL.xlsx`, `SCL-90_vragenlijst.xls` | indien afgenomen | vragenlijsten |
| `Observaties.docx` | optioneel | jouw eigen indruk en observaties, als je die apart noteert |

## 4. Welke normen worden gebruikt

| Test | Bron | Weergave in verslag |
|---|---|---|
| AVLT, CFT (Rey), COWAT, Bourdon | Vingerhoets (Vlaamse normen), zoals in `Normen.xlsx` | Z = … |
| D-KEFS Tower | TOL-handleiding, tabellen A.1–A.6 | GS = … / Cum. % |
| WAIS-IV-NL (cijferreeksen, symbool zoeken, symbool substitutie, VSI) | WAIS-handleiding Vlaanderen, tabellen A.1, A.5 en C.1 | GS = …, Pct. en BI (95 %) |
| RDS | afgeleid uit cijferreeksen, cut-off ≤ 7 | |
| VAT lange vorm | VAT-handleiding tabel 3 | Pct. |
| BDI-II-NL | 0–13 minimaal, 14–19 licht, 20–28 matig ernstig, 29+ ernstig | |
| SCL-90 | N-normen (normale populatie) uit `Vragenlijst 2.xls` | zeer laag … zeer hoog |
| CFT-werkwijze | `Scoringssystemen CFT.docx` (RCF-OSS niveaus) | "gefragmenteerde werkwijze" enz. |

## 5. De testcasus A.B.: wat er gebeurde

**Opgeleverd**
- Google Doc "NPO verslag A.B. (concept – Claude)" in de map NPO A.B.
- Word-versie in jouw sjabloon (bezorgd via Tom)

**Onderweg gevonden (graag je oordeel)**
1. **AVLT A4**: op het formulier staan 8 woorden genoteerd, het totaal zegt 7.
   Op vraag van Tom werd 8 gebruikt, waardoor de som 31 wordt.
2. **CFT onmiddellijke en uitgestelde reproductie**: de itemscores op het
   formulier tellen op tot 24 en 24. In `Normen.xlsx` staat 21,5 en 23,5. In
   het verslag staan de waarden van het formulier; beide staan in de
   opmerking.
3. **Bourdon**: 45 regeltijden ingevuld in plaats van 50. Het sjabloon zegt
   "normen op basis van eerste 25 regels", `Normen.xlsx` gebruikt alle
   regels. Het bestand werd gevolgd.
4. **RDS = 6** (onder cut-off 7). Dit werd als aandachtspunt in het besluit
   gezet.
5. **Symbool Zoeken**: een volledige pagina werd overgeslagen.
6. **Onduidelijk in de intake**: "19 dagen in GHB", Depakine-dosis ("50 mh"),
   Bilastine (antiallergicum, maar genoteerd bij reuma), "niet met armen of
   benen slapen".
7. **Ontbrekend**: leeftijd (Tom gaf 53 door), verwijzer, datums,
   lateraliteit, jouw eigen indruk en observaties.
8. **WAIS-tabellen**: de handleiding was te groot om te downloaden en werd
   uit de tekstversie gelezen. De methode werd gecontroleerd met je
   voorbeeldverslag (61 jaar), maar een korte controle van GS 6 / 6 / 7 / 9 en
   VSI 89 is aangeraden.

**Waar je extra naar mag kijken**
- De **conceptdiagnose en het advies**. Verder genoemd: droomgedrag, sloffen
  en de familiale belasting voor Parkinson als reden voor neurologische
  correlatie.
- De **kwalitatieve inschattingen**: klok en kubus, CFT-werkwijze (voorstel:
  niveau 4 "gefragmenteerd").

## 6. Feedback geven: zo verbeteren we het

Schrijf gerust in de Google Doc zelf (opmerkingen of suggesties), of in een
aparte lijst. Handig om te weten:

1. **Toon en formulering**: welke zinnen klinken niet als jij? Wat wil je
   korter of langer?
2. **Anamnese**: klopt de volgorde van de alinea's? Wat laat je normaal weg of
   voeg je toe?
3. **Observaties**: hoe noteer je die voortaan het best (apart bestand,
   kantlijn van de scan, of in het intakedocument)?
4. **Interpretatie**: klopt de vertaling van scores naar woorden? Bv. geldt
   Z = −0,67 bij jou als "gemiddeld" of als "laaggemiddeld"?
5. **Besluit en diagnose**: hoeveel mag Claude voorstellen? Liever alleen een
   samenvatting en laat je diagnose en advies volledig open?
6. **Normkeuzes**: klopt Bourdon in Z (zoals in het sjabloon) of wil je
   percentielen (zoals `Normen.xlsx` geeft)? Welke SCL-90-normgroep wil je?
7. **Andere testen of vragenlijsten** die je soms afneemt (Stroop, TMT, BNT,
   RBANS, DASS, ADHD-lijst, …): die zitten al in `Normen.xlsx` en kunnen
   toegevoegd worden.

Elke opmerking wordt verwerkt in de instructies van de agent, zodat het
volgende verslag er al rekening mee houdt.

## 7. Privacy

- Patiëntgegevens blijven op jouw Drive. Ze worden **niet** in de code-opslag
  (GitHub) bewaard.
- Om te kunnen lezen en schrijven, verwerkt Claude de inhoud van de bestanden.
  Werk dus met initialen, zonder naam, geboortedatum of rijksregisternummer
  in de bestanden.
- Het eindverslag met naam en geboortedatum vul je zelf in.

## 8. Waar alles staat

- **Patiëntenmap (test)**: Drive → Oefening → NPO A.B. Daar staan het
  conceptverslag en `claude_werkbestand_scoring_AB.py` (de berekeningen, om
  later te kunnen herberekenen).
- **Instructies en code van de agent**: GitHub `tombuttiens-cpu/AgentNaomi`,
  branch `claude/neuropsych-paperwork-agent-2ytnhp`
  - `CLAUDE.md`: vaste regels
  - `.claude/skills/process-case/SKILL.md`: stappenplan per casus
  - `docs/norm-sources.md`: welke normtabel voor welke test
  - `templates/stijlgids.md`: jouw schrijfstijl
  - `docs/feedback-log.md`: jouw feedback en wat ermee gebeurde
