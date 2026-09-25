---
name: process-case
description: Process an anonymous neuropsychological case folder. Validate the files, score the tests against norms, summarise the documents, and draft the report. Use when she says "process case X", "do the paperwork for X", or uploads a new case folder.
---

# Process a case

Input: a folder `cases/<CASEID>/`. If she didn't name one, list the folders
under `cases/` that have no `output/` folder yet, and ask which one.

## 1. Check the folder

- Read `docs/naming-convention.md`.
- Check that every file starts with `<CASEID>_` and has a known TYPE. List
  any unknown files and ask about them. Don't guess what they are.
- Check that `INFO.txt` and `SCORES.csv` exist and that `INFO.txt` has `age`
  and `education`.
- Scan the documents for identifying data (names, national register numbers,
  addresses, full birth dates). If you find any, tell her which file contains
  it and don't reproduce it anywhere.

## 2. Score

Run:

```
python tools/score_case.py cases/<CASEID>
```

- Exit code 0 means everything was scored.
- Exit code 1 means some measures couldn't be scored. Read
  `output/<CASEID>_ISSUES.md` and report the issues. Don't try to score them
  by hand.
- If `SCORESHEET_*` files exist, compare the raw scores on them with
  `SCORES.csv` and flag any mismatch.

## 3. Summarise the documents

From `REFERRAL`, `ANAMNESIS`, and `OBSERVATIONS`, write
`output/<CASEID>_SUMMARY.md` with these sections: referral question,
relevant history, observations during testing. Stick to what the documents
say.

## 4. Draft the report

Fill `templates/report_template.md` and write it to
`output/<CASEID>_REPORT_DRAFT.md`.

- Copy score tables verbatim from `output/<CASEID>_SCORED.md`.
- In the interpretation, refer only to the classifications in the scored
  output.
- Mark anything uncertain as `[TO CHECK: …]`.

## 5. Report back

Keep the summary short and cover:

- what was produced
- open issues: missing norms, missing scores, mismatches, identifying data
  found
- everything marked `[TO CHECK]`
