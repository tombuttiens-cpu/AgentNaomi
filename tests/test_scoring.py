import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import scoring  # noqa: E402


class ConversionTests(unittest.TestCase):
    def test_z_direction(self):
        self.assertAlmostEqual(scoring.z_from_raw(60, 50, 10), 1.0)
        self.assertAlmostEqual(scoring.z_from_raw(60, 50, 10, higher_is_better=False), -1.0)

    def test_percentile(self):
        self.assertAlmostEqual(scoring.percentile_from_z(0), 50.0)
        self.assertAlmostEqual(scoring.percentile_from_z(-1.645), 5.0, places=1)
        self.assertAlmostEqual(scoring.percentile_from_z(1.96), 97.5, places=1)

    def test_scales(self):
        self.assertEqual(scoring.z_to_t(-1), 40)
        self.assertEqual(scoring.z_to_scaled(-1), 7)
        self.assertEqual(scoring.z_to_standard(-1), 85)

    def test_bad_sd(self):
        with self.assertRaises(ValueError):
            scoring.z_from_raw(1, 1, 0)


class WorkbookTests(unittest.TestCase):
    """Values her Normen.xlsx computed (cached cell values), reproduced exactly."""

    def test_reproduces_workbook(self):
        cases = [  # raw, M, SD, workbook result
            (4, 5.7, 1.8, -0.94), (7, 10.6, 2.3, -1.57), (30, 44.9, 8.5, -1.75),
            (6, 8, 3, -0.67), (32, 32.7, 2.6, -0.27), (21.5, 19, 6.2, 0.4),
            (23.5, 17.5, 6.3, 0.95), (2, 10.9, 4, -2.23), (4, 12.4, 4.3, -1.95),
        ]
        for raw, m, sd, expected in cases:
            self.assertEqual(scoring.z_workbook(raw, m, sd), expected, (raw, m, sd))

    def test_half_away_from_zero(self):
        self.assertEqual(scoring.excel_round(-2.225), -2.23)
        self.assertEqual(scoring.excel_round(2.225), 2.23)

    def test_format(self):
        self.assertEqual(scoring.format_z(-0.94), "Z = -0,94")
        self.assertEqual(scoring.format_z(-1.6), "Z = -1,60")


class ClassificationTests(unittest.TestCase):
    """Her Scorehulpmiddel bands."""

    def test_bands(self):
        bands = scoring.load_classification()
        expect = {2.0: "zeer hoog", 1.99: "hoog", 1.33: "hoog", 1.32: "hooggemiddeld",
                  0.67: "hooggemiddeld", 0.66: "gemiddeld", -0.67: "gemiddeld",
                  -0.68: "laaggemiddeld", -1.33: "laaggemiddeld", -1.34: "laag",
                  -2.0: "laag", -2.01: "zeer laag"}
        for z, label in expect.items():
            self.assertEqual(scoring.classify(z, bands), label, z)


class NormLookupTests(unittest.TestCase):
    def test_age_band(self):
        young = scoring.score("EXAMPLE-MEMORY", "total recall", 45, 30, "high")
        old = scoring.score("EXAMPLE-MEMORY", "total recall", 40, 70, "high")
        self.assertAlmostEqual(young.z, 0)
        self.assertAlmostEqual(old.z, 0)

    def test_education_and_lower_is_better(self):
        r = scoring.score("EXAMPLE-SPEED", "time (s)", 54, 40, "high")
        self.assertAlmostEqual(r.z, -1.0)

    def test_table(self):
        r = scoring.score("EXAMPLE-SUBTEST", "raw", 17, 40, "low")
        self.assertAlmostEqual(r.scaled, 10)

    def test_missing_norm(self):
        with self.assertRaises(scoring.NormNotFound):
            scoring.score("NOPE", "x", 1, 40, "high")
        with self.assertRaises(scoring.NormNotFound):
            scoring.score("EXAMPLE-MEMORY", "total recall", 10, 95, "high")


if __name__ == "__main__":
    unittest.main()
