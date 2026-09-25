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


class ClassificationTests(unittest.TestCase):
    def test_bands(self):
        bands = scoring.load_classification()
        self.assertEqual(scoring.classify(0, bands), "Average")
        self.assertEqual(scoring.classify(-1.3, bands), "Average")
        self.assertEqual(scoring.classify(-1.31, bands), "Below average")
        self.assertEqual(scoring.classify(-5, bands), "Well below average")


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
