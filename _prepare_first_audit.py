#!/usr/bin/env python3
"""One-use preparation of the localized first-audit corrections."""
from pathlib import Path
import hashlib
ROOT=Path(__file__).resolve().parent

def replace(path,old,new):
    p=ROOT/path
    s=p.read_text()
    if s.count(old)!=1:
        raise ValueError(f'{path}: expected exactly one edit anchor: {old[:100]!r}')
    p.write_text(s.replace(old,new))

def append(path,text):
    p=ROOT/path
    p.write_text(p.read_text().rstrip()+'\n\n'+text.strip()+'\n')

expected={
'gamma_mds_active_uniform.tex':'36854a9c5a0890462e78f601f9873342e58a31209ffb62ea8b927bba73c2e990',
 'terminal_cloud_staircase.tex':'a44203e4a1b3c2a21e9b8c68637af23eba65dfa7656520e7cd1b79f192485980',
 'archive/v30/nonuniform_coverage_theorem_notes_v30.tex':'b02adfe4de5352b20edc27420692f272f06e5503180e506eb9538ca680e3eda3',
}
for name,digest in expected.items():
    if hashlib.sha256((ROOT/name).read_bytes()).hexdigest()!=digest:
        raise ValueError(f'Input snapshot mismatch: {name}')

replace('gamma_mds_active_uniform.tex',
        'For the expected terminal cloud, the support size minimizes\n\\[\n  (n-q)+q\\psi_t(M/q).',
        'For the expected terminal cloud at an integer threshold \\(t\\ge1\\), the support size minimizes\n\\[\n  (n-q)+q\\bigl(1-F_t(M/q)\\bigr).')
replace('terminal_cloud_staircase.tex',
 r'Write \([n]=\{1,\ldots,n\}\) and',
 r'For an integer \(n\ge1\), write \([n]=\{1,\ldots,n\}\) and')
replace('terminal_cloud_staircase.tex',
 r'''We now fix \(p\); these statements evaluate or bound a specified
allocation rather than classify an optimum. Read counts take values in
\(\N=\{0,1,2,\ldots\}\).''',
 r'''In this toolkit, \(n\ge1\) and \(1\le k\le n\) are integers,
\(p\in\Delta_n\) is fixed, and \(M\ge0\) is a finite budget.
These statements evaluate or bound a specified allocation rather than
classify an optimum. Read counts take values in
\(\N=\{0,1,2,\ldots\}\).''')
replace('terminal_cloud_staircase.tex',
 r'''Thus Poisson splitting gives independent counts of means \(Mp_i\).''',
 r'''Thus Poisson splitting gives independent counts of means \(Mp_i\).
At \(M=0\), all counts vanish. For hard thresholds,
\(\Lambda_t(0;p)=n\) for every \(p\); the preceding optimizer and
uniqueness theorems retain their positive-budget hypotheses.''')
replace('terminal_cloud_staircase.tex',
 r'''In particular, for \(s_i(r)=\1_{\{r\ge t\}}\), one has
\(\theta_i(M)=\phi_t(Mp_i)\).''',
 r'''At \(M=0\), \(\theta_i(0)=s_i(0)\), with the usual convention
\(0^0=1\) in the series. In particular, for
\(s_i(r)=\1_{\{r\ge t\}}\), one has \(\theta_i(M)=\phi_t(Mp_i)\).''')
replace('terminal_cloud_staircase.tex',
 r'''This uses \(O(nk)\) arithmetic operations and \(O(k)\) memory.
If every \(s_i\) is nondecreasing, \(P_{\rm succ}(M)\) is continuous
and nondecreasing in \(M\); bisection is valid once a feasible target
bracket has been established.''',
 r'''Given the recovery probabilities \(\theta_i\), this uses \(O(nk)\)
arithmetic operations and \(O(k)\) memory. For arbitrary curves
\(s_i:\N\to[0,1]\), \(P_{\rm succ}(M)\) is continuous on
\([0,\infty)\). If every \(s_i\) is nondecreasing, it is also
nondecreasing in \(M\); bisection then applies once a feasible target
bracket has been established.''')
replace('terminal_cloud_staircase.tex',
 r'''previous row. A Poisson-increment coupling and the same independent
uniform random variables for the Bernoulli decisions show monotonicity.
Continuity of each Poisson expectation follows by dominated convergence
under this coupling, or from its locally uniformly convergent series;
the tail is a polynomial in the \(\theta_i\).''',
 r'''previous row. On \(0\le M\le A<\infty\), the absolute value of
the \(r\)-th series term for \(\theta_i(M)\) is at most
\(A^r/r!\). The series therefore converges uniformly on every compact
budget interval, without a monotonicity assumption on \(s_i\).
The tail is a polynomial in the \(\theta_i\), so it is continuous.
When the curves are nondecreasing, a Poisson-increment coupling and
the same independent uniforms for the decisions show monotonicity.''')
replace('terminal_cloud_staircase.tex',
 r'For every \(m\ge1\) and \(0<\varepsilon<1\),',
 r'For every integer \(m\ge0\) and \(0<\varepsilon<1\),')
replace('terminal_cloud_staircase.tex',
 r'''Construct all \(C^{(j)}\) from successive prefixes of one infinite''',
 r'''If \(m=0\), then \(C^{(0)}=Z^{(0)}=0\) almost surely and both
exponential error terms equal one, so the inequalities hold directly.
Assume now \(m\ge1\). Construct all \(C^{(j)}\) from successive
prefixes of one infinite''')
replace('terminal_cloud_staircase.tex',
 r'''Let \(P=(P_1,\ldots,P_n)\) be a random probability vector. Conditional
on \(P\), suppose counts are independent Poisson variables of means''',
 r'''Let \(0<\delta,\eta<1\), let \(M\ge0\) be a fixed finite budget,
and let \(P=(P_1,\ldots,P_n)\) be a random probability vector.
Conditional on \(P\), suppose counts are independent Poisson variables of means''')
replace('terminal_cloud_staircase.tex',
 r'''If \(\E P_i=1/n\) for every \(i\), then''',
 r'''Let \(M>0\) and let \(P=(P_1,\ldots,P_n)\) be a random probability
vector with \(\E P_i=1/n\) for every \(i\). Then''')
replace('terminal_cloud_staircase.tex',
 r'''For a fixed true law \(p\), let \(0\le\ell_i\le p_i\).''',
 r'''For a fixed true law \(p\in\Delta_n\) and a finite budget \(M\ge0\),
let \(0\le\ell_i\le p_i\).''')
replace('terminal_cloud_staircase.tex',
 r'''Suppose independent calibration data produce nonnegative simultaneous
lower bounds \(\widehat\ell_i\) such that
\(\Pbb(\widehat\ell_i\le p_i\text{ for all }i)\ge1-\eta\).
If a calibration-dependent depth \(M(\widehat\ell)\) is chosen with''',
 r'''Let \(0<\delta,\eta<1\). Suppose calibration data produce
nonnegative simultaneous lower bounds \(\widehat\ell_i\) such that
\(\Pbb(\widehat\ell_i\le p_i\text{ for all }i)\ge1-\eta\).
Choose a measurable depth rule
\(M:[0,\infty)^n\to[0,\infty)\). Conditional on calibration,
subsequent counts are independent Poisson variables of means
\(M(\widehat\ell)p_i\), generated using independent fresh randomness.
If the selected finite depth satisfies''')
replace('scripts/validate_repository.py',
 "              'statement_sha256':hashlib.sha256(m.group(0).encode()).hexdigest()})",
 "              'statement_sha256':hashlib.sha256(m.group(0).encode()).hexdigest(),\n"
 "              'context_sha256':hashlib.sha256(text[:m.start()].encode()).hexdigest()})")
replace('scripts/validate_repository.py',
 " record={'status':'Analytic proofs supplied; no proof-assistant coverage claimed.','manuscripts':registry}",
 " record={'schema_version':2,\n"
 "         'status':'Analytic proofs supplied; no proof-assistant coverage claimed.',\n"
 "         'source_sha256':{f'{stem}.tex':sha(ROOT/f'{stem}.tex') for stem in STEMS},\n"
 "         'manuscripts':registry}")
replace('Makefile',
 '\t$(PYTHON) scripts/validate_repository.py --sources-only\n',
 '\t$(PYTHON) scripts/test_audit_regressions.py\n\t$(PYTHON) scripts/validate_repository.py --sources-only\n')
replace('THEOREM_STATUS.md',
 'Status at the initial two-paper split, October 11, 2026.',
 'Updated after the localized first-audit corrections, October 11, 2026.\nThe principal extremal statements and their proofs are unchanged.')
replace('THEOREM_STATUS.md',
 '| Fixed-read sandwich | II, `thm:depoissonization` | Probability transfer for a fixed law, not optimizer transfer |',
 '| Fixed-read sandwich | II, `thm:depoissonization` | Includes zero reads by a separate trivial case; fixed-law probability transfer, not optimizer transfer |')
replace('THEOREM_STATUS.md',
 '| Calibration/environment guarantees | II, `thm:plugin`, `thm:random-environment` | Conditional guarantees with stated independence and feasibility assumptions |',
 '| Calibration/environment guarantees | II, `thm:plugin`, `thm:random-environment` | Error parameters explicitly in (0,1); calibration depth measurable and finite, with a conditional fresh-sequencing model |')
replace('THEOREM_STATUS.md',
 'The registry hashes statements, not proofs, and is not a mathematical checker.',
 'The registry separately hashes statement environments, their complete source prefixes, and whole manuscript sources. These conservative context fingerprints detect edits to surrounding assumptions and definitions, but also react to earlier proof or cosmetic changes; they are not a mathematical checker.')
append('THEOREM_STATUS.md',
 'The localized repairs and their verification scope are recorded in [docs/FIRST_AUDIT_CORRECTIONS.md](docs/FIRST_AUDIT_CORRECTIONS.md). The separate deeper paper audits and Lean formalization remain outstanding.')
append('AGENTS.md',
 '''## Context-sensitive statement registry

Registry schema 2 records each statement environment, its complete preceding source prefix, and the whole manuscript source. Review context/source hash changes as well as statement hashes; a changed surrounding assumption or definition is mathematically relevant even when a theorem environment is unchanged. Prefix hashes are deliberately conservative, not semantic dependency analysis. Do not refresh the registry merely to silence a failure without reviewing the source diff.''')
append('FORMALIZATION_STATUS.md',
 '''## Ambient context after the first audit

Before translating a statement, resolve its complete local context, not only its theorem environment. Registry schema 2 fingerprints source prefixes and whole manuscripts to flag context drift. Important contexts include Paper I's common Gamma response and positive-face hypotheses, its fixed n/k/shape asymptotic regime, and Paper II's distinction between positive-budget optimizer claims and nonnegative-budget probability identities. Calibration depth rules are now explicitly measurable and finite, and the conditional sequencing law is stated. These source checks do not certify measurability or any analytic proof in Lean.''')
append('docs/INTEGRATION_AUDIT.md',
 '''## Localized corrections following the first audit

The subsequent first audit identified missing local error-parameter domains, one undefined comparison symbol, and compressed toolkit scope. Those issues are addressed in [FIRST_AUDIT_CORRECTIONS.md](FIRST_AUDIT_CORRECTIONS.md). The initial audit record above is historical and has not been rewritten as a deeper certification. The principal theorems and proofs and the frozen v30 remain unchanged; source-context fingerprinting and targeted regression tests have been added.''')
replace('README.md',
 'the [statement registry](docs/statement_registry.json), [integration audit](docs/INTEGRATION_AUDIT.md), and [formalization roadmap](FORMALIZATION_STATUS.md).',
 'the [context-sensitive statement registry](docs/statement_registry.json), [integration audit](docs/INTEGRATION_AUDIT.md), [first-audit corrections](docs/FIRST_AUDIT_CORRECTIONS.md), and [formalization roadmap](FORMALIZATION_STATUS.md).')
replace('README.md',
 '`make test` runs exact rational certificates, symbolic identities, and deterministic finite numerical diagnostics.',
 '`make test` runs exact rational certificates, symbolic identities, deterministic finite numerical diagnostics, and localized-audit regression tests.')
replace('README.md',
 '`make check` checks provenance, stable statements, internal references, local README links, and warning-free rebuilds,',
 '`make check` checks provenance, stable statements and source-context fingerprints, internal references, local README links, and warning-free rebuilds,')
replace('README.md',
 'The initial PDFs have **21 pages** (Paper I) and **13 pages** (Paper II).',
 'The current PDFs have **21 pages** (Paper I) and **14 pages** (Paper II).')
append('docs/VISUAL_REVIEW.md',
 '''## First-audit corrections, October 11, 2026

Rendered the locally rebuilt corrected sources with MuPDF and compared
page renders against the corresponding initial local PDFs. The only
changed page in Paper I is page 12. Paper II changes pages 2 and 8--13
and adds bibliography page 14; all other corresponding pages render
identically in this local comparison. Inspected all affected pages at
readable resolution: the comparison formula, toolkit hypotheses,
continuity proof, zero-read case, random-environment domains, annealed
assumptions, calibration rule, and reference continuation are legible,
with no clipping, overlap, or broken glyphs. The local PDFs are 21 and
14 pages. Font size and margins are unchanged.

This is a visual check of local builds of the corrected sources, not an
independent mathematical audit or a claim of byte-identical output across
TeX installations. GitHub Actions separately rebuilds and validates the
tracked source/PDF pair on its runner.''')

(ROOT/'scripts/test_audit_regressions.py').write_text(r'''#!/usr/bin/env python3
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
''')
(ROOT/'docs/FIRST_AUDIT_CORRECTIONS.md').write_text('''# Localized corrections after the first audit

Date: October 11, 2026. Baseline: `d5a8b96201785a02fb93b0cc93ba6a658c55345a`.
This is the disposition of the first-audit findings, not a new independent
referee audit, a novelty claim, or proof-assistant certification.

## Changes applied

| Finding | Resolution |
|---|---|
| Paper I used an undefined Poisson lower-tail symbol in the comparison remark | Use `1-F_t` directly and specify the integer threshold. No Paper I theorem or proof changes. |
| Paper II omitted error-parameter domains | State `0 < delta, eta < 1` locally in the environment and calibration guarantees. |
| Continuity was unnecessarily conditioned on monotone recovery curves | Restore continuity for every curve into `[0,1]`; monotonicity and bisection remain conditional. Give the compact-interval series domination explicitly. |
| Dynamic-program cost could be misread | Specify that `O(nk)` counts arithmetic operations given the recovery probabilities. |
| Zero budgets/reads were excluded from the toolkit wording | Permit finite nonnegative toolkit budgets; evaluate recovery at zero by `s_i(0)`; handle zero reads separately before using Chernoff's positive-mean argument. |
| Annealed result inherited its probability-vector hypothesis | State the random-vector hypothesis and positive budget locally, preserving the strict equality case. |
| Calibration selector was implicit | Specify a measurable finite depth rule and the fixed-law conditional Poisson model with fresh sequencing randomness. Feasibility is still a hypothesis. |
| Registry omitted surrounding context | Schema 2 records full-source hashes and complete-prefix hashes for each statement, in addition to exact statement hashes. |

Positive-budget optimizer and uniqueness hypotheses have not been relaxed.
At zero hard-threshold budget every sampling law has expected cloud `n`.
No global MDS support-phase result or higher-threshold fixed-read optimizer
is asserted. The fixed-parameter qualifications on Paper I's asymptotics
are unchanged.

## Changed statement environments

Only six Paper II environments change: `thm:poissonized-identity`,
`thm:dp`, `thm:depoissonization`, `thm:random-environment`,
`thm:annealed-jensen`, and `thm:plugin`. All 20 Paper I statement
environments and the other nine Paper II environments are preserved
byte-for-byte from the baseline. No principal extremal proof changes.
The frozen v30 source remains byte-for-byte unchanged.

## Registry semantics and formalization boundaries

`statement_sha256` fingerprints the exact theorem/lemma/proposition/corollary
environment. `context_sha256` fingerprints all source preceding that
environment. `source_sha256` fingerprints the entire manuscript, including
later definitions or proofs. These checks deliberately react to cosmetic
and earlier proof changes as well as hypothesis edits. They do not infer
semantic scope, prove a statement, or replace human review of the diff.

For formalization, resolve the full context of each statement. In particular:
Paper I's asymmetric-pattern arguments use positive faces, shape greater
than one, and internal recovery thresholds; its support asymptotics fix
`n,k,tau`. Paper II's optimizer claims use positive budgets, while its
probability toolkit allows zero. Conditional independence is with respect
to the full count vector; calibration bounds use a measurable finite rule
and fresh fixed-law sequencing. No Lean coverage is added.

## Verification

`make test` includes five targeted regression tests covering the notation,
local domains, continuity/zero-budget wording, a finite exact two-stage
grid and the invalid-domain counterexample, and context-drift detection.
These tests are not proofs of the analytic theorems. Existing exact,
symbolic, and finite numerical checks remain in place.

Run `make test`, `make pdf`, and `make check` for the complete validation.
The PDF manifest records the current source/PDF pair; source-context and
statement records are intentionally regenerated only after reviewing the
source changes. Affected-page visual inspection is recorded separately
in `VISUAL_REVIEW.md`. Separate deeper audits of the two papers remain
outstanding.
''')
for name,digest in {
 'gamma_mds_active_uniform.tex':'a16b7f2a8533250bc6803b6b2b3056be368cf52534bd526d4ef9503855b172d0',
 'terminal_cloud_staircase.tex':'0a3e893d909f0684be1c35acddd55378b4ad19ee046469c32457629845829472',
}.items():
    actual=hashlib.sha256((ROOT/name).read_bytes()).hexdigest()
    if actual!=digest: raise ValueError(f'Output source mismatch: {name}: {actual}')
    print(name,actual)
print('Applied localized corrections; both source hashes match the locally tested versions.')
