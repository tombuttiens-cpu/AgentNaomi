"""Score all raw test results in a case folder.

Usage:
    python tools/score_case.py cases/<CASE-ID>

Reads:
    <CASE-ID>_INFO.txt     demographics needed for norm selection
    <CASE-ID>_SCORES.csv   raw scores (columns: test, measure, raw)

Writes (into <case>/output/):
    <CASE-ID>_SCORED.csv   full results, machine readable
    <CASE-ID>_SCORED.md    results table for the report
    <CASE-ID>_ISSUES.md    anything that could not be scored (only if needed)
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from scoring import NormNotFound, load_classification, score  # noqa: E402

REQUIRED_INFO = ("age", "education")


def read_info(path: Path) -> dict[str, str]:
    info: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, value = line.split(":", 1)
        info[key.strip().lower()] = value.strip()
    missing = [k for k in REQUIRED_INFO if not info.get(k)]
    if missing:
        raise SystemExit(f"{path.name} is missing required field(s): {', '.join(missing)}")
    return info


def find_one(folder: Path, suffix: str) -> Path:
    matches = sorted(folder.glob(f"*_{suffix}"))
    if len(matches) != 1:
        raise SystemExit(f"Expected exactly one *_{suffix} in {folder}, found {len(matches)}")
    return matches[0]


def fmt(x: float, digits: int = 1) -> str:
    return f"{x:.{digits}f}".replace("-0.0", "0.0")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2
    folder = Path(argv[1])
    case_id = folder.name
    info = read_info(find_one(folder, "INFO.txt"))
    age = float(info["age"])
    education = info["education"]
    bands = load_classification()

    results, issues = [], []
    with open(find_one(folder, "SCORES.csv"), newline="", encoding="utf-8") as f:
        for i, row in enumerate(csv.DictReader(f), start=2):
            test, measure, raw = row["test"].strip(), row["measure"].strip(), row["raw"].strip()
            if not raw:
                issues.append(f"Line {i}: {test}/{measure} has no raw score (not administered?)")
                continue
            try:
                results.append(score(test, measure, float(raw.replace(",", ".")), age, education, bands))
            except (NormNotFound, ValueError) as e:
                issues.append(f"Line {i}: {e}")

    out = folder / "output"
    out.mkdir(exist_ok=True)
    with open(out / f"{case_id}_SCORED.csv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["test", "measure", "raw", "z", "percentile", "t", "scaled",
                    "standard", "classification", "norm_source"])
        for r in results:
            w.writerow([r.test, r.measure, r.raw, round(r.z, 2), round(r.percentile, 1),
                        round(r.t, 1), round(r.scaled, 1), round(r.standard, 1),
                        r.classification, r.norm_source])

    lines = [f"# Scores {case_id}", "",
             f"Age: {info['age']} · Education: {education}", "",
             "| Test | Measure | Raw | z | Percentile | Classification |",
             "|---|---|---|---|---|---|"]
    for r in results:
        lines.append(f"| {r.test} | {r.measure} | {r.raw:g} | {fmt(r.z, 2)} | "
                     f"{fmt(r.percentile)} | {r.classification} |")
    (out / f"{case_id}_SCORED.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    issues_path = out / f"{case_id}_ISSUES.md"
    if issues:
        issues_path.write_text("# Could not score\n\n" + "\n".join(f"- {x}" for x in issues) + "\n",
                               encoding="utf-8")
    elif issues_path.exists():
        issues_path.unlink()

    print(f"Scored {len(results)} measure(s), {len(issues)} issue(s). Output in {out}")
    for x in issues:
        print(f"  ! {x}")
    return 1 if issues else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
