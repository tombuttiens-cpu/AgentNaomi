# Handleiding: je NPO-verslagen laten voorbereiden door Claude

*Versie 12/10/2026, na het verwerken van je feedback op testcasus 1*

Claude maakt per patiënt een **conceptverslag in jouw sjabloon**. Dat
concept bevat:

- de (hetero)anamnese en de observaties
- de bespreking per domein en het besluit, met de diagnose en het advies als
  concept
- de bijlage met alle scores, opmerkingen, de tekeningen en de
  Bourdon-grafiek

Jij leest na, past aan en ondertekent.

---

## A. Eenmalig instellen (± 30 minuten, samen met Tom)

1. **Eigen Claude-abonnement** op claude.ai. Neem liefst Max: elke casus
   vraagt veel leeswerk (scan van ± 18 pagina's en normtabellen).
2. **GitHub-account** aanmaken op github.com (gratis), als je er nog geen
   hebt.
3. **Tom** zet de opslagplaats `AgentNaomi` op **privé** en nodigt jou uit:
   - Privé zetten: GitHub → AgentNaomi → *Settings* → *General* →
     *Danger Zone* → *Change visibility* → *Private*.
   - Jou uitnodigen: GitHub → AgentNaomi → *Settings* → *Collaborators* →
     *Add people*.

   Aanvaard daarna de uitnodiging in je mail.
4. Ga in Claude naar **claude.ai/code** en koppel je **GitHub-account**
   wanneer daarom gevraagd wordt.
5. Koppel **Google Drive** in Claude: *Settings → Connectors → Google
   Drive*. Claude werkt dan rechtstreeks in jouw eigen Drive.
6. **Privacy-instelling**: kijk in *Settings → Privacy* of je gesprekken mogen
   gebruikt worden om modellen te verbeteren, en zet dat naar wens uit.
7. **Laat op je Drive staan waar het nu staat**:
   - het sjabloon `NPO verslag SJABLOON.docx`
   - de map met normtabellen
   - `Scoringssystemen CFT.docx`
   - `Vragenlijst 2.xls` (SCL-90-normen)
   - je voorbeeldverslagen

   Verplaats je iets, zeg het dan aan Claude. Dan wordt de verwijzing
   aangepast.

## B. Per patiënt: de map klaarzetten

Maak op Drive een map **`NPO <initialen>`** (bv. `NPO X.Y.`) met deze
bestanden:

| Bestand | Wat erin moet |
|---|---|
| `Intakegesprek.docx` | **Bovenaan:** geslacht, leeftijd, opleiding (bv. "Man, 53 jaar, opleiding ≤ 12 j: …"), verwijzer, datum consult en onderzoek, beroep, links- of rechtshandig, en de **vraagstelling** (bv. dementie). **Onderaan:** je indruk, inzet en medewerking. **Daartussen:** je gewone notities, met de medicatie zoals je ze in het verslag wil zien. |
| `Testonderzoek <initialen>.pdf` | **Alle** scoreformulieren en tekeningen, goed leesbaar gescand (liefst 300 dpi, rechte pagina's). Noteer testspecifieke observaties op het formulier zelf: die komen als *Opmerking bij die test. |
| `Normen.xlsx` | Ingevuld met de ruwe scores van deze patiënt, inclusief de Bourdon-regeltijden. Wat jij hier invult, geldt als de juiste score. |
| `BDI-II-NL.xlsx`, `SCL-90_vragenlijst.xls` | Als ze afgenomen werden. |

**Niet** in de map: de naam, geboortedatum of rijksregisternummer van de
patiënt. Die vul je zelf in het eindverslag in.

## C. Claude starten

1. Ga naar **claude.ai/code** → *New session* → kies de opslagplaats
   **AgentNaomi**.
2. Plak de link van de patiëntenmap en typ: **"Verwerk casus: <link>"**
3. Claude leest alles, rekent alles na en stelt vragen als er iets ontbreekt
   of niet past, bv. een ontbrekende leeftijd of geen passende normgroep.
   Antwoord gewoon in het gesprek.
4. Daarna krijg je:
   - een **Google Doc** "NPO verslag <initialen> (concept – Claude)" in de
     map
   - het **Word-bestand** in je eigen sjabloon (downloaden in het gesprek)
   - een **samenvatting** met de normgroepen, de verschillen tussen scan en
     `Normen.xlsx`, en alle punten die je nog moet nakijken

## D. Nalezen

- **Gele stukken** = nakijken of aanvullen.
- **[CONCEPT]** = diagnose en advies, altijd jouw beslissing.
- Kijk de **verschillen tussen scan en Normen.xlsx** na uit de samenvatting.
- Vul naam en geboortedatum in en onderteken.

## E. Feedback geven: zo wordt Claude beter

- **In hetzelfde gesprek:** zeg gewoon wat er anders moet. Claude past het
  verslag aan **en** de vaste regels, zodat het de volgende keer meteen juist
  is.
- **Of via opmerkingen** in de Google Doc, zoals je deed bij testcasus 1.
  Typ daarna: "Lees de opmerkingen in <link> en verwerk ze."
- Elke aanpassing aan de regels komt in het **feedbacklogboek** en in een
  wijzigingsvoorstel (pull request) op GitHub. **Tom (of jij) klikt op
  *Merge***. Pas dan gebruiken alle volgende gesprekken de nieuwe regel.

## F. Kwaliteit testen met casussen die je al afwerkte

1. Zet je eigen definitieve verslag in de map en zet het woord
   **"definitief"** in de naam (bv. `NPO verslag X.Y. definitief.docx`).
2. Typ: **"Vergelijk casus: <link>"**
3. Claude maakt eerst een eigen concept **zonder** jouw verslag te openen.
   Daarna maakt het een document **"Vergelijking <initialen>"** met elk
   verschil: in de cijfers, de classificatie, de formulering, en wat ontbreekt
   of te veel is.
4. Systematische verschillen worden meteen omgezet in nieuwe regels.

## G. Tips voor het beste resultaat

- **Eén gesprek per patiënt.** Begin voor de volgende patiënt een nieuw
  gesprek.
- **Gebruik altijd dezelfde bestandsnamen.**
- **Afkortingen** (zoals GHB): schrijf ze één keer voluit in je feedback.
  Ze komen dan in de woordenlijst.
- **Nieuwe test of vragenlijst** (Stroop, TMT, BNT, RBANS, DASS, …)? Zeg welke
  normtabel Claude moet gebruiken. Zolang die er niet is, stopt Claude en
  vraagt het.
- **Twijfel je aan een getal?** Vraag "toon hoe je X berekend hebt". Elke
  score wordt met code berekend en kan je stap voor stap nakijken.

## Nog open vragen aan jou

1. AVLT: als de genoteerde woorden en het totaal op het formulier verschillen,
   telt dan je ingevulde totaal of het aantal woorden?
2. RDS buiten een vraagstelling rond dementie (bv. NAH, juridisch): bespreken
   of niet?
3. Bourdon-omissies bij opleiding > 12 jaar: die normen staan niet in
   `Normen.xlsx`. Wil je ze toevoegen?
4. SCL-90: blijven de normen voor de normale populatie de standaard?
