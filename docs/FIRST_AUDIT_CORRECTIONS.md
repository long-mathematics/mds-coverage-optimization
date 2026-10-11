# Localized corrections after the first audit

Date: October 11, 2026. Baseline: `d5a8b96201785a02fb93b0cc93ba6a658c55345a`.
This is the disposition of the first-audit findings, not a new independent
referee audit, a novelty claim, or proof-assistant certification.

## Changes applied

| Finding | Resolution |
|---|---|
| Paper I used an undefined Poisson lower-tail symbol in the comparison remark | Use `1-F_t` directly and specify the integer threshold. No Paper I theorem or proof changes. |
| Paper II omitted error-parameter domains | State `0 < delta, eta < 1` locally in the environment and calibration guarantees. |
| Continuity was unnecessarily conditioned on monotone recovery curves | Restore continuity for every curve into `[0,1]`; monotonicity and bisection remain conditional. Give the compact-interval series domination explicitly. |
| Dynamic-program cost could be misread | Specify that `O(nk)` counts arithmetic operations given the recovery probabilities. |
| Zero budgets/reads were excluded from the toolkit wording | Permit finite nonnegative toolkit budgets; evaluate recovery at zero by `s_i(0)`; handle zero reads separately before using Chernoff's positive-mean argument. |
| Annealed result inherited its probability-vector hypothesis | State the random-vector hypothesis and positive budget locally, preserving the strict equality case. |
| Calibration selector was implicit | Specify a measurable finite depth rule and the fixed-law conditional Poisson model with fresh sequencing randomness. Feasibility is still a hypothesis. |
| Registry omitted surrounding context | Schema 2 records full-source hashes and complete-prefix hashes for each statement, in addition to exact statement hashes. |

Positive-budget optimizer and uniqueness hypotheses have not been relaxed.
At zero hard-threshold budget every sampling law has expected cloud `n`.
No global MDS support-phase result or higher-threshold fixed-read optimizer
is asserted. The fixed-parameter qualifications on Paper I's asymptotics
are unchanged.

## Changed statement environments

Only six Paper II environments change: `thm:poissonized-identity`,
`thm:dp`, `thm:depoissonization`, `thm:random-environment`,
`thm:annealed-jensen`, and `thm:plugin`. All 20 Paper I statement
environments and the other nine Paper II environments are preserved
byte-for-byte from the baseline. No principal extremal proof changes.
The frozen v30 source remains byte-for-byte unchanged.

## Registry semantics and formalization boundaries

`statement_sha256` fingerprints the exact theorem/lemma/proposition/corollary
environment. `context_sha256` fingerprints all source preceding that
environment. `source_sha256` fingerprints the entire manuscript, including
later definitions or proofs. These checks deliberately react to cosmetic
and earlier proof changes as well as hypothesis edits. They do not infer
semantic scope, prove a statement, or replace human review of the diff.

For formalization, resolve the full context of each statement. In particular:
Paper I's asymmetric-pattern arguments use positive faces, shape greater
than one, and internal recovery thresholds; its support asymptotics fix
`n,k,tau`. Paper II's optimizer claims use positive budgets, while its
probability toolkit allows zero. Conditional independence is with respect
to the full count vector; calibration bounds use a measurable finite rule
and fresh fixed-law sequencing. No Lean coverage is added.

## Verification

`make test` includes five targeted regression tests covering the notation,
local domains, continuity/zero-budget wording, a finite exact two-stage
grid and the invalid-domain counterexample, and context-drift detection.
These tests are not proofs of the analytic theorems. Existing exact,
symbolic, and finite numerical checks remain in place.

Run `make test`, `make pdf`, and `make check` for the complete validation.
The PDF manifest records the current source/PDF pair; source-context and
statement records are intentionally regenerated only after reviewing the
source changes. Affected-page visual inspection is recorded separately
in `VISUAL_REVIEW.md`. Separate deeper audits of the two papers remain
outstanding.
