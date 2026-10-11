#!/usr/bin/env python3
"""Apply the two reviewed Paper II toolkit strengthenings.

This one-use branch script changes only the integer-lattice concentration
thresholds and the closed-simplex perturbative parametrization, together
with targeted tests and documentation.
"""
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parent


def replace(path: str, old: str, new: str) -> None:
    target = ROOT / path
    text = target.read_text()
    count = text.count(old)
    if count != 1:
        raise ValueError(f"{path}: expected one replacement anchor, found {count}: {old[:120]!r}")
    target.write_text(text.replace(old, new))


def append(path: str, text: str) -> None:
    target = ROOT / path
    target.write_text(target.read_text().rstrip() + "\n\n" + text.strip() + "\n")


expected_source = "dd5ac834f104ddbc04596b6b05c67b5e37ea4219ae89e34a1cea90e014b98529"
actual_source = hashlib.sha256((ROOT / "terminal_cloud_staircase.tex").read_bytes()).hexdigest()
if actual_source != expected_source:
    raise ValueError(f"Paper II input snapshot mismatch: {actual_source}")

replace(
    "terminal_cloud_staircase.tex",
    r"""An \([n,k]\) MDS code succeeds exactly when \(U_{M,t}\le n-k\).
For every \(s>0\),
\[
 \Pbb(U_{M,t}\ge\Lambda+s),\quad
 \Pbb(U_{M,t}\le\Lambda-s)
 \ \le\ \exp\!\left(-\frac{s^2}{2V+2s/3}\right).
\]
If \(\Lambda<n-k\), a sufficient failure bound is
\[
 \Pbb(\mathrm{failure})
 \le \exp\!\left(-\frac{(n-k-\Lambda)^2}
                         {2V+2(n-k-\Lambda)/3}\right).
\]
For general independent recovery indicators, let
\(\mu=\sum_i\theta_i\) and \(v=\sum_i\theta_i(1-\theta_i)\).
If \(\mu>k\), then
\[
 \Pbb\!\left(\sum_i B_i<k\right)
 \le\exp\!\left(-\frac{(\mu-k)^2}{2v+2(\mu-k)/3}\right).
\]
In particular, for \(0<\delta<1\), success probability is at least
\(1-\delta\) whenever
\[
 \mu-k\ge\sqrt{2v\log(1/\delta)}+\frac23\log(1/\delta).
\]""",
    r"""An \([n,k]\) MDS code succeeds exactly when \(U_{M,t}\le n-k\).
Thus the first failing defect count is
\[
 r_{\rm fail}=n-k+1.
\]
For every \(s>0\),
\[
 \Pbb(U_{M,t}\ge\Lambda+s),\quad
 \Pbb(U_{M,t}\le\Lambda-s)
 \ \le\ \exp\!\left(-\frac{s^2}{2V+2s/3}\right).
\]
If \(\Lambda<r_{\rm fail}\), then
\[
 \Pbb(\mathrm{failure})
 \le \exp\!\left(-\frac{(r_{\rm fail}-\Lambda)^2}
                         {2V+2(r_{\rm fail}-\Lambda)/3}\right).
\]
For general independent recovery indicators, let
\(\mu=\sum_i\theta_i\) and \(v=\sum_i\theta_i(1-\theta_i)\).
If \(\mu>k-1\), then
\[
 \Pbb\!\left(\sum_i B_i<k\right)
 \le\exp\!\left(-\frac{(\mu-k+1)^2}{2v+2(\mu-k+1)/3}\right).
\]
In particular, for \(0<\delta<1\), success probability is at least
\(1-\delta\) whenever
\[
 \mu-k+1\ge\sqrt{2v\log(1/\delta)}+\frac23\log(1/\delta).
\]
For the hard-threshold model, \(\mu=n-\Lambda\) and \(v=V\), so the
two lattice gaps agree:
\[
 \mu-k+1=r_{\rm fail}-\Lambda.
\]""",
)

replace(
    "terminal_cloud_staircase.tex",
    r"""The defect indicators are independent Bernoulli variables with
parameters \(\psi_t(Mp_i)\), giving the moment formulas and recovery
event. Apply Bernstein's inequality for independent centered variables
bounded by one \cite[Chapter~2]{BoucheronLugosiMassart2013}. Apply it
again to \(B_i-\theta_i\) for the general recovery bound. If
\(L=\log(1/\delta)\) and \(a\ge\sqrt{2vL}+2L/3\), direct expansion
gives \(a^2\ge L(2v+2a/3)\), proving the sufficient margin condition.""",
    r"""The defect indicators are independent Bernoulli variables with
parameters \(\psi_t(Mp_i)\), giving the moment formulas and recovery
event.  Since failure is exactly \(U_{M,t}\ge r_{\rm fail}\), apply
Bernstein's upper-tail inequality with
\(s=r_{\rm fail}-\Lambda>0\).  For general recovery indicators,
\(\sum_i B_i<k\) means \(\sum_iB_i\le k-1\), so Bernstein's lower-tail
inequality applies with displacement \(a=\mu-k+1>0\).  If
\(L=\log(1/\delta)\) and \(a\ge\sqrt{2vL}+2L/3\), direct expansion
gives \(a^2\ge L(2v+2a/3)\), proving the sufficient margin condition
\cite[Chapter~2]{BoucheronLugosiMassart2013}.""",
)

replace(
    "terminal_cloud_staircase.tex",
    r"""  p_i=\frac{1+\varepsilon_i}{n},
  \qquad \sum_{i=1}^n\varepsilon_i=0,
  \qquad \varepsilon_i>-1.
\]""",
    r"""  p_i=\frac{1+\varepsilon_i}{n},
  \qquad \sum_{i=1}^n\varepsilon_i=0,
  \qquad \varepsilon_i\ge-1.
\]
Thus the expansion includes boundary sampling laws with \(p_i=0\).""",
)

# Add focused source and numerical regressions.
test_path = ROOT / "scripts/test_audit_regressions.py"
test_text = test_path.read_text()
test_text = test_text.replace(
    "import hashlib\nimport re\nimport unittest\n",
    "import hashlib\nimport math\nimport re\nimport unittest\n",
)
anchor = "    def test_ambient_change_invalidates_context_not_statement_hash(self):\n"
if test_text.count(anchor) != 1:
    raise ValueError("Could not locate regression-test insertion point")
methods = r'''    def test_integer_lattice_concentration_strengthening(self):
        concentration = statement(self.cloud, 'thm:terminal-cloud')
        self.assertIn(r'r_{\rm fail}=n-k+1', concentration)
        self.assertIn(r'\Lambda<r_{\rm fail}', concentration)
        self.assertIn(r'\mu>k-1', concentration)
        self.assertIn(r'\mu-k+1', concentration)
        self.assertNotIn(r'\Lambda<n-k\)', concentration)
        # Boundary case where the old condition was unavailable:
        # n=k=1, one Bernoulli success with probability 1/2.
        failure = 0.5
        variance = 0.25
        gap = 0.5  # mu-k+1 = r_fail-Lambda
        bound = math.exp(-(gap * gap) / (2 * variance + 2 * gap / 3))
        self.assertLessEqual(failure, bound)
        self.assertGreater(0.5, 0)  # mu > k-1
        self.assertFalse(0.5 > 1)   # old mu > k condition did not apply

    def test_closed_simplex_bias_parametrization(self):
        uniform = statement(self.cloud, 'thm:uniform-penalty')
        self.assertIn(r'\varepsilon_i\ge-1', uniform)
        self.assertIn(r'p_i=0', uniform)
        # Exact boundary parametrization eps=(-1,1), checked against the
        # stated Taylor remainder at a fixed alpha.
        alpha = 0.75
        eps = (-1.0, 1.0)
        sigma2 = sum(value * value for value in eps) / 2
        sigma3 = sum(abs(value) ** 3 for value in eps) / 2
        delta = max(abs(value) for value in eps)
        normalized = sum(math.exp(-alpha * value) for value in eps) / 2
        remainder = normalized - 1 - alpha * alpha * sigma2 / 2
        remainder_bound = alpha ** 3 * math.exp(alpha * delta) * sigma3 / 6
        self.assertLessEqual(abs(remainder), remainder_bound + 1e-15)

'''
test_path.write_text(test_text.replace(anchor, methods + anchor))

replace(
    "docs/DEEP_AUDIT_CLARIFICATIONS.md",
    """The optional strengthenings identified by the audit--allowing a boundary
value in one perturbative parametrization and sharpening integer
concentration offsets--are not included, in order to avoid unreviewed scope
changes.""",
    """The two optional Paper II strengthenings identified by the audit were
not included in that clarity-only patch.  They were subsequently reviewed
and adopted in a separate focused change: the concentration theorem now uses
the exact first failing lattice thresholds, and the perturbative bias
parametrization covers the closed simplex.  See
[PAPER_II_TOOLKIT_STRENGTHENINGS.md](PAPER_II_TOOLKIT_STRENGTHENINGS.md).""",
)

append(
    "THEOREM_STATUS.md",
    """## Focused Paper II toolkit strengthenings

The concentration theorem `thm:terminal-cloud` now uses the exact integer
failure gaps `n-k+1-Lambda` and `mu-k+1`, including the additional regime in
which the mean lies between the old real-valued threshold and the first
failing lattice point.  The one-read perturbative theorem
`thm:uniform-penalty` now permits `epsilon_i = -1`, so its expansion applies
on the closed simplex, including zero sampling coordinates.  No optimizer,
staircase, or fixed-read classification changes.  See
[docs/PAPER_II_TOOLKIT_STRENGTHENINGS.md](docs/PAPER_II_TOOLKIT_STRENGTHENINGS.md).""",
)

append(
    "FORMALIZATION_STATUS.md",
    """## Paper II lattice and boundary endpoints

The formalization target should encode failure as the integer event
`U >= n-k+1` (equivalently recovered count `S <= k-1`) before invoking a
real-valued concentration inequality.  The perturbative one-read
parametrization now includes `epsilon_i = -1`, corresponding to a zero
sampling coordinate; no interior-simplex hypothesis is available or needed
for its Taylor remainder bound.""",
)

append(
    "docs/INTEGRATION_AUDIT.md",
    """## Focused Paper II toolkit strengthening

A later focused change adopts the two optional strengthenings identified by
the Paper II deep audit.  The Bernstein bounds use the exact first failing
integer thresholds, and the one-read perturbative expansion permits boundary
sampling laws.  The simple sufficient Bernstein margin is retained; the
exact quadratic inversion is deliberately not added.  No Paper I source or
principal Paper II optimizer/staircase result is changed.""",
)

(ROOT / "docs/PAPER_II_TOOLKIT_STRENGTHENINGS.md").write_text(r"""# Paper II toolkit strengthenings

Date: October 11, 2026. Baseline commit:
`244c1fab380f6db03dd5f82d1d03d9a7bd35f16f`.

This focused revision adopts the two optional strengthenings identified by
the deep audit of Paper II.  It does not alter the active-uniform optimizer,
the terminal-cloud staircase, their equality cases, or any Paper I result.

## Exact integer concentration thresholds

For the defect count `U`, failure is the lattice event
`U >= n-k+1`, not merely a real-valued deviation past `n-k`.  Accordingly,
the Bernstein displacement is

`n-k+1-Lambda`.

For the recovered count `S`, failure is `S <= k-1`, so the lower-tail
displacement is

`mu-k+1`.

In the hard-threshold model these gaps coincide because `mu=n-Lambda` and
`v=V`.  The strengthened statement applies in the additional regime where
the mean lies between the old threshold and the first failing lattice point.
The manuscript retains the simple sufficient margin
`sqrt(2 v L) + 2 L / 3`; it does not add the slightly sharper exact quadratic
solution.

## Closed-simplex perturbative parametrization

The representation

`p_i=(1+epsilon_i)/n`

now assumes `epsilon_i >= -1`, exactly matching `p_i >= 0`.  Taylor's
formula and its cubic remainder remain valid at `epsilon_i=-1`, so the
one-read bias expansion now includes boundary laws with zero sampling
coordinates.  Its strict Jensen equality classification for positive budget
is unchanged.

## Statement impact

Only the Paper II formal statement environments `thm:terminal-cloud` and
`thm:uniform-penalty` change.  Their scopes are strengthened as described;
no principal optimizer or staircase statement changes.  Registry context and
whole-source hashes are regenerated with the source diff.

## Verification

Targeted regressions cover a one-Bernoulli lattice case in which the old
concentration condition was unavailable and the new bound applies, and the
boundary perturbation `epsilon=(-1,1)`.  The standard `make test`, `make pdf`,
and `make check` targets, matching PDF manifests, and affected-page visual
inspection are required before merge.  The regression calculations are
supplementary checks, not proofs of the general inequalities.
""")

validation = {
    "date": "2026-10-11",
    "base_commit": "244c1fab380f6db03dd5f82d1d03d9a7bd35f16f",
    "scope": "Focused Paper II toolkit strengthening: exact integer concentration thresholds and closed-simplex perturbative parametrization.",
    "changed_formal_statements": ["thm:terminal-cloud", "thm:uniform-penalty"],
    "principal_optimizer_or_staircase_statements_changed": False,
    "paper_i_source_changed": False,
    "exact_quadratic_bernstein_inversion_added": False,
    "commands_required": ["make test", "make pdf", "make check"],
    "status": "generated before validation; workflow must replace this status after all checks pass",
}
(ROOT / "docs/paper_ii_toolkit_validation.json").write_text(json.dumps(validation, indent=2) + "\n")

print("Applied the two focused Paper II toolkit strengthenings.")
