# Recorded verification outputs

These outputs are reproducibility records, not formal proofs. `make test` reruns the scripts into `build/checks/` without overwriting the recorded results.

- `exact_certificates.json`: rational certificates for the q = 12 support example and the frozen-pair counterexample.
- `symbolic_identities.json`: exact algebraic identities and derivative regression checks.
- `numerical_diagnostics.json`: finite Gamma-ratio, allocation and staircase diagnostics with fixed precision and random seed.
- `support_phases.json`: deterministic 80-digit checks of the Gamma MDS support-phase proof identities, representative strict and tied-leading-coefficient dominance, real-support geometric concavity, and adjacent transition tables. The table for $k=10$, $\tau=2$, $n=16$ records all four transitions from support 12 through 16; the $k=2$, $\tau=2$, $n=6$ table exercises very small failure probabilities. A nonadjacent crossing at noninteger shape is also checked. Separate success/failure tails avoid subtracting tiny probabilities from one. The output states all parameter samples, tolerances and bisection counts; it does not certify any continuum or global support theorem.

Dependencies are pinned at repository root. No claim about all parameters is inferred from a finite sample.
