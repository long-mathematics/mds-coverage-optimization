# Formalization status and roadmap

**Current Lean coverage: none.** There is no Lake project, theorem stub, or formalization CI badge. The analytic manuscripts and reproducibility scripts are not Lean proofs.

## First milestones

1. **Paper II, finite optimization reduction.** Formalize the compact simplex, active support, and abstract two-point-collapse theorem. Check that the conclusion classifies every minimizer, not merely the existence of one symmetric minimizer.
2. **Paper II, calculus and phase ordering.** Formalize the Poisson-tail formulas, the two-point sign pattern, strictly decreasing elasticity, unique adjacent crossings, endpoint clipping, and the complete tie classification. This is the preferred first standalone formalization target.
3. **Paper I, finite Bernoulli algebra.** Formalize pivotal derivatives, pair-shadow reduction and positivity on active faces, coefficient log-concavity, and the two structured perturbations.
4. **Paper I, Gamma analysis.** Formalize tail-to-density integral representations, differentiation under the integral, endpoint asymptotics, the Riccati minimum argument and its strict constants, and the common-response criterion.
5. **Paper I, assembly and shape boundaries.** Treat compactness and boundary activation explicitly, including n = k, k = 1, shape = 1, and shape below one. Then add support asymptotics and the Hessian result.
6. **Paper I, global support phases.** Formalize cumulative-hazard geometry, the density-ratio crossing lemma, strict exponential and Gamma quantile-ratio orders, and their endpoint limits. Add the exponential-spacing interpolation, Prékopa–Leindler step with the positive-measure strictness argument, adjacent-tie maximality, ordered transitions, and all allocation equality cases. Leading-coefficient ties, q0 > k, and the q0 = n empty crossing list are required cases, not optional corollaries.

Use the labels in [docs/statement_registry.json](docs/statement_registry.json) as the manuscript-to-Lean correspondence keys. The two main theorems are independent: Paper II is not a dependency of Paper I, and vice versa.

When work begins, use a root `lakefile.toml`, pinned `lean-toolchain` and Mathlib dependency/manifest, a root `MdsCoverageOptimization.lean`, and a `MdsCoverageOptimization/` module tree. Add Lean CI only when there is real formalized content. Keep proposed tasks distinct from completed coverage and apply [FORMALIZATION_AUDIT.md](FORMALIZATION_AUDIT.md).
