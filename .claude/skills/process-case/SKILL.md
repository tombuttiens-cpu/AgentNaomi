---
name: process-case
description: Turn one patient folder (intake notes, scanned test forms, Normen.xlsx, BDI/SCL-90 questionnaires) into a draft NPO report in Naomi's Word template. Use when she says "verwerk casus X", "maak het verslag voor X", or shares a new NPO folder (Drive link). Also used in comparison mode for cases she already reported.
---

# Process an NPO case

Write everything for her in Dutch. Keep patient files out of git (scratchpad
or `cases/`). Read `docs/feedback-log.md` first: every rule there is hers.

## 0. Collect

1. Get the folder ID from the Drive link she pastes, list its files and
   download them (see `docs/workflow.md`). Also download, once per session:
   `NPO verslag SJABLOON.docx` and the style examples.
2. Check the files against `docs/naming-convention.md`. For an unknown file,
   ask her what it is.
3. From `Intakegesprek`, get **sex, age, education** and the **personalia**
   (referrer, consultation and test dates, profession, handedness), plus her
   **impression, effort and cooperation** if she noted them. If sex, age or
   education is missing, ask before scoring (hard rule 4).
4. Write the case facts into a `case.json` in the scratchpad: demographics,
   raw scores, remarks per test.

## 1. Read the raw scores

- **`Normen.xlsx` is leading** for every raw score she entered (sheets
  `Scorehulpmiddel` and `Bourdon_invul`). She sometimes re-scores, e.g. half
  points on the CFT, so her entry wins over a sum you re-add from the scan.
- Read the scan `Testonderzoek <ID>.pdf` (render pages to PNG and look at
  every page) to:
  - **cross-check** her entries. Report every difference **in your chat
    summary** and let her decide; don't put it in the report.
  - collect what isn't in the workbook: WAIS raw scores (CRV, CRA, Symbool
    Zoeken goed/fout, Symbool Substitutie), VAT, Kubus-Klok, digit-span
    items, the CFT drawing order, and every handwritten remark
    (quotes, "lacht", "afwezige indruk", time limits, skipped pages).
- **Bourdon:** take the row times from `Bourdon_invul` and the omissions per
  row from the scan (circled dots). Norms use the **first 25 rows**
  (`normen_xlsx.bourdon_raw`).
- Questionnaires: `BDI-II-NL.xlsx` (21 items) and `SCL-90_vragenlijst.xls`
  (check the subscale totals against the item key in `docs/norm-sources.md`).

## 2. Score (code only)

- AVLT, CFT, COWAT, Bourdon: `tools/normen_xlsx.py` reads the norm group
  straight from her `Normen.xlsx`. Z comes from `scoring.z_workbook`.
- For times, average deviation, omissions and errors, take the class from
  −Z (`scoring.class_for_lower_is_better`). Show Z unflipped, as she does.
- Tower, WAIS, VAT, BDI, SCL-90: use the tables listed in
  `docs/norm-sources.md`. Prove a table lookup against a known value first.
- **No fitting norm group → stop and ask** (hard rule 3).
- **RDS:** fill in the table row, but **don't interpret it** when the
  question is about dementia or neurodegeneration. In other contexts, ask
  her before discussing it.

## 3. Write the content

Follow `templates/stijlgids.md`. Generate the content JSON with a script that
reads the scores, so no number is typed by hand. Use `scoring.adjective()`
before de-words ("een gemiddelde mate").

- **Personalia:** take them from the intake. Name and date of birth stay
  `_/_/_`; she fills those in herself.
- **(hetero)Anamnese:** her narrative order. Copy the **medication list
  literally** from the intake (no indications, no corrections). Expand known
  abbreviations using the glossary in the style guide.
- **OBSERVATIES:** the companion, plus her general impression, effort and
  cooperation. If those aren't in the notes, write `[AAN TE VULLEN: …]`.
  **Never** put test-specific observations here: those go in the table
  under each test as `*Opmerking`.
- **Bespreking resultaten:** her fixed sentences per domain. In the learning
  curve, mention trials without an increase, or with a decrease.
- **Besluit:** summary; one sentence on the questionnaires **without
  repeating subscale names**; an "Observationeel …" sentence; the standard
  caveat; then `[CONCEPT – …]` diagnosis and advice.
- **Attachment tables:** one `*Opmerking` per test, including errors and
  skipped items or pages. Pictures:
  - the cube and clock drawings, cropped from the scan, in the row
    `Kubus-Klok teken test`
  - the Bourdon chart (`tools/charts.py`) in the empty row under `41-50`
- Put scale and item names between “ ” so they come out in italics.

## 4. Build and deliver

```
python tools/build_report.py "NPO verslag SJABLOON.docx" content.json "NPO verslag <ID> (concept).docx" --html report.html
```

- Put the HTML in the case folder as a Google Doc titled
  `NPO verslag <ID> (concept – Claude)`.
- Send the .docx to her with `SendUserFile`.
- Save the case script(s) in the case folder as `claude_werkbestand_*.py`,
  so the case can be rebuilt after feedback.

## 5. Report back (Dutch, short)

- the norm groups used
- differences between the scan and `Normen.xlsx` (her values were used)
- everything marked `[TE CONTROLEREN]`, `[AAN TE VULLEN]`, `[CONCEPT]`

## Comparison mode (cases she already reported)

When she asks to compare ("vergelijk met mijn verslag"):

1. Make the draft **without opening her final report**. Exclude any file
   whose name contains `verslag` or `definitief`.
2. Then read her report and write `Vergelijking <ID>` (a Google Doc in the
   case folder) with a table:
   - section
   - difference (numbers, classification, wording, missing or extra content)
   - who is right, or a question for her
3. Log every systematic difference in `docs/feedback-log.md` and fix the
   rule it points to.
