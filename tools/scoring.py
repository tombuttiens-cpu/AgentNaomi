"""Deterministic scoring engine for neuropsychological test results.

All arithmetic happens here, never in the language model. The agent calls
`python tools/score_case.py <case-folder>` and only *reports* what this
module produces.

Two norm types are supported (see norms/README.md):
  * meansd - norm group mean and SD, selected by age band and education
  * table  - a raw-score -> standard-score lookup table (e.g. scaled scores)
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
NORMS_DIR = ROOT / "norms"


# ---------------------------------------------------------------------------
# Score conversions
# ---------------------------------------------------------------------------

def z_from_raw(raw: float, mean: float, sd: float, higher_is_better: bool = True) -> float:
    """z-score, sign-corrected so that a negative z always means 'worse'."""
    if sd <= 0:
        raise ValueError(f"SD must be positive, got {sd}")
    z = (raw - mean) / sd
    return z if higher_is_better else -z


def percentile_from_z(z: float) -> float:
    """Percentile rank (0-100) under the normal distribution."""
    return 50.0 * (1.0 + math.erf(z / math.sqrt(2.0)))


def z_to_t(z: float) -> float:
    return 50.0 + 10.0 * z


def z_to_scaled(z: float) -> float:
    """Wechsler-style scaled score (mean 10, SD 3)."""
    return 10.0 + 3.0 * z


def z_to_standard(z: float) -> float:
    """Standard/index score (mean 100, SD 15)."""
    return 100.0 + 15.0 * z


def z_from_standard(score: float, mean: float, sd: float) -> float:
    return (score - mean) / sd


SCALES = {
    # name: (mean, sd)
    "z": (0.0, 1.0),
    "t": (50.0, 10.0),
    "scaled": (10.0, 3.0),
    "standard": (100.0, 15.0),
}


# ---------------------------------------------------------------------------
# Classification (labels live in norms/classification.csv so she can edit them)
# ---------------------------------------------------------------------------

@dataclass(frozen=True)
class Band:
    z_min: float  # inclusive
    label: str


def load_classification(path: Path | None = None) -> list[Band]:
    path = path or NORMS_DIR / "classification.csv"
    with open(path, newline="", encoding="utf-8") as f:
        bands = [Band(float(r["z_min"]), r["label"].strip()) for r in csv.DictReader(f)]
    return sorted(bands, key=lambda b: b.z_min, reverse=True)


def classify(z: float, bands: list[Band]) -> str:
    for band in bands:
        if z >= band.z_min:
            return band.label
    return bands[-1].label


# ---------------------------------------------------------------------------
# Norm lookup
# ---------------------------------------------------------------------------

class NormNotFound(LookupError):
    pass


@dataclass
class Norm:
    test: str
    measure: str
    kind: str                 # "meansd" or "table"
    higher_is_better: bool
    mean: float | None = None
    sd: float | None = None
    table: str | None = None  # file name in norms/tables/
    scale: str | None = None  # scale of the table output (scaled, t, standard)
    source: str = ""


def _matches(row: dict, age: float, education: str) -> bool:
    if not (float(row["age_min"]) <= age <= float(row["age_max"])):
        return False
    edu = row.get("education", "").strip()
    return edu in ("", "*") or edu.lower() == education.lower()


def find_norm(test: str, measure: str, age: float, education: str,
              norms_file: Path | None = None) -> Norm:
    norms_file = norms_file or NORMS_DIR / "norms.csv"
    with open(norms_file, newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f)
                if r["test"].strip().lower() == test.lower()
                and r["measure"].strip().lower() == measure.lower()
                and _matches(r, age, education)]
    if not rows:
        raise NormNotFound(f"No norm for {test}/{measure} at age {age}, education '{education}'")
    # Prefer an education-specific row over a wildcard one.
    rows.sort(key=lambda r: r.get("education", "").strip() in ("", "*"))
    r = rows[0]
    kind = r["kind"].strip().lower()
    return Norm(
        test=r["test"].strip(),
        measure=r["measure"].strip(),
        kind=kind,
        higher_is_better=r["direction"].strip().lower() in ("higher", "higher_is_better", "+"),
        mean=float(r["mean"]) if r.get("mean") else None,
        sd=float(r["sd"]) if r.get("sd") else None,
        table=r.get("table", "").strip() or None,
        scale=r.get("scale", "").strip().lower() or None,
        source=r.get("source", "").strip(),
    )


def lookup_table(table: str, raw: float) -> float:
    """Raw -> score from a lookup table with columns raw_min, raw_max, score."""
    path = NORMS_DIR / "tables" / table
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            if float(r["raw_min"]) <= raw <= float(r["raw_max"]):
                return float(r["score"])
    raise NormNotFound(f"Raw score {raw} is outside the range of table {table}")


# ---------------------------------------------------------------------------
# Scoring one result
# ---------------------------------------------------------------------------

@dataclass
class Scored:
    test: str
    measure: str
    raw: float
    z: float
    percentile: float
    t: float
    scaled: float
    standard: float
    classification: str
    norm_source: str


def score(test: str, measure: str, raw: float, age: float, education: str,
          bands: list[Band] | None = None, norms_file: Path | None = None) -> Scored:
    bands = bands or load_classification()
    norm = find_norm(test, measure, age, education, norms_file)
    if norm.kind == "meansd":
        if norm.mean is None or norm.sd is None:
            raise ValueError(f"Norm for {test}/{measure} is missing mean or sd")
        z = z_from_raw(raw, norm.mean, norm.sd, norm.higher_is_better)
    elif norm.kind == "table":
        if not norm.table or norm.scale not in SCALES:
            raise ValueError(f"Table norm for {test}/{measure} needs 'table' and a valid 'scale'")
        m, s = SCALES[norm.scale]
        z = z_from_standard(lookup_table(norm.table, raw), m, s)
        # Tables are expected to already encode direction; no sign flip here.
    else:
        raise ValueError(f"Unknown norm kind '{norm.kind}'")
    return Scored(
        test=norm.test, measure=norm.measure, raw=raw, z=z,
        percentile=percentile_from_z(z), t=z_to_t(z), scaled=z_to_scaled(z),
        standard=z_to_standard(z), classification=classify(z, bands),
        norm_source=norm.source,
    )
