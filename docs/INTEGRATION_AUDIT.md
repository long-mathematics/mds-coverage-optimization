# Initial split: integration audit

Date: October 11, 2026. This records the current extraction/integration review. It does not describe a new independent referee review, and it is not proof-assistant certification.

## Mathematical review

- Checked that the Gamma optimizer statement includes all positive shapes, every-maximizer classification, one-point k = 1 optimum for shape > 1, full-recovery uniqueness, and the shape = 1 / k = 1 constant-objective exception.
- Reviewed the Riccati minimum argument, marginal-ratio cancellation, shadow ordering, two structured perturbations, and boundary-activation arguments while integrating the source. No theorem-strengthening claim was added in the split.
- Preserved the exact small-depth support example, finite-gap limitations, large-depth k >= 2 restriction, and the unclassified degenerate Hessian threshold.
- Shortened the common-response proof only where it duplicates response-independent algebra already proved in the same paper. The proof now names those dependencies and still supplies the general-response derivative signs, peak argument, and final secant inequalities. The dependency direction is acyclic.
- Corrected a normalization slip in the v30 two-point cloud proof: g(x) must equal exp(-x) x^(t-1)/(t-1)! for the displayed derivative h'_S(a) = -g(a)+g(S-a) to be literal. The omitted factor was positive, so the sign and logarithmic-ratio arguments are unchanged. The normalization is now included, and a symbolic regression test checks it.
- Condensed standard coverage calculations without transferring optimizer conclusions to fixed-read, heterogeneous, random-environment, or arbitrary recovery-family settings. Full-count conditional independence and calibration feasibility are explicit.

## Reproducible checks

`make test` runs two exact rational example certificates, exact symbolic identities, and deterministic finite Gamma/allocation/staircase diagnostics. The script outputs state their scope. These computations do not verify all real parameters or certify a global optimum.

`make pdf` and `make check` require standalone compilation, resolved references and citations, no duplicated labels, no uncited bibliography items, matching source/PDF hashes, warning-free TeX logs, and rebuild text agreement. Stable labeled statements are recorded in `docs/statement_registry.json`.

The exact archive hash is checked separately. Visual review of the generated pages is recorded in `docs/VISUAL_REVIEW.md`. CI verifies text/layout warnings but does not replace visual or mathematical review.

## Still required for stronger certification

An independent mathematical audit can now be performed paper by paper using the dependency ledger. No Lean theorem is yet formalized. Future formalization must include boundary cases, hypotheses and equality-case correspondence, and transitive-axiom checks rather than merely a successful build.
