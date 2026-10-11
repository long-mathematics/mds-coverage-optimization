#!/usr/bin/env python3
"""Apply the localized clarity revisions from the deep audits.

This is a one-use branch preparation script. It does not strengthen the
principal theorems or alter their equality classifications.
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


expected = {
    "gamma_mds_active_uniform.tex": "314d3959557803756ae58f4fb59939257b96fffcc72137572fd96df4ceb0d21b",
    "terminal_cloud_staircase.tex": "24790dfd913e430ee44d8b24bc96cacccb6555f5a7e5b765c56a75ae49b34214",
}
for name, digest in expected.items():
    actual = hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
    if actual != digest:
        raise ValueError(f"Input snapshot mismatch for {name}: {actual}")

# ---------------------------------------------------------------------------
# Paper I-A: explicit parameters, asymptotics, Newton inequality, boundaries.
# ---------------------------------------------------------------------------
replace(
    "gamma_mds_active_uniform.tex",
    r"""\begin{lemma}[Mixed Gamma tail-ratio bound]
\label{lem:gamma-tail-ratio-bound}
For every real \(m>0\) and \(z>0\),
\[
  \frac{3m}{5}<\eta(z)\zeta(z)<m.
\]
\end{lemma}""",
    r"""\begin{lemma}[Mixed Gamma tail-ratio bound]
\label{lem:gamma-tail-ratio-bound}
Let \(\tau>1\), put \(m=\tau-1\), and let \(\eta,\zeta\) be the
corresponding Gamma tail-ratio elasticities defined above. Then, for
every \(z>0\),
\[
  \frac{3m}{5}<\eta(z)\zeta(z)<m.
\]
\end{lemma}""",
)

replace(
    "gamma_mds_active_uniform.tex",
    r"""For example, at zero one has
\(P(z)\sim\Gamma(m+1)z^{-m}\) and \(Q(z)\sim z/(m+1)\); at infinity, \eqref{eq:mds-gamma-P-integral} gives \(P(z)=1+m/z+O(z^{-2})\).  Thus \(W(z)\to m\) at both ends.""",
    r"""For example, at zero one has
\(P(z)\sim\Gamma(m+1)z^{-m}\) and \(Q(z)\sim z/(m+1)\).
At infinity, Taylor expansion under the exponentially weighted integral
in~\eqref{eq:mds-gamma-P-integral} gives
\[
 P(z)=\int_0^\infty e^{-u}\left(1+\frac uz\right)^m\,du
     =1+\frac mz+O(z^{-2}).
\]
Consequently \(\eta=-zP'/P=m/z+O(z^{-2})\).  Also the identity
\(zQ'=(z-m)Q+z\) gives
\[
 \zeta=z-m+\frac z{Q(z)}=z-m+o(1),
\]
since \(Q(z)\to\infty\).  Thus \(W(z)\to m\) at both ends.""",
)

replace(
    "gamma_mds_active_uniform.tex",
    r"""At the zero of \(N_\alpha\),
\[
  \partial_\alpha N_\alpha=g-uF=\frac gD>0.
\]""",
    r"""At the zero of \(N_\alpha\), the critical relation
\(uD+\alpha g=0\) gives
\[
  \partial_\alpha N_\alpha=g-uF=\frac gD>0.
\]""",
)

replace(
    "gamma_mds_active_uniform.tex",
    r"""The last inequality is log-concavity of the Poisson-binomial mass sequence.  Its probability generating polynomial is a product of linear factors with nonpositive real zeros, so Newton's inequalities give the required coefficient inequality; see also \cite{Liggett1997}.""",
    r"""The last inequality is log-concavity of the Poisson-binomial mass
sequence.  If \(W\) is a sum of \(d\) Bernoulli variables, its
probability generating polynomial is a product of linear factors with
nonpositive real zeros.  For an interior index \(j\), Newton's
inequalities give the normalized form
\[
 \left(\frac{p_j}{\binom dj}\right)^2
 \ge
 \frac{p_{j-1}}{\binom d{j-1}}
 \frac{p_{j+1}}{\binom d{j+1}}.
\]
Since \(\binom dj^2>\binom d{j-1}\binom d{j+1}\), this implies
\(p_j^2\ge p_{j-1}p_{j+1}\).  Taking \(j=k-2\) proves the displayed
inequality; boundary indices follow from the zero extension.  See also
\cite{Liggett1997}.""",
)

replace(
    "gamma_mds_active_uniform.tex",
    r"""No boundary allocation can maximize in this range of shapes.  Indeed, a boundary allocation with positive success has a positive support of size \(q\ge k\).  Activate a zero coordinate with mass \(\varepsilon\) and subtract this mass from one positive coordinate.  Its new recovery probability is
\[
  F_\tau(\varepsilon)
  =\frac{\varepsilon^\tau}{\Gamma(\tau+1)}(1+O(\varepsilon)).
\]
The pivotal probability for the new coordinate tends to the strictly positive probability that exactly \(k-1\) of the original active coordinates recover.  The loss caused by the donor perturbation is \(O(\varepsilon)\), since that coordinate remains bounded away from zero.  Hence the gain is a positive multiple of \(\varepsilon^\tau\), up to \(o(\varepsilon^\tau)\), and it dominates the donor loss.  Every maximizer therefore has full support, and the preceding stationary-point argument proves that full uniformity is the unique maximizer.""",
    r"""No boundary allocation can maximize in this range of shapes.  Indeed, a boundary allocation with positive success has a positive support of size \(q\ge k\).  Activate a zero coordinate with mass \(\varepsilon\) and subtract this mass from one positive coordinate.  Its new recovery probability is
\[
  F_\tau(\varepsilon)
  =\frac{\varepsilon^\tau}{\Gamma(\tau+1)}(1+O(\varepsilon)).
\]
Let
\[
 R_{\rm new}=\Pbb\left(\text{exactly \(k-1\) of the original active
 coordinates recover}\right)>0.
\]
Multi-affinity of the Bernoulli tail in its success probabilities, and
differentiability of the donor response at its positive intensity, give
\[
 \mathcal S(\lambda(\varepsilon))-\mathcal S(\lambda(0))
 =\frac{R_{\rm new}}{\Gamma(\tau+1)}\varepsilon^\tau+O(\varepsilon).
\]
Because \(0<\tau<1\), one has \(O(\varepsilon)=o(\varepsilon^\tau)\),
so the displayed difference is positive for all sufficiently small
\(\varepsilon>0\).  Every maximizer therefore has full support, and the
preceding stationary-point argument proves that full uniformity is the
unique maximizer.""",
)

replace(
    "gamma_mds_active_uniform.tex",
    r"""Their ratio is
\[
  \frac{\binom q{k-1}}{\binom{q-1}{k-1}}
  =\frac q{q-k+1}>1.
\]
The perturbation strictly improves the objective.  Thus a maximizer has full support and is uniquely uniform.""",
    r"""Their ratio is
\[
  \frac{\binom q{k-1}}{\binom{q-1}{k-1}}
  =\frac q{q-k+1}>1.
\]
Thus the first directional derivative along the activation path is the
positive donor derivative multiplied by
\(q/(q-k+1)-1\), and is strictly positive.  The perturbation strictly
improves the objective.  Hence a maximizer has full support and is
uniquely uniform.""",
)

# ---------------------------------------------------------------------------
# Paper I-B: crossing lemma, inverse asymptotics, Prekopa, notation.
# ---------------------------------------------------------------------------
replace(
    "gamma_mds_active_uniform.tex",
    r"""The set \(I=\{x:g(x)>f(x)\}\) is a nonempty interval and cannot
be the entire half-line, since the densities have equal integral.
Strict concavity excludes an interval on which \(g/f=1\).
To the left of \(I\), when nonempty, \(D<0\). To its right,
when nonempty, total mass zero gives
\[
 D(x)=-\int_x^\infty(g(t)-f(t))\,dt>0.
\]
On \(I\), \(D'=g-f>0\). Thus every zero lies in \(I\), is
unique, and has positive derivative. The same argument covers
intervals \(I\) with zero or infinity as an endpoint.""",
    r"""The set \(I=\{x:g(x)>f(x)\}=\{x:\log(g/f)>0\}\) is an interval,
because a superlevel set of a concave function is convex.  It is
nonempty: otherwise \(g\le f\) everywhere, and equality of the two
total integrals together with continuity would force \(g=f\),
contradicting strict concavity of \(\log(g/f)\).  The set cannot be the
entire half-line, again because the densities have equal integral.
Strict concavity also excludes an interval on which \(g/f=1\).
Consequently, on every nonempty region to the left of \(I\), the
integrand \(g-f\) is nonpositive and strictly negative on a set of
positive measure, so \(D<0\).  To the right of \(I\), total mass zero
gives
\[
 D(x)=-\int_x^\infty(g(t)-f(t))\,dt>0.
\]
On \(I\), \(D'=g-f>0\). Thus every zero lies in \(I\), is unique,
and has positive derivative. The same argument covers intervals
\(I\) with zero or infinity as an endpoint.""",
)

replace(
    "gamma_mds_active_uniform.tex",
    r"""For a fixed pair \(q,r\), apply the endpoint estimates with a finite
support cap at least \(r\).
Proposition~\ref{prop:mds-small-depth} gives
\(V_q(M)\sim c(q)M^{\tau k}/\Gamma(\tau+1)^k\) at zero, so""",
    r"""For a fixed pair \(q,r\), apply the endpoint estimates with a finite
support cap at least \(r\).  We use the elementary monotone-inversion
rules
\[
 H(x)\sim ax^p\ (x\downarrow0)
 \ \Longrightarrow\ 
 H^{-1}(u)\sim (u/a)^{1/p}\ (u\downarrow0),
\]
and
\[
 -\log(1-H(x))=ax+o(x)\ (x\to\infty)
 \ \Longrightarrow\ 
 H^{-1}(u)\sim a^{-1}\log\frac1{1-u}\ (u\uparrow1).
\]
Both follow by sandwiching the monotone function between the
corresponding comparison functions with factors \(1\pm\varepsilon\).
Proposition~\ref{prop:mds-small-depth} gives
\(V_q(M)\sim c(q)M^{\tau k}/\Gamma(\tau+1)^k\) at zero, so""",
)

replace(
    "gamma_mds_active_uniform.tex",
    r"""Then \(\widetilde V(e^s,M)=\mu(K_s)\), where \(\mu\) has density
\(\rho\) and \(K_s=\{u:L(u,s)\le b_M(s)\}\).
The function \(L\) is jointly convex: log-sum-exp is convex and
increasing in each argument, and""",
    r"""Then \(\widetilde V(e^s,M)=\mu(K_s)\), where \(\mu\) has density
\(\rho\) and \(K_s=\{u:L(u,s)\le b_M(s)\}\).
The function \(L\) is jointly convex: log-sum-exp is convex and
increasing in each argument, and""",
)
# Insert the convex/Borel conclusion immediately after the displayed curvature.
replace(
    "gamma_mds_active_uniform.tex",
    r""" \frac{d^2}{ds^2}[-\log(1-je^{-s})]
 =\frac{je^{-s}}{(1-je^{-s})^2}\ge0.
\]
Lemma~\ref{lem:mds-cumulative-hazard-geometry} makes \(b_M\)
strictly concave.""",
    r""" \frac{d^2}{ds^2}[-\log(1-je^{-s})]
 =\frac{je^{-s}}{(1-je^{-s})^2}\ge0.
\]
For each \(s\), the function \(u\mapsto L(u,s)\) is continuous and
convex, so \(K_s\) is a closed convex Borel set.  Lemma
\ref{lem:mds-cumulative-hazard-geometry} makes \(b_M\) strictly
concave.""",
)

replace(
    "gamma_mds_active_uniform.tex",
    r"""The Pr\'ekopa--Leindler inequality for the log-concave measure
\(\mu\) \cite[Theorem 2]{Prekopa1973} yields
\[
 \mu(K_\theta^-)
 \ge\mu(K_{s_0})^{1-\theta}\mu(K_{s_1})^\theta.
\]""",
    r"""The density \(\rho\) is log-concave, so Pr\'ekopa's theorem
\cite[Theorem 2]{Prekopa1973} makes the generated measure \(\mu\)
log-concave.  Applying its defining Minkowski inequality to the closed
convex Borel sets above yields
\[
 \mu(K_\theta^-)
 \ge\mu(K_{s_0})^{1-\theta}\mu(K_{s_1})^\theta.
\]""",
)

replace(
    "gamma_mds_active_uniform.tex",
    r"""\[
 \E e^{-tZ}
 =\prod_{j=0}^{k-1}\frac{q-j}{q-j+t}
 =\frac{\Gamma(q+1)\Gamma(q-k+1+t)}
        {\Gamma(q-k+1)\Gamma(q+1+t)}.
\]
For nonnegative integer \(t\), these are the moments of a
\(\mathrm{Beta}(q-k+1,k)\) variable.""",
    r"""\[
 \E e^{-\sigma Z}
 =\prod_{j=0}^{k-1}\frac{q-j}{q-j+\sigma}
 =\frac{\Gamma(q+1)\Gamma(q-k+1+\sigma)}
        {\Gamma(q-k+1)\Gamma(q+1+\sigma)}.
\]
For nonnegative integer \(\sigma\), these are the moments of a
\(\mathrm{Beta}(q-k+1,k)\) variable.""",
)

# ---------------------------------------------------------------------------
# Paper II: existence, t=1 derivative, localization proof, averaging.
# ---------------------------------------------------------------------------
replace(
    "terminal_cloud_staircase.tex",
    r"""\begin{proof}
Let $\lambda^*$ be a global minimizer.  If two positive coordinates of $\lambda^*$ are unequal,""",
    r"""\begin{proof}
The allocation simplex is compact and the objective is continuous, so
a global minimizer exists.  Let $\lambda^*$ be one.  If two positive
coordinates of $\lambda^*$ are unequal,""",
)

replace(
    "terminal_cloud_staircase.tex",
    r"""For \(t=1\),
\[
  a_1(x)=\frac{1-e^{-x}}{x},
\]
which is strictly decreasing on \((0,\infty)\).  Since \(M/q\) is strictly decreasing as \(q\) increases,""",
    r"""For \(t=1\),
\[
  a_1(x)=\frac{1-e^{-x}}{x},
  \qquad
  a_1'(x)=\frac{(x+1)e^{-x}-1}{x^2}<0,
\]
where the strict inequality is equivalent to \(e^x>1+x\).  Thus
\(a_1\) is strictly decreasing on \((0,\infty)\).  Since \(M/q\) is
strictly decreasing as \(q\) increases,""",
)

replace(
    "terminal_cloud_staircase.tex",
    r"""Thus the exact support search is localized to the nearest integer support sizes around \(M/\rho_t\), with only endpoint clipping by \(1\) and \(n\).
\end{corollary}

\begin{example}[Low read depth and deliberate sacrifice]""",
    r"""Thus the exact support search is localized to the nearest integer support sizes around \(M/\rho_t\), with only endpoint clipping by \(1\) and \(n\).
\end{corollary}
\begin{proof}
If \(q\) is optimal, Theorem~\ref{thm:terminal-cloud-staircase} gives
\(\beta_{q-1}\le M\le\beta_q\).  For \(1<q<n\), the strict bounds
on the phase boundaries imply
\[
 (q-1)\rho_t<\beta_{q-1}\le M\le\beta_q<(q+1)\rho_t.
\]
Hence \(q-1<M/\rho_t<q+1\), so \(q\) is one of the floor or ceiling
of \(M/\rho_t\).  When \(q=1\) or \(q=n\), the same conclusion follows
after applying the clipping map to the one available finite boundary.
\end{proof}

\begin{example}[Low read depth and deliberate sacrifice]""",
)

replace(
    "terminal_cloud_staircase.tex",
    r"""is increasing. The preceding prefix argument applies with the same
\(U_i\) at every prefix and the same Poisson-tail error bounds.
\end{proof}""",
    r"""is increasing. For each fixed \(u\), the preceding prefix argument
therefore gives the two sandwich inequalities for the corresponding
deterministic count event, with error terms independent of \(u\).
Averaging those inequalities over the auxiliary uniforms \(U_i\)
gives the stated unconditional randomized-recovery bounds.
\end{proof}""",
)

# ---------------------------------------------------------------------------
# Repository documentation and source-regression tests.
# ---------------------------------------------------------------------------
replace(
    "README.md",
    "[first-audit corrections](docs/FIRST_AUDIT_CORRECTIONS.md), and [formalization roadmap](FORMALIZATION_STATUS.md).",
    "[first-audit corrections](docs/FIRST_AUDIT_CORRECTIONS.md), [deep-audit clarifications](docs/DEEP_AUDIT_CLARIFICATIONS.md), and [formalization roadmap](FORMALIZATION_STATUS.md).",
)

append(
    "THEOREM_STATUS.md",
    """## Deep-audit clarification baseline

The independent deep audits of Paper I-A, Paper I-B, and Paper II found no
principal theorem, scope, or equality case requiring weakening.  The
subsequent clarity patch makes the mixed Gamma parameters explicit,
expands endpoint inversion and Newton normalization, writes the two
boundary derivatives literally, records the convex/Borel hypotheses in
the Pr\'ekopa step, and supplies four omitted proof details in Paper II.
Only `lem:gamma-tail-ratio-bound` changes inside a formal statement
environment, solely to state its existing relation `m = tau - 1`
explicitly.  See [docs/DEEP_AUDIT_CLARIFICATIONS.md](docs/DEEP_AUDIT_CLARIFICATIONS.md).""",
)

append(
    "FORMALIZATION_STATUS.md",
    """## Deep-audit proof-explication baseline

The formalization baseline now states explicitly the parameter relation in
the mixed Gamma bound, the normalized Newton inequality, the boundary
activation expansions, both monotone inverse-asymptotic rules, the closed
convex Borel nature of the Pr\'ekopa sets, compactness in the abstract
collapse theorem, the threshold-one derivative, support localization, and
averaging over auxiliary reconstruction uniforms.  These additions reduce
implicit paper reasoning but do not constitute Lean coverage or alter the
principal theorem scopes.""",
)

append(
    "FORMALIZATION_AUDIT.md",
    """For the deep-audit baseline, treat the monotone inversion statements,
normalized Newton inequality, multi-affine boundary expansion, and
Pr\'ekopa set measurability/convexity as explicit lemmas rather than
informal simplification steps.  In Paper II, formalize existence on the
compact simplex before selecting a minimizer, prove the threshold-one
derivative sign, and derive the localization corollary from the phase
bounds including clipped endpoints.""",
)

append(
    "docs/PROOF_DEPENDENCIES.md",
    """## Deep-audit explication notes

The allocation proof now records the normalized Newton inequality before
ordinary Poisson-binomial log-concavity, and writes the shape-below-one and
shape-one boundary directions explicitly.  The global support proof states
the two inverse-asymptotic rules used at the quantile endpoints and records
that the Pr\'ekopa sets are closed convex Borel sets.  Paper II now states
compactness/existence in the abstract collapse proof, proves the threshold-one
efficiency derivative, proves the localization corollary, and explicitly
averages the fixed-uniform transfer inequalities.  These are proof
explications, not new dependency arrows or theorem strengthenings.""",
)

append(
    "docs/INTEGRATION_AUDIT.md",
    """## Deep audits and clarity-only integration

Separate deep audits reconstructed Paper I-A (Gamma allocation), Paper I-B
(global support phases), and Paper II.  They found no fatal gap, no principal
statement requiring weakening, and no missing equality case.  The resulting
patch adds only the explicit intermediate steps listed in
[DEEP_AUDIT_CLARIFICATIONS.md](DEEP_AUDIT_CLARIFICATIONS.md).  Optional
strengthenings of the Paper II concentration and perturbation statements
were deliberately not introduced.  The frozen v30 source remains unchanged.""",
)

(ROOT / "docs/DEEP_AUDIT_CLARIFICATIONS.md").write_text(r"""# Deep-audit clarifications

Date: October 11, 2026. Baseline commit:
`471e88fbf383095f79b5884717b20c676a3fd18b`.

The deep audits of Paper I-A, Paper I-B, and Paper II found no fatal gap,
no principal theorem requiring weakening, and no incorrect equality case.
This revision applies the recommended proof-explication changes only.
It is not an external referee report and adds no proof-assistant coverage.

## Paper I-A

- State the relation `m = tau - 1` and the corresponding Gamma elasticities
  inside the mixed tail-ratio lemma.
- Expand the large-argument derivation of `P`, `eta`, and `zeta`.
- State the normalized Newton inequality before ordinary coefficient
  log-concavity.
- Make the shape-below-one multi-affine boundary gain and the shape-one
  directional derivative explicit.
- Record the critical relation used in the marginal-peak derivative.

## Paper I-B

- Explain nonemptiness and strict signs in the density-ratio crossing lemma.
- State the elementary inverse-asymptotic rules used at zero and one.
- Record that the Prékopa sets are closed convex Borel sets and describe the
  cited theorem as generation of a log-concave measure by a log-concave
  density.
- Rename the beta-form Laplace parameter to avoid collision with the Poisson
  threshold notation.

## Paper II

- State compactness and existence before choosing a global minimizer.
- Give the derivative proving the threshold-one efficiency is decreasing.
- Add the proof of the support-localization corollary, including clipped
  endpoints.
- Explicitly average the fixed-uniform de-Poissonization inequalities over
  the auxiliary reconstruction uniforms.

The optional strengthenings identified by the audit--allowing a boundary
value in one perturbative parametrization and sharpening integer
concentration offsets--are not included, in order to avoid unreviewed scope
changes.

## Statement impact

All principal theorem statements and equality classifications are unchanged.
Only the statement environment of `lem:gamma-tail-ratio-bound` changes, and
only to make its already-used relation `m = tau - 1` explicit.  The
context-sensitive registry and whole-source hashes are regenerated and must
be reviewed with the source diff.

## Validation

The standard `make test`, `make pdf`, and `make check` targets must pass.
Source-regression tests verify the presence of each clarification.  Matching
sources, PDFs, manifests, and the affected-page visual review are required
before merge.  Numerical diagnostics remain supplementary evidence rather
than proofs.
""")

# Extend the existing source-regression suite without turning it into a
# semantic or mathematical checker.
test_path = ROOT / "scripts/test_audit_regressions.py"
test_text = test_path.read_text()
anchor = "    def test_ambient_change_invalidates_context_not_statement_hash(self):\n"
if test_text.count(anchor) != 1:
    raise ValueError("Could not locate audit regression insertion point")
methods = r'''    def test_deep_audit_gamma_explications(self):
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
        self.assertIn('It is nonempty', self.gamma[self.gamma.index(density):])

    def test_deep_audit_cloud_explications(self):
        self.assertIn('allocation simplex is compact', self.cloud)
        self.assertIn(r'a_1\'(x)=\frac{(x+1)e^{-x}-1}{x^2}<0', self.cloud)
        self.assertIn(r'\begin{proof}\nIf \(q\) is optimal', self.cloud)
        self.assertIn('Averaging those inequalities over the auxiliary uniforms', self.cloud)

'''
test_path.write_text(test_text.replace(anchor, methods + anchor))

# Record the base and expected scope of the generated validation record.
validation = {
    "date": "2026-10-11",
    "base_commit": "471e88fbf383095f79b5884717b20c676a3fd18b",
    "scope": "Clarity-only integration following the deep audits of Paper I-A, Paper I-B, and Paper II; no theorem strengthening or proof-assistant certification.",
    "principal_theorem_statements_changed": False,
    "formal_statement_clarifications": ["lem:gamma-tail-ratio-bound"],
    "optional_strengthenings_applied": False,
    "commands_required": ["make test", "make pdf", "make check"],
    "status": "generated before validation; workflow must replace this status after all checks pass",
}
(ROOT / "docs/deep_audit_validation.json").write_text(json.dumps(validation, indent=2) + "\n")

print("Applied deep-audit clarity revisions to both manuscripts and repository documentation.")
