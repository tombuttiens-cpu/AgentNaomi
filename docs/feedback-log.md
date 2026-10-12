# Feedback log

Every piece of feedback from Naomi goes here, together with what changed in
the agent (which file). Newest at the top.

| Date | Case | Feedback | Change made |
|---|---|---|---|
| 2026-10-11 | test case 1 | Bourdon Z-scores wrong: compute over the first 25 rows with Vingerhoets norms; omissions over the first 25 rows too | `normen_xlsx.bourdon_raw`, skill step 1, style guide, norm-sources |
| 2026-10-11 | test case 1 | Bourdon: add a chart of the row times with a trend line | `tools/charts.py`, builder `images`, style guide |
| 2026-10-11 | test case 1 | Add the scan of the cube and clock under the Kubus-Klok heading | builder `images`, skill step 3 |
| 2026-10-11 | test case 1 | CFT O.R. = 21,5 and U.R. = 23,5 (her entries were correct) | rule: `Normen.xlsx` is leading; differences only in the chat summary |
| 2026-10-11 | test case 1 | Test-specific observations belong under each test as *Opmerking, not in OBSERVATIES | skill step 3, style guide |
| 2026-10-11 | test case 1 | Good to ask for impression, effort and cooperation; she will note these from now on | naming convention (intake), skill step 0 |
| 2026-10-11 | test case 1 | Medication: copy the list literally as noted | style guide, skill step 3 |
| 2026-10-11 | test case 1 | An ambiguous phrase in the intake notes was clarified by her | report v2; agent marks unclear phrases [TE VERDUIDELIJKEN] |
| 2026-10-02 | test case 1 | Abbreviation of a hospital explained (GHB) | glossary in style guide |
| 2026-10-02 | test case 1 | Personalia will be in the intake document | skill step 0, naming convention |
| 2026-10-11 | test case 1 | Learning curve: mention that the third trial shows no increase | style guide, skill step 3 |
| 2026-10-11 | test case 1 | Use 'minieme' instead of 'minimale' (BDI) | style guide; `Miniem` category in the table |
| 2026-10-11 | test case 1 | Subscale names always in italics | builder: text between “ ” → italics |
| 2026-10-11 | test case 1 | Don't repeat the subscales in the besluit | style guide, skill step 3 |
| 2026-10-11 | test case 1 | RDS doesn't apply in an NPO for dementia | skill step 2, style guide |
| 2026-10-11 | test case 1 | Always mention errors and skipped items per task | skill step 3, style guide |
| 2026-09-30 | test case 1 | Age, sex and education must always be in the intake summary | CLAUDE.md rule 4 + docs/naming-convention.md; agent asks when missing |
| 2026-09-30 | test case 1 | `Normen.xlsx` (with Bourdon row times) is always part of the case folder | docs/naming-convention.md, process-case step 1 |
| 2026-09-30 | test case 1 | AVLT: Tom chose the count of words over the total written on the form | superseded on 2026-10-11 by "Normen.xlsx is leading"; still an open question below |

## Open questions for Naomi

- Test case 1, AVLT A4: the words noted on the form and the total she wrote differ. The report uses the count of words (decided by Tom). Which counts in general: her entry or the count of words?
- RDS outside a dementia question (e.g. after brain injury or in a legal context): discuss it or not?
- Bourdon omission norms for > 12 j are not in `Normen.xlsx` (only in the Vingerhoets PDF, table 6). Should they be added to the workbook?
- SCL-90: is the N (general population) norm the right default? (no comment so far, so it is kept)
