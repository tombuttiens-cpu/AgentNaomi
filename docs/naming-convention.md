# Case folder naming convention

Each patient gets one folder under `cases/`. The folder name is the **case
ID**, and every file in the folder starts with that same ID:

```
cases/
  2026-014/
    2026-014_INFO.txt
    2026-014_SCORES.csv
    2026-014_REFERRAL.pdf
    2026-014_ANAMNESIS.docx
    2026-014_OBSERVATIONS.docx
    2026-014_SCORESHEET_<test>.pdf      (optional, one per test)
    output/                            (written by the agent)
```

Pattern: `<CASEID>_<TYPE>[_<detail>].<ext>`

- Use no names, initials, or birth dates in the case ID or in file names.
- `TYPE` is always in CAPITALS and must come from the table below.

## Document types

| TYPE | Required | Format | What the agent does with it |
|---|---|---|---|
| `INFO` | yes | `.txt` (key: value) | Demographics used for norm selection: `age`, `education` (required), plus `sex`, `handedness`, `test_date`, `referral_question` |
| `SCORES` | yes | `.csv` (`test,measure,raw`) | Raw scores. Fed to `tools/score_case.py`. An empty `raw` means the test was not administered |
| `REFERRAL` | no | pdf/docx | Referral letter. The agent extracts the referral question and relevant history |
| `ANAMNESIS` | no | pdf/docx | Intake interview. Summarised into the history section |
| `OBSERVATIONS` | no | pdf/docx/txt | Behavioural observations during testing |
| `SCORESHEET_<test>` | no | pdf/image | Scanned score forms, used to double-check `SCORES.csv` |

**TODO:** extend this table with her real document types (questionnaires,
previous reports, medical imaging reports, invoices, …).

## Example `INFO.txt`

```
age: 62
education: high
sex: F
handedness: right
test_date: 2026-09-20
referral_question: Memory complaints for 1 year.
```

The `education` values must match the ones used in `norms/norms.csv`.
