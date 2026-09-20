import csv
import math
import tempfile
import unittest
from pathlib import Path

from tools.fearprime_bayesian_calculator import derive_row
from tools.fearprime_model_compare import Trial, fit_all


class CalculatorTests(unittest.TestCase):
    def test_accommodation_like_row(self):
        row = {
            "pre_threat_expectancy": "80",
            "observed_severity": "0",
            "post_threat_expectancy": "40",
            "evidence_credibility": "90",
            "evidence_relevance": "80",
            "pre_generalized_belief": "70",
            "post_generalized_belief": "55",
            "next_day_threat_expectancy": "50",
            "generalization_pre_expectancy": "75",
            "generalization_post_expectancy": "50",
        }
        out = derive_row(row)
        self.assertEqual(float(out["calc_pe_signed"]), -80.0)
        self.assertEqual(float(out["calc_pe_absolute"]), 80.0)
        self.assertEqual(float(out["calc_expectancy_update"]), -40.0)
        self.assertEqual(out["calc_inferred_violex_response"], "accommodation_like")
        self.assertAlmostEqual(float(out["calc_retention_fraction"]), 0.75)

    def test_immunization_like_row(self):
        row = {
            "pre_threat_expectancy": "80",
            "observed_severity": "0",
            "post_threat_expectancy": "78",
            "evidence_credibility": "95",
            "evidence_relevance": "95",
        }
        out = derive_row(row)
        self.assertEqual(out["calc_inferred_violex_response"], "immunization_like")
        self.assertGreater(
            float(out["calc_immunization_score"]),
            float(out["calc_accommodation_score"]),
        )


class ModelComparisonTests(unittest.TestCase):
    def test_all_models_return_finite_scores(self):
        raw = [
            (80, 0, 45, 90, 90, 10),
            (75, 20, 50, 85, 80, 20),
            (65, 10, 35, 95, 90, 10),
            (55, 30, 40, 80, 70, 30),
            (50, 0, 25, 90, 95, 5),
            (45, 20, 30, 70, 80, 40),
            (35, 10, 20, 95, 95, 5),
            (30, 0, 15, 95, 90, 0),
        ]
        trials = [
            Trial(pre, obs, post, cred, rel, safety)
            for pre, obs, post, cred, rel, safety in raw
        ]
        scored = fit_all(trials)
        self.assertEqual(len(scored), 5)
        self.assertEqual(scored[0][0].model, "rescorla_wagner")
        for _, metric in scored:
            self.assertTrue(math.isfinite(metric["bic"]))
            self.assertTrue(math.isfinite(metric["rmse"]))


if __name__ == "__main__":
    unittest.main()
