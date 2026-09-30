# AgentNaomi

A Claude agent that turns a neuropsychological examination (NPO) into a draft
report in Naomi's own Word template, written in Dutch.

## What it does per patient

1. Reads the Drive case folder: intake notes, the scan of the test forms, her
   `Normen.xlsx` workbook and the BDI/SCL-90 questionnaires.
2. Reads every score form in the scan and checks the raw scores against her
   workbook. Any mismatch is reported, not silently fixed.
3. Scores everything against the correct norm group (sex, age, education)
   using code, never mental arithmetic. If no norm group fits, it asks her.
4. Writes the (hetero)anamnese, observations, discussion of results and
   conclusion in her style. Diagnosis and advice are marked as drafts.
5. Fills in `NPO verslag SJABLOON.docx`, keeping the logo and footer. Anything
   she still needs to check is highlighted yellow.
6. Puts a Google Docs copy in the case folder and delivers the .docx.

## Layout

| Path | Purpose |
|---|---|
| `CLAUDE.md` | Rules the agent always follows |
| `.claude/skills/process-case/` | Step-by-step case workflow |
| `docs/naming-convention.md` | What a case folder must contain |
| `docs/norm-sources.md` | Which norm table per test and norm group, plus her classification |
| `docs/workflow.md` | Technical notes (Drive downloads and uploads) |
| `templates/stijlgids.md` | Her writing style and fixed sentences |
| `tools/scoring.py` | Conversions, Excel-exact rounding, classification |
| `tools/build_report.py` | Fills the Word template from a content JSON |

## Privacy

- Patient files are never committed; `cases/` is git-ignored.
- Norm tables stay on her Drive because they're copyrighted.
- Keep this repository private.

## Tests

```
python3 -m unittest discover -s tests
```
