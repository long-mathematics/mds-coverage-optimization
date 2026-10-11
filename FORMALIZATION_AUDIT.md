# Formalization audit policy

No formalization audit has passed yet, because this repository has no Lean code. Do not infer certification from the absence of placeholder files.

For future coverage claims require all of the following:

- A clean build with the pinned toolchain and dependencies, and reproducible Lean CI.
- No `sorry`, `admit`, custom theorem axioms, or imported proof assumptions replacing manuscript arguments.
- Transitive-axiom inspection for public theorems, with a documented foundational whitelist (for example Lean's standard classical choice/propositional extensionality/quotient soundness as actually used), not merely a source grep.
- A statement-correspondence review: domain, positivity, independence, total-budget constraint, quantifier order, every equality case, and boundary cases must agree with the manuscript.
- A dependency ledger distinguishing fully proved theorems from conditional reductions and wrappers.

Priority pitfalls: an active-face theorem is not a global theorem; a numerical grid is not an interval theorem; the existence of an active-uniform optimizer is weaker than classification of all optimizers; shape-one degeneracy cannot be omitted; expected-cloud and MDS-tail objectives must not be identified.

For the global Gamma/MDS support theorem, check the strict direction of the quantile ratio and the CDF crossing separately. Non-strict log-concavity alone does not prove the exact tie classification. The geometric-support interpolation must agree with integer support values, the strictness argument must establish positive measure, and a leading-coefficient tie must imply strict global dominance. The staircase begins at the largest leading-coefficient maximizer q0, which need not equal k; q0 = n produces no crossing list. A candidate-response geometry theorem cannot replace the active-uniform allocation theorem.
