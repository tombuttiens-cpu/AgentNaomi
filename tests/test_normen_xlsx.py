"""Checks against Naomi's Normen.xlsx. Runs only when NORMEN_XLSX points to it
(the workbook holds copyrighted norms and is not stored in this repository)."""
import os
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "tools"))

import scoring  # noqa: E402

PATH = os.environ.get("NORMEN_XLSX")


@unittest.skipUnless(PATH, "set NORMEN_XLSX to her Normen.xlsx to run")
class NormenTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import normen_xlsx
        cls.nx = normen_xlsx
        cls.wb = normen_xlsx.load(PATH)

    def test_reference_case_61(self):
        """Her example report: man, 61 y, <=12 j."""
        a = self.nx.avlt_norms(self.wb, "man", "<=12", 61)
        self.assertEqual(scoring.z_workbook(5, *a["A1"]), -0.39)
        self.assertEqual(scoring.z_workbook(52, *a["Som"]), 0.84)
        self.assertEqual(self.nx.avlt_recognition_pct(self.wb, "man", "<=12", 61, 14, 0),
                         ("Pct. 50-70", "> Pct. 80"))
        c = self.nx.cowat_norms(self.wb, "<=12", 61)
        self.assertEqual(scoring.z_workbook(3, *c["A"]), -2.23)
        b = self.nx.bourdon_norms(self.wb, "<=12", 61)
        self.assertEqual(scoring.z_workbook(16.92, *b["ART"]), 0.52)
        self.assertEqual(scoring.z_workbook(13, *b["Weglatingen"]), 0.06)
        f = self.nx.cft_norms(self.wb, "man", "<=12", 61)
        self.assertEqual(scoring.z_workbook(32, *f["Kopie"]), -0.27)

    def test_case_1_53(self):
        a = self.nx.avlt_norms(self.wb, "man", "<=12", 53)
        self.assertEqual(scoring.z_workbook(4, *a["A1"]), -0.94)
        f = self.nx.cft_norms(self.wb, "man", "<=12", 53)
        self.assertEqual(scoring.z_workbook(21.5, *f["OR"]), 0.40)

    def test_no_group_raises(self):
        with self.assertRaises(scoring.NormNotFound):
            self.nx.cowat_norms(self.wb, "<=12", 18)


class BourdonRawTests(unittest.TestCase):
    def test_first_25_rows(self):
        import normen_xlsx
        rows = [15] * 25 + [10] * 20
        r = normen_xlsx.bourdon_raw(rows, {3: 1, 30: 2}, {})
        self.assertEqual(r["ART"], 15)
        self.assertEqual(r["AD"], 0)
        self.assertEqual(r["Weglatingen"], 1)


class AdjectiveTests(unittest.TestCase):
    def test_forms(self):
        self.assertEqual(scoring.adjective("gemiddeld"), "gemiddelde")
        self.assertEqual(scoring.adjective("laag"), "lage")
        self.assertEqual(scoring.class_for_lower_is_better(0.76), "laaggemiddeld")
