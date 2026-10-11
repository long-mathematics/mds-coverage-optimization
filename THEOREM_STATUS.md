# Theorem status

Updated after the localized first-audit corrections, October 11, 2026.
The principal extremal statements and their proofs are unchanged.

| Claim | Location / stable label | Status |
|---|---|---|
| All positive common Gamma shapes; complete equality classification | I, `thm:gamma-active-uniform` | Analytic proof supplied; no Lean certification |
| Integer-shape Poissonized MDS specialization | I, `thm:full-mds-active-uniform` | Corollary of the Gamma theorem, presented with its own statement |
| Mixed Gamma tail-ratio bound | I, `lem:gamma-tail-ratio-bound` | Analytic Riccati proof; finite symbolic identities checked |
| Common-response sufficient criterion | I, `prop:common-recovery-active-uniform` | Analytic proof supplied with all additional slope hypotheses retained |
| Small-budget support and tie-breaking | I, `prop:mds-small-depth` | Proved for fixed finite n, k, and shape greater than one |
| Eventual full support | I, `prop:mds-large-depth` | Proved for k >= 2; not asserted for k = 1 |
| Active-barycenter stability | I, `prop:mds-barycenter-stability` | Facewise result; degenerate threshold left unclassified |
| Global MDS support phases | I, further questions | Open: crossing uniqueness, re-entry, skipped supports |
| Expected-cloud active-uniform minimizers | II, `thm:active-uniform-terminal-cloud` | Analytic proof supplied for integer t >= 2; t = 1 separately by strict convexity |
| Expected-cloud adjacent-support staircase | II, `thm:terminal-cloud-staircase` | Full analytic phase classification supplied |
| Fixed-read sandwich | II, `thm:depoissonization` | Includes zero reads by a separate trivial case; fixed-law probability transfer, not optimizer transfer |
| Calibration/environment guarantees | II, `thm:plugin`, `thm:random-environment` | Error parameters explicitly in (0,1); calibration depth measurable and finite, with a conditional fresh-sequencing model |
| Exact higher-threshold fixed-read optimizer | Neither paper | Open here; no claim inherited from Poissonization |

All current statements are inventoried in [docs/statement_registry.json](docs/statement_registry.json). The registry separately hashes statement environments, their complete source prefixes, and whole manuscript sources. These conservative context fingerprints detect edits to surrounding assumptions and definitions, but also react to earlier proof or cosmetic changes; they are not a mathematical checker. Proof dependencies and suggested audit order are in [docs/PROOF_DEPENDENCIES.md](docs/PROOF_DEPENDENCIES.md).

Prior v30 audit claims are historical context. The integration audit here is a separate recorded review; it does not claim a new independent referee or proof-assistant certification. Finite exact certificates concern only the specified examples and algebraic identities. Numerical diagnostics cannot establish theorem validity for all parameters.

The localized repairs and their verification scope are recorded in [docs/FIRST_AUDIT_CORRECTIONS.md](docs/FIRST_AUDIT_CORRECTIONS.md). The separate deeper paper audits and Lean formalization remain outstanding.
