# Deep-audit clarifications

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

The two optional Paper II strengthenings identified by the audit were
not included in that clarity-only patch.  They were subsequently reviewed
and adopted in a separate focused change: the concentration theorem now uses
the exact first failing lattice thresholds, and the perturbative bias
parametrization covers the closed simplex.  See
[PAPER_II_TOOLKIT_STRENGTHENINGS.md](PAPER_II_TOOLKIT_STRENGTHENINGS.md).

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
