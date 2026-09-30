# Norm sources per test

Norm groups are chosen by **sex, age and education (≤ 12 j / > 12 j)**. The
norm data itself stays on Drive (copyrighted); this file only says where to
find it and how she uses it.

| Test | Source | Groups | Output in report |
|---|---|---|---|
| AVLT (Vlaamse versie, vorm A) | `Normen.xlsx` sheet `AVLT(1)` = Vingerhoets, *Updated and extended Flemish normative data*, tables 1-2 | sex × educ × age ≤30 / 30–50 / >50 | `Z =` per trial; A8+ / A8− as percentile band from the percentile table |
| Complexe Figuur van Rey | `Normen.xlsx` sheet `CFT` (Vingerhoets) | sex × educ × age ≤30 / 30–50 / >50 | `Z =` + time in seconds |
| CFT drawing strategy | `Scoringssystemen CFT.docx` (RCF-OSS levels 1–7, Craeynest 2017) | – | wording such as "gefragmenteerde werkwijze" |
| COWAT | `Normen.xlsx` sheet `COWAT` (Vingerhoets) | educ × age by decade (20–29 … 70+) | `Z =` |
| Bourdon-Wiersma | `Normen.xlsx` sheets `Bourdon_invul` (row times) and `Bourdon Wiersma` (Vingerhoets) | age by decade; omissions also by educ | `Z =` for ART, AD, omissions, errors (as in the template; the workbook also gives percentiles) |
| D-KEFS Tower | `TOL.pdf` tables A.1–A.6, or `Normen.xlsx` sheet `Tower of London` | age 8 … 80–89 | `GS =`; rule violations as `Cum. % =` |
| WAIS-IV-NL (VL) | `WAIS.pdf`: table A.1 (subtests per age group), C.1 (CRV/CRA process scores), A.5 (VSI) | 16–17 … 75–84 (e.g. 45:0–54:11, 55:0–64:11) | `GS =`; VSI with pct and 95% BI |
| RDS | derived from digit span | – | value + "Cut-off ≤7" |
| VAT lange vorm | `VAT.pdf` table 3 (neurological patients 16–62 y) | – | `Pct.` |
| Kubus-Klok | `Scoreformulier Kubus Klok Tekentest.docx` | – | qualitative remark |
| BDI-II-NL | `BDI.pdf`: 0–13 minimaal, 14–19 licht, 20–28 matig ernstig, 29–63 ernstig | – | total + category; items ≥ 1 in remark |
| SCL-90 | N-norms (general population) in `Vragenlijst 2.xls`, sheet `Score` | – | raw score + zeer laag … zeer hoog; items ≥ 3 in remark |

## Classification (her `Scorehulpmiddel`)

| Label | Z | Percentile | GS | T |
|---|---|---|---|---|
| zeer hoog | ≥ 2,00 | ≥ 98 | ≥ 16 | ≥ 70 |
| hoog | 1,33 – 1,99 | 91 – 97 | 14 – 15 | 64 – 69 |
| hooggemiddeld | 0,67 – 1,32 | 75 – 90 | 12 – 13 | 57 – 63 |
| gemiddeld | −0,67 – 0,66 | 25 – 74 | 8 – 11 | 44 – 56 |
| laaggemiddeld | −1,33 – −0,68 | 9 – 24 | 6 – 7 | 37 – 43 |
| laag | −2,00 – −1,34 | 3 – 8 | 4 – 5 | 30 – 36 |
| zeer laag | ≤ −2,01 | ≤ 2 | ≤ 3 | ≤ 29 |

For times (Bourdon), she reports Z = (x − M)/SD without flipping the sign, so
a positive Z means slower.

## SCL-90 item key (Arrindell & Ettema)

- AGO: 13 25 47 50 70 75 82
- ANG: 2 17 23 33 39 57 72 78 80 86
- DEP: 3 5 14 15 19 20 22 26 29 30 31 32 51 54 59 79
- SOM: 1 4 12 27 40 42 48 49 52 53 56 58
- IN: 9 10 28 38 45 46 55 65 71
- SEN: 6 7 8 18 21 34 35 36 37 41 43 61 68 69 73 76 83 88
- HOS: 11 24 63 67 74 81
- SLA: 44 64 66
- OVER: 16 60 62 77 84 85 87 89 90

## Reading WAIS tables from the extracted text

The PDF is often too large to download. The text from `read_file_content` for
table A.1 lists, per scaled score, the columns
`BP OV CR MR WS RE SZ FS IN SSC CLN GW BG FZ OT`. Parse only rows that are
clean, and check the column against a known case before using it. For
example, her 61-year-old reference case in 55:0–64:11 gives SZ 21 → GS 6,
SSC 36 → GS 4, and sum 10 → VSI 73, pct 4, BI 67–86. Note in the report that
you read the table from text.
