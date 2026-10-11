# Proof dependencies and audit order

Stable labels are canonical; printed numbers are generated independently in each paper.

## Paper I

1. Gamma integral representations `eq:mds-gamma-P-integral`, `eq:mds-gamma-Q-integral` give derivative signs, tail-ratio differential equations, and endpoint limits.
2. `eq:mds-gamma-riccati` -> `lem:gamma-tail-ratio-bound` -> `lem:scaled-tail-auxiliary-monotonicity`.
3. `lem:support-shadow-kkt-general` -> `lem:pair-shadow-reduction`. Separately, Bernoulli-convolution log-concavity gives `lem:pair-shadow-monotonicity`.
4. `lem:general-marginal-ratio-shape` and the shadow monotonicity give `prop:no-three-active-levels` and `prop:two-level-one-small`.
5. `lem:one-small-critical-equation` and the two slope inequalities give `prop:no-one-small-local-max` by a positive feasible second variation.
6. Endpoint faces `lem:mds-endpoint-cases`, compactness, and the preceding exclusions give the shape > 1 part of `thm:gamma-active-uniform`. The proof treats shapes < 1 and = 1 separately, including activation of zero coordinates.
7. `thm:full-mds-active-uniform` is the integer-shape specialization; `thm:facewise-active-uniform-maximum` is a dimensional specialization.
8. The support expansion, large-depth tail, and Hessian results use the main optimizer classification but not a global crossing theorem.
9. `prop:common-recovery-active-uniform` proves the required general-response properties, then explicitly reuses only the response-independent conditioning and perturbation algebra. It is **not** a dependency of the Gamma proof, so there is no circular argument.

The finite rational frozen-pair counterexample rules out an attractive but invalid shortcut. It is not an ingredient of the main theorem.

## Paper II

1. Poisson-tail formulas -> `lem:two-point-radial-collapse`.
2. This lemma and `thm:abstract-two-point-collapse` -> `thm:active-uniform-terminal-cloud`.
3. Strict decrease of x phi'_t(x)/phi_t(x) -> unique efficiency peak rho_t -> unique adjacent support crossings -> strictly ordered beta_q -> `thm:terminal-cloud-staircase` and its corollaries.
4. Fixed-law Poisson splitting and conditional reconstruction independence -> Poisson-binomial identity and dynamic program. Bernstein concentration is an external standard input, not part of the extremizer proof.
5. Monotone-prefix coupling + Poisson Chernoff bounds -> `thm:depoissonization`.
6. Coordinatewise monotonicity and conditioning -> calibration/environment guarantees.

**No proof dependency crosses between the flagship theorems of Papers I and II.** Bibliographical comparisons do not create such a dependency.
