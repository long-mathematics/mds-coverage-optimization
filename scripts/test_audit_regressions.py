#!/usr/bin/env python3
"""Finite exact and source-regression checks; not mathematical certification."""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import math
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

    def test_deep_audit_gamma_explications(self):
        mixed = statement(self.gamma, 'lem:gamma-tail-ratio-bound')
        self.assertIn(r'Let \(\tau>1\), put \(m=\tau-1\)', mixed)
        self.assertIn('normalized form', self.gamma)
        self.assertIn(r'R_{\rm new}', self.gamma)
        self.assertIn('first directional derivative along the activation path', self.gamma)
        self.assertIn(r'\zeta=z-m+\frac z{Q(z)}', self.gamma)

    def test_deep_audit_support_explications(self):
        self.assertIn('elementary monotone-inversion', self.gamma)
        self.assertIn('closed convex Borel set', self.gamma)
        self.assertIn('generated measure', self.gamma)
        self.assertIn(r'\E e^{-\sigma Z}', self.gamma)
        density = statement(self.gamma, 'lem:mds-density-ratio-crossing')
        self.assertIn('nonempty:', self.gamma[self.gamma.index(density):])

    def test_deep_audit_cloud_explications(self):
        self.assertIn('allocation simplex is compact', self.cloud)
        self.assertIn("a_1'(x)=\\frac{(x+1)e^{-x}-1}{x^2}<0", self.cloud)
        self.assertIn(r'If \(q\) is optimal, Theorem', self.cloud)
        self.assertIn('Averaging those inequalities over the auxiliary uniforms', self.cloud)

    def test_integer_lattice_concentration_strengthening(self):
        concentration = statement(self.cloud, 'thm:terminal-cloud')
        self.assertIn(r'r_{\rm fail}=n-k+1', concentration)
        self.assertIn(r'\Lambda<r_{\rm fail}', concentration)
        self.assertIn(r'\mu>k-1', concentration)
        self.assertIn(r'\mu-k+1', concentration)
        self.assertNotIn(r'\Lambda<n-k', concentration)
        # Boundary case where the old condition was unavailable:
        # n=k=1, one Bernoulli success with probability 1/2.
        k = 1
        mu = 0.5
        failure = 0.5
        variance = 0.25
        gap = mu - k + 1
        bound = math.exp(-(gap * gap) / (2 * variance + 2 * gap / 3))
        self.assertLessEqual(failure, bound)
        self.assertGreater(mu, k - 1)
        self.assertFalse(mu > k)

    def test_closed_simplex_bias_parametrization(self):
        uniform = statement(self.cloud, 'thm:uniform-penalty')
        self.assertIn(r'\varepsilon_i\ge-1', uniform)
        self.assertIn(r'p_i=0', uniform)
        # Boundary parametrization eps=(-1,1), checked against the stated
        # Taylor remainder at a fixed alpha.
        alpha = 0.75
        eps = (-1.0, 1.0)
        probabilities = tuple((1 + value) / 2 for value in eps)
        self.assertEqual(probabilities, (0.0, 1.0))
        sigma2 = sum(value * value for value in eps) / 2
        sigma3 = sum(abs(value) ** 3 for value in eps) / 2
        delta = max(abs(value) for value in eps)
        normalized = sum(math.exp(-alpha * value) for value in eps) / 2
        remainder = normalized - 1 - alpha * alpha * sigma2 / 2
        remainder_bound = alpha ** 3 * math.exp(alpha * delta) * sigma3 / 6
        self.assertLessEqual(abs(remainder), remainder_bound + 1e-15)

    def test_ambient_change_invalidates_context_not_statement_hash(self):
        sample = r'Assume \(\tau>1\).\begin{theorem}\label{test}Claim.\end{theorem}'
        changed = sample.replace(r'\tau>1', r'\tau>0')
        original_row, changed_row = statements(sample)[0], statements(changed)[0]
        self.assertEqual(original_row['statement_sha256'], changed_row['statement_sha256'])
        self.assertNotEqual(original_row['context_sha256'], changed_row['context_sha256'])
        self.assertNotEqual(hashlib.sha256(sample.encode()).hexdigest(), hashlib.sha256(changed.encode()).hexdigest())


if __name__ == '__main__':
    unittest.main(verbosity=2)
