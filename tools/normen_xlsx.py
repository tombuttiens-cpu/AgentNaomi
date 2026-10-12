"""Read norm groups directly from Naomi's Normen.xlsx (her scoring workbook).

The workbook holds the Vingerhoets (Flemish) norm tables she uses for AVLT,
CFT, COWAT and Bourdon-Wiersma. Reading them from her own file means no norm
values are typed by hand and none are stored in this repository.

    wb = load("Normen.xlsx")
    avlt_norms(wb, "man", "<=12", 53)  -> {"A1": (5.7, 1.8), ...}

Every function raises NormNotFound when no group fits (hard rule 3:
stop and ask her).
"""

from __future__ import annotations

import openpyxl

from scoring import NormNotFound


def load(path):
    return openpyxl.load_workbook(path, data_only=True)


def _sex(sex: str) -> str:
    s = sex.strip().lower()
    if s in ("man", "m", "male", "meneer"):
        return "man"
    if s in ("vrouw", "v", "f", "female", "mevrouw"):
        return "vrouw"
    raise NormNotFound(f"Onbekend geslacht: {sex!r}")


def _edu(edu: str) -> str:
    e = edu.replace(" ", "").replace("j", "").lower()
    if e in ("<=12", "≤12", "tem12", "lager", "laag"):
        return "<=12"
    if e in (">12", "hoger", "hoog"):
        return ">12"
    raise NormNotFound(f"Onbekend opleidingsniveau: {edu!r} (gebruik '<=12' of '>12')")


def _band3(age: float) -> int:
    """AVLT/CFT age bands as in her workbook (Variabelen): <=30, 31-50, >50."""
    if age < 31:
        return 0
    if age < 51:
        return 1
    return 2


def _decade(age: float) -> int:
    """COWAT/Bourdon bands: 20-29, 30-39, 40-49, 50-59, 60-69, 70+."""
    if age < 20:
        raise NormNotFound(f"Geen normgroep onder 20 jaar (leeftijd {age})")
    return min(int(age // 10) - 2, 5)


def _col(index: int) -> str:
    return openpyxl.utils.get_column_letter(index)


def _mean_sd(ws, row: int, first_col: int) -> tuple[float, float]:
    m = ws[f"{_col(first_col)}{row}"].value
    sd = ws[f"{_col(first_col + 1)}{row}"].value
    if m is None or sd is None:
        raise NormNotFound(f"Lege normcel in {ws.title} rij {row}")
    return float(m), float(sd)


# ----------------------------------------------------------------- AVLT

AVLT_ROWS = {"A1": 20, "A2": 21, "A3": 22, "A4": 23, "A5": 24, "Som": 25,
             "B1": 26, "A6": 27, "A7": 28, "A8+": 29, "A8-": 30}


def avlt_norms(wb, sex, edu, age) -> dict:
    """Mean/SD per trial. Sheet AVLT(1) rows 20-30, column pairs from B:
    man <=12 (<=30, 30-50, >50), man >12 (...), vrouw <=12, vrouw >12."""
    ws = wb["AVLT(1)"]
    group = {"man": 0, "vrouw": 6}[_sex(sex)] + {"<=12": 0, ">12": 3}[_edu(edu)] + _band3(age)
    first_col = 2 + 2 * group
    return {k: _mean_sd(ws, r, first_col) for k, r in AVLT_ROWS.items()}


def avlt_recognition_pct(wb, sex, edu, age, hits: int, false_pos: int) -> tuple[str, str]:
    """Percentile labels for A8+ and A8- from the workbook's lookup blocks
    (rows 45-53 for A8+, rows 79-87 for A8-): label column + threshold column."""
    ws = wb["AVLT(1)"]
    group = {"man": 0, "vrouw": 6}[_sex(sex)] + {"<=12": 0, ">12": 3}[_edu(edu)] + _band3(age)
    label_col, thr_col = 1 + 2 * group, 2 + 2 * group

    def scan(rows, value, higher_is_better):
        entries = []
        for r in rows:
            lab = ws[f"{_col(label_col)}{r}"].value
            thr = ws[f"{_col(thr_col)}{r}"].value
            if lab is not None and thr is not None:
                entries.append((str(lab), float(thr)))
        if not entries:
            raise NormNotFound("Geen A8-percentieltabel voor deze groep")
        first_label, first_thr = entries[0]
        if higher_is_better:
            # workbook: IF(score < first threshold) -> first label, else exact match
            if value < first_thr:
                return first_label
            for lab, thr in entries[1:]:
                if value <= thr:
                    return lab
            return entries[-1][0]
        # false positives: IF(score > first threshold) -> first label, else match
        if value > first_thr:
            return first_label
        for lab, thr in entries[1:]:
            if value >= thr:
                return lab
        return entries[-1][0]

    return scan(range(45, 54), hits, True), scan(range(79, 88), false_pos, False)


# ----------------------------------------------------------------- CFT

def cft_norms(wb, sex, edu, age) -> dict:
    """Sheet CFT: men rows 12-14, women rows 20-22; triplets (M, SD, Z) from B:
    <=12 (<=30, 30-50, >50), >12 (...)."""
    ws = wb["CFT"]
    base = {"man": 12, "vrouw": 20}[_sex(sex)]
    group = {"<=12": 0, ">12": 3}[_edu(edu)] + _band3(age)
    first_col = 2 + 3 * group
    return {k: _mean_sd(ws, base + i, first_col) for i, k in enumerate(["Kopie", "OR", "UR"])}


# ----------------------------------------------------------------- COWAT

def cowat_norms(wb, edu, age) -> dict:
    """Sheet COWAT rows 15-19 (Dieren, Beroepen, N, A, K), pairs from B:
    <=12 by decade, then >12 by decade. Men and women combined."""
    ws = wb["COWAT"]
    group = {"<=12": 0, ">12": 6}[_edu(edu)] + _decade(age)
    first_col = 2 + 2 * group
    keys = ["Dieren", "Beroepen", "N", "A", "K"]
    return {k: _mean_sd(ws, 15 + i, first_col) for i, k in enumerate(keys)}


# ----------------------------------------------------------------- Bourdon

def bourdon_norms(wb, edu, age) -> dict:
    """Sheet 'Bourdon Wiersma' rows 14-17 (ART, AD, Fouten, Omissies), pairs from
    B by decade. Omissions in the workbook are the <=12 j group only."""
    ws = wb["Bourdon Wiersma"]
    first_col = 2 + 2 * _decade(age)
    out = {k: _mean_sd(ws, 14 + i, first_col) for i, k in enumerate(["ART", "AD", "Fouten"])}
    if _edu(edu) != "<=12":
        raise NormNotFound("Omissienormen > 12 j staan niet in Normen.xlsx: vraag Naomi "
                           "(Vingerhoets tabel 6 bevat ze wel).")
    out["Weglatingen"] = _mean_sd(ws, 17, first_col)
    return out


def bourdon_raw(row_times: list[float], omissions_per_row: dict[int, int] | None = None,
                errors_per_row: dict[int, int] | None = None, n_rows: int = 25) -> dict:
    """Her method (feedback 11/10/2026): average row time, average deviation
    (Excel AVEDEV), omissions and errors over the FIRST 25 ROWS only."""
    first = row_times[:n_rows]
    art = sum(first) / len(first)
    ad = sum(abs(t - art) for t in first) / len(first)
    om = sum(v for r, v in (omissions_per_row or {}).items() if r <= n_rows)
    err = sum(v for r, v in (errors_per_row or {}).items() if r <= n_rows)
    return {"ART": art, "AD": ad, "Weglatingen": om, "Fouten": err}
