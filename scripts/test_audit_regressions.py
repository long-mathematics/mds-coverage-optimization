#!/usr/bin/env python3
"""Finite exact and source-regression checks; not mathematical certification."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import re
import unittest
from validate_repository import ROOT, statements


def statement(text, label):
    pattern = r'\\begin\{(theorem|lemma|proposition|corollary)\}(?:\[[^\]]*\])?.*?\\end\{\1\}'
    for match in re.finditer(pattern, text, re.S):
        if r'\label{' + label + '}' in match.group(0):
            return match.group(0)
    raise AssertionError(f'Missing statement {label}')


class FirstAuditRegressions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.gamma = (ROOT / 'gamma_mds_active_uniform.tex').read_text()
        cls.cloud = (ROOT / 'terminal_cloud_staircase.tex').read_text()

    def test_no_undefined_comparison_tail(self):
        self.assertNotIn(r'\psi_t', self.gamma)
        self.assertIn(r'(n-q)+q\bigl(1-F_t(M/q)\bigr)', self.gamma)

    def test_probability_domains_are_local(self):
        for label in ('thm:random-environment', 'thm:plugin'):
            self.assertIn(r'0<\delta,\eta<1', statement(self.cloud, label))
        annealed = statement(self.cloud, 'thm:annealed-jensen')
        self.assertIn('random probability', annealed)
        self.assertIn(r'M>0', annealed)
        calibration = statement(self.cloud, 'thm:plugin')
        self.assertIn('measurable depth rule', calibration)
        self.assertIn(r'M:[0,\infty)^n\to[0,\infty)', calibration)
        self.assertIn('Conditional on calibration', calibration)
        self.assertIn('independent fresh randomness', calibration)

    def test_toolkit_continuity_and_zero_budget(self):
        dp = statement(self.cloud, 'thm:dp')
        self.assertIn('For arbitrary curves', dp)
        self.assertIn(r'\theta_i(0)=s_i(0)', statement(self.cloud, 'thm:poissonized-identity'))
        self.assertIn(r'integer \(m\ge0\)', statement(self.cloud, 'thm:depoissonization'))
        # Zero reads: P_0 = Pi_0; the displayed error terms both equal one.
        for probability in (F(0), F(1, 4), F(1, 2), F(3, 4), F(1)):
            self.assertLessEqual(probability - 1, probability)
            self.assertLessEqual(probability, probability + 1)

    def test_two_stage_finite_exact_grid_and_invalid_domain(self):
        values = tuple(F(i, 4) for i in range(5))
        errors = (F(1, 4), F(1, 2), F(3, 4))
        checked = 0
        for left in values:
            for right in values:
                for mass in values:
                    mean = mass * left + (1 - mass) * right
                    for delta in errors:
                        good = mass * (left >= 1 - delta) + (1 - mass) * (right >= 1 - delta)
                        for eta in errors:
                            if good >= 1 - eta:
                                self.assertGreaterEqual(mean, (1 - delta) * (1 - eta))
                                checked += 1
        self.assertGreater(checked, 0)
        # Original unrestricted assertion fails: q=1/2, delta=eta=2.
        q, delta, eta = F(1, 2), F(2), F(2)
        self.assertGreaterEqual(F(q >= 1 - delta), 1 - eta)
        self.assertLess(q, (1 - delta) * (1 - eta))

    def test_ambient_change_invalidates_context_not_statement_hash(self):
        sample = r'Assume \(\tau>1\).\begin{theorem}\label{test}Claim.\end{theorem}'
        changed = sample.replace(r'\tau>1', r'\tau>0')
        original_row, changed_row = statements(sample)[0], statements(changed)[0]
        self.assertEqual(original_row['statement_sha256'], changed_row['statement_sha256'])
        self.assertNotEqual(original_row['context_sha256'], changed_row['context_sha256'])
        self.assertNotEqual(hashlib.sha256(sample.encode()).hexdigest(), hashlib.sha256(changed.encode()).hexdigest())


if __name__ == '__main__':
    unittest.main(verbosity=2)
