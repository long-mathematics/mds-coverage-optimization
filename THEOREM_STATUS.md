# Theorem status

Status after integration of the global Gamma/MDS support results, October 11, 2026. Paper I is now titled **Optimal Allocations for Gamma Completion and MDS Recovery**; its stable source and PDF basenames are unchanged.

| Claim | Location / stable label | Status |
|---|---|---|
| All positive common Gamma shapes; complete equality classification | I, `thm:gamma-active-uniform` | Analytic proof supplied; no Lean certification |
| Integer-shape Poissonized MDS specialization | I, `thm:full-mds-active-uniform` | Corollary of the Gamma theorem, presented with its own statement |
| Mixed Gamma tail-ratio bound | I, `lem:gamma-tail-ratio-bound` | Analytic Riccati proof; finite symbolic identities checked |
| Common-response sufficient criterion | I, `prop:common-recovery-active-uniform` | Analytic proof supplied with all additional slope hypotheses retained |
| Small-budget support and tie-breaking | I, `prop:mds-small-depth` | Proved for fixed finite n, k, and shape greater than one |
| Eventual full support | I, `prop:mds-large-depth` | Proved for k >= 2; not asserted for k = 1 |
| Active-barycenter stability | I, `prop:mds-barycenter-stability` | Facewise result; degenerate threshold left unclassified |
| Gamma cumulative-hazard geometry | I, `lem:mds-cumulative-hazard-geometry` | Strict geometric concavity for every real shape > 1; inverse elasticity is positive and strictly increasing |
| Scaled Gamma quantile-ratio order | I, `prop:mds-gamma-quantile-order` | Strict increase for each pair k <= q < r, k >= 2, shape > 1; analytic transfer from exponential order statistics |
| Global MDS pairwise crossings | I, `thm:mds-pairwise-crossing` | Complete dominance-or-unique-crossing classification, including leading-coefficient equality and strict transversality |
| Strict concavity in logarithmic support | I, `thm:mds-log-support-concavity` | Positive real-support interpolation; strictness proved by a positive-measure shell in the Prékopa–Leindler argument |
| Global Gamma/MDS support staircase | I, `thm:mds-global-support-staircase` | Proved for shape > 1 and 2 <= k <= n; consecutive supports q0 through n; no re-entry or skipped transitions after q0; exactly two adjacent supports at each boundary |
| Nonadjacent crossing location | I, `cor:mds-nonadjacent-crossing-location` | Crossing lies strictly between the outer adjacent transition budgets and below the optimum |
| Expected-cloud active-uniform minimizers | II, `thm:active-uniform-terminal-cloud` | Analytic proof supplied for integer t >= 2; t = 1 separately by strict convexity |
| Expected-cloud adjacent-support staircase | II, `thm:terminal-cloud-staircase` | Full analytic phase classification supplied |
| Zero-budget coverage and arbitrary-curve continuity | II, `thm:poissonized-identity`, `thm:dp` | Toolkit includes M = 0; continuity holds for all bounded count recovery curves; monotonicity has its own hypothesis |
| Fixed-read sandwich | II, `thm:depoissonization` | Includes zero reads as a separate case; probability transfer for a fixed law, not optimizer transfer |
| Calibration/environment guarantees | II, `thm:plugin`, `thm:random-environment` | Explicit 0 < delta, eta < 1; measurable finite calibration depth, feasibility, and a conditional fixed-law sequencing model with fresh randomness |
| Annealed one-read bias penalty | II, `thm:annealed-jensen` | Random-probability-vector and positive-budget assumptions stated locally, preserving strict equality classification |
| Exact higher-threshold fixed-read optimizer | Neither paper | Open here; no claim inherited from Poissonization |

Here q0 is the largest maximizer of the small-budget coefficient over the available supports. It may exceed k; supports below it are permanently dominated. If q0 = n, there are no transition budgets and full support is optimal for every positive budget. The shape <= 1 and k = 1 classifications are unchanged. The general-response support remark concerns active-uniform candidates; it does not establish an optimizer classification for arbitrary response curves.

All current formal statements are inventoried in [docs/statement_registry.json](docs/statement_registry.json). Schema 2 supplements individual statement hashes with complete source-prefix and whole-source hashes. These conservative fingerprints also detect edits to ambient hypotheses, definitions, and proofs, but are not semantic dependency analysis or mathematical verification. Proof dependencies and suggested audit order are in [docs/PROOF_DEPENDENCIES.md](docs/PROOF_DEPENDENCIES.md).

Prior v30 audit claims are historical context. The integration audit records proof review of the new arguments and localized extraction corrections; it does not claim an external referee report or proof-assistant certification. Finite exact certificates concern only the specified examples and algebraic identities. The new support diagnostics reproduce transition values and selected strict inequalities; numerical diagnostics cannot establish theorem validity for all parameters.

The [localized first-audit repairs](docs/FIRST_AUDIT_CORRECTIONS.md) are retained in full. Relative to that corrected version, the global-support integration preserves every existing formal statement in both papers and adds ten in Paper I.

## Deep-audit clarification baseline

The independent deep audits of Paper I-A, Paper I-B, and Paper II found no
principal theorem, scope, or equality case requiring weakening.  The
subsequent clarity patch makes the mixed Gamma parameters explicit,
expands endpoint inversion and Newton normalization, writes the two
boundary derivatives literally, records the convex/Borel hypotheses in
the Pr'ekopa step, and supplies four omitted proof details in Paper II.
Only `lem:gamma-tail-ratio-bound` changes inside a formal statement
environment, solely to state its existing relation `m = tau - 1`
explicitly.  See [docs/DEEP_AUDIT_CLARIFICATIONS.md](docs/DEEP_AUDIT_CLARIFICATIONS.md).

## Focused Paper II toolkit strengthenings

The concentration theorem `thm:terminal-cloud` now uses the exact integer
failure gaps `n-k+1-Lambda` and `mu-k+1`, including the additional regime in
which the mean lies between the old real-valued threshold and the first
failing lattice point.  The one-read perturbative theorem
`thm:uniform-penalty` now permits `epsilon_i = -1`, so its expansion applies
on the closed simplex, including zero sampling coordinates.  No optimizer,
staircase, or fixed-read classification changes.  See
[docs/PAPER_II_TOOLKIT_STRENGTHENINGS.md](docs/PAPER_II_TOOLKIT_STRENGTHENINGS.md).
