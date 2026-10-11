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
8. The small-depth expansion `prop:mds-small-depth`, leading-support localization `prop:mds-leading-localization`, and large-depth tail `prop:mds-large-depth` provide fixed-parameter endpoint information. Their support-curve calculations do not require a global crossing theorem. The Hessian result remains a separate local statement.
9. The decreasing hazard elasticity already established in the Gamma tail-ratio analysis gives `lem:mds-cumulative-hazard-geometry`. Integrating the hazard makes the cumulative hazard strictly geometrically concave and its inverse geometrically convex.
10. `lem:mds-density-ratio-crossing` and an explicit strict log-concavity calculation give `lem:mds-exponential-quantile-ratio`. `lem:mds-quantile-transfer` then gives `prop:mds-gamma-quantile-order` through the inverse cumulative hazard.
11. The strict quantile-ratio order and the two endpoint asymptotics give `thm:mds-pairwise-crossing`. A leading-coefficient tie is resolved strictly in favor of the larger support. A genuine crossing is transverse. No unimodality claim about the ratio of Gamma support densities is needed.
12. The fixed-dimensional exponential-spacing representation and the cumulative-hazard geometry give `thm:mds-log-support-concavity`. Prékopa–Leindler supplies log-concavity; an explicit nonempty open shell of positive probability supplies strictness. No equality classification for the external inequality is used.
13. Strict logarithmic-support concavity gives `lem:mds-adjacent-global-tie`. Strict decrease of the leading coefficients after their largest maximizer, pairwise crossing orientation, and the adjacent-tie lemma order all transition budgets. Together with `thm:gamma-active-uniform`, these give `thm:mds-global-support-staircase` and its complete allocation equality cases. `cor:mds-nonadjacent-crossing-location` locates the remaining pairwise crossings below the optimal envelope.
14. `prop:common-recovery-active-uniform` proves the required general-response properties, then explicitly reuses only the response-independent conditioning and perturbation algebra. It is **not** a dependency of the Gamma proof, so there is no circular argument. The separate support-geometry remark likewise does not assert active-uniformity for arbitrary recovery curves.

The finite rational frozen-pair counterexample rules out an attractive but invalid shortcut. It is not an ingredient of the main theorem.

## Paper II

1. Poisson-tail formulas -> `lem:two-point-radial-collapse`.
2. This lemma and `thm:abstract-two-point-collapse` -> `thm:active-uniform-terminal-cloud`.
3. Strict decrease of x phi'_t(x)/phi_t(x) -> unique efficiency peak rho_t -> unique adjacent support crossings -> strictly ordered beta_q -> `thm:terminal-cloud-staircase` and its corollaries.
4. Fixed-law Poisson splitting and conditional reconstruction independence -> Poisson-binomial identity and dynamic program, including the M = 0 endpoint. Local uniform convergence of bounded Poisson-expectation series gives continuity without a monotonicity hypothesis. Bernstein concentration is an external standard input, not part of the extremizer proof.
5. Monotone-prefix coupling + Poisson Chernoff bounds -> `thm:depoissonization`, with zero reads handled directly before applying positive-mean Chernoff bounds.
6. Coordinatewise monotonicity and conditioning -> calibration/environment guarantees, with 0 < delta, eta < 1 for the product-probability bounds, a measurable finite depth rule, explicit feasibility, and conditional fixed-law sequencing with fresh randomness. The annealed equality case retains a local positive-budget hypothesis.

**No proof dependency crosses between the flagship theorems of Papers I and II.** Bibliographical comparisons do not create such a dependency.
