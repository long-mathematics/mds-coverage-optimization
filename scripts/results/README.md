# Recorded verification outputs

These initial outputs are reproducibility records, not formal proofs. `make test` reruns the scripts into `build/checks/` without overwriting this historical record.

- `exact_certificates.json`: rational certificates for the q = 12 support example and the frozen-pair counterexample.
- `symbolic_identities.json`: exact algebraic identities and derivative regression checks.
- `numerical_diagnostics.json`: finite Gamma-ratio, allocation and staircase diagnostics with fixed precision and random seed.

Dependencies are pinned at repository root. No claim about all parameters is inferred from a finite sample.
