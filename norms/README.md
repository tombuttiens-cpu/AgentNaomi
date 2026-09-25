# Norms

`norms.csv` has one row per test × measure × age band × education level.

| column | meaning |
|---|---|
| test, measure | must match `SCORES.csv` exactly (case-insensitive) |
| kind | `meansd` (mean + SD) or `table` (raw → score lookup) |
| direction | `higher` if a higher raw score is better, `lower` for e.g. time or errors |
| age_min, age_max | inclusive age band |
| education | an education level, or `*` for any level. A specific level wins over `*` |
| mean, sd | for `meansd` |
| table, scale | for `table`: file in `tables/` and its output scale (`scaled`, `t`, `standard`, `z`) |
| source | the manual or article and the page, so every number can be traced |

The current rows are **fictional examples** and have to be replaced with her
real norms. Commercial norm tables are copyrighted, so keep this repo private.
