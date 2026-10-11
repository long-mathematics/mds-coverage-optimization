# Integration audit

Date: October 11, 2026. This records extraction and integration reviews. It does not describe an external referee review, and it is not proof-assistant certification.

## Initial two-paper split

- Checked that the Gamma optimizer statement includes all positive shapes, every-maximizer classification, one-point k = 1 optimum for shape > 1, full-recovery uniqueness, and the shape = 1 / k = 1 constant-objective exception.
- Reviewed the Riccati minimum argument, marginal-ratio cancellation, shadow ordering, two structured perturbations, and boundary-activation arguments while integrating the source. No theorem-strengthening claim was added in the split.
- Preserved the exact small-depth support example, finite-gap limitations, large-depth k >= 2 restriction, and the unclassified degenerate Hessian threshold.
- Shortened the common-response proof only where it duplicates response-independent algebra already proved in the same paper. The proof now names those dependencies and still supplies the general-response derivative signs, peak argument, and final secant inequalities. The dependency direction is acyclic.
- Corrected a normalization slip in the v30 two-point cloud proof: g(x) must equal exp(-x) x^(t-1)/(t-1)! for the displayed derivative h'_S(a) = -g(a)+g(S-a) to be literal. The omitted factor was positive, so the sign and logarithmic-ratio arguments are unchanged. The normalization is now included, and a symbolic regression test checks it.
- Condensed standard coverage calculations without transferring optimizer conclusions to fixed-read, heterogeneous, random-environment, or arbitrary recovery-family settings. Full-count conditional independence and calibration feasibility are explicit.

## Global Gamma/MDS support integration

Paper I is retitled **Optimal Allocations for Gamma Completion and MDS Recovery**. Its source and PDF basenames are unchanged. The new results complete its finite support comparison and belong with its active-uniform theorem; Paper II retains its separate expected-defect objective and independent staircase proof. There are still two active manuscripts. The frozen v30 source is unchanged.

The mathematical additions are:

- Geometric concavity of the Gamma cumulative hazard, derived from the decreasing hazard elasticity already proved in Paper I. The inverse has positive increasing logarithmic elasticity.
- A density-ratio crossing lemma and an explicit exponential-order-statistic comparison, followed by transfer through the inverse cumulative hazard. This proves strict increase of scaled Gamma quantile ratios.
- A complete pairwise support classification from that strict ratio order and the existing fixed-parameter endpoint asymptotics. Leading-coefficient equality yields strict dominance by the larger support for every positive budget; other pairs cross exactly once, transversely, toward the larger support.
- A fixed-dimensional exponential-spacing interpolation of the support curves. Joint convexity and the Prékopa–Leindler inequality give logarithmic-support concavity; a nonempty open shell of positive probability establishes strictness directly.
- An adjacent-tie lemma, strict ordering of all transition budgets, and the complete allocation staircase. The theorem includes the largest-leading-maximizer convention, permanent domination below q0, q0 = n, and exactly two adjacent supports at every transition. Nonadjacent crossings lie below the optimal envelope.

These claims replace the former open questions about global MDS crossings, support re-entry, and skipped transitions. Absence of skipped transitions begins at q0, which may exceed k. No direct unimodality claim about the ratio of Gamma support densities is used. The common-response support observation remains a statement about active-uniform candidates; it does not supply a general allocation theorem.

The proof supplement was checked separately before integration. The integration reuses the existing hazard-elasticity identity and asymptotic results rather than duplicating their proofs. The new supporting external input is Prékopa's 1973 theorem on log-concave measures; the strictness step is proved in the manuscript. The original Gamma allocation proof, all shape-boundary equality cases, and the local Hessian criterion are retained.

A separate analytic review of the integrated text checked crossing direction and transversality, strictness of the support interpolation, the empty-list and leading-tie cases, and the final allocation equality classification. It found no remaining substantive proof defect. Its scope clarifications are incorporated: support-curve formulas extend to all integer q >= k for pairwise comparisons, whereas feasible allocations keep q <= n; endpoint asymptotics for a fixed pair use a finite cap containing that pair; Paper II explicitly restricts its summary of the MDS phase result to k >= 2. The registry diff confirms that all 20 original Paper I formal statements are unchanged, with 10 added statements; the four Paper II statement edits are exactly the localized corrections listed below.

## Localized extraction corrections

- Paper I defines the complementary integer-threshold response psi_t = 1 - F_t before using the expected-cloud comparison.
- Paper II's conditional-environment and stochastic calibration guarantees explicitly assume 0 < delta, eta < 1. Their independence and feasibility hypotheses are preserved.
- Paper II states continuity of the Poissonized success probability for arbitrary count recovery curves taking values in [0,1]. Continuity follows from locally uniform convergence; nondecreasing curves are required separately for monotonicity and bisection.
- Paper II's coverage toolkit explicitly allows M = 0 and records the corresponding endpoint identities. Positive-budget hypotheses in all optimizer and strict equality statements are unchanged.

These are local repairs identified by the extraction audit. They do not transfer an optimizer between objectives or from Poissonized to fixed-read sampling.

## Reproducible checks

`make test` runs two exact rational example certificates, exact symbolic identities, and deterministic finite Gamma/allocation/staircase diagnostics. The new `scripts/verify_support_phases.py` independently evaluates the support tails, reproduces the transition illustration, and checks selected density, hazard, dominance, and support-concavity consequences at high precision. The script outputs state their scope and tolerances. These computations do not verify all real parameters or certify a global optimum.

`make pdf` and `make check` require standalone compilation, resolved references and citations, no duplicated labels, no uncited bibliography items, matching source/PDF hashes, warning-free TeX logs, and rebuild text agreement. Stable labeled statements are recorded in `docs/statement_registry.json`. Full manuscript hashes now supplement the statement-body hashes, detecting edits to ambient hypotheses, definitions, notation, and proofs. The validator also checks local links in the audit documentation and all tracked READMEs.

The exact archive hash is checked separately. Visual review of the generated pages is recorded in `docs/VISUAL_REVIEW.md`. CI verifies text/layout warnings but does not replace visual or mathematical review.

The completed local validation is recorded in [global_support_validation.json](global_support_validation.json): all three standard commands passed, both PDFs rebuilt without warnings, all 45 formal statements were inventoried, and fresh outputs matched all four recorded diagnostic files. Paper I has 27 pages and Paper II has 13. The earlier `initial_validation.json` remains the historical record of the initial split.

## Still required for stronger certification

The dependency ledger supports further independent review paper by paper. No Lean theorem is yet formalized. Future formalization must include boundary cases, hypotheses and equality-case correspondence, and transitive-axiom checks rather than merely a successful build.
