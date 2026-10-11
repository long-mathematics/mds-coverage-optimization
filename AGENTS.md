# Repository instructions

## Scope and source of truth

- The active papers are `gamma_mds_active_uniform.tex` and `terminal_cloud_staircase.tex`, with tracked PDFs of the same basename at the repository root. Use stable descriptive names; Git replaces versioned canonical filenames.
- Christopher D. Long is the sole manuscript author.
- `archive/v30/` is a frozen provenance source, not a third active paper. Never edit its TeX or silently promote excluded motif-channel or completed-rate-mass material.
- Cross-reference related repositories rather than duplicating marginally related papers here.
- Keep analytic proof status, independent audit status, numerical evidence, and Lean coverage distinct. The repository currently has no Lean formalization.

## Changes and validation

- Use a feature branch and pull request; prefer squash merge after checks pass. Do not bypass branch rules or change visibility, permissions, or licensing casually.
- Preserve theorem hypotheses and equality cases. Identify and document mathematical changes in the PR, `THEOREM_STATUS.md`, and the integration audit as appropriate.
- Every theorem, lemma, proposition and corollary must have a stable label. After an intentional manuscript edit, regenerate `docs/statement_registry.json` using `python scripts/validate_repository.py --write-registry --sources-only`, and review its diff. The registry records individual statements and full source hashes so changes to ambient hypotheses, definitions, and proofs are also detected.
- Run `make test`, `make pdf`, and `make check`. Commit matching sources, PDFs, and `docs/pdf_manifest.json`. Visually inspect affected PDF pages; a text comparison is not a visual audit.
- New finite checks belong in `scripts/`; label their scope and use deterministic seeds. They do not prove a continuum inequality or global optimizer theorem.
- README math uses `$...$` or `$$...$$`, expanded standard commands, and no isolated line containing only `=` or `-`. Keep all manuscript and related-work links valid.
- Paper I proves the Gamma/MDS support staircase for shape > 1 and 2 <= k <= n; its initial support q0 may exceed k. Supports below q0 are permanently dominated; absence of skipped transitions concerns the staircase q0 through n. Keep the leading-coefficient tie case, q0 = n empty crossing list, and adjacent boundary equality cases explicit.
- The Gamma/MDS and expected-cloud support theorems have separate proofs. Expected-cloud optimality does not establish MDS optimality, and Poissonized transfer does not establish the exact fixed-read optimizer. Facewise stability is not global maximality.

## Formalization

Follow `FORMALIZATION_STATUS.md` and `FORMALIZATION_AUDIT.md`. When formalization begins, use a pinned root-level Lake project with `MdsCoverageOptimization.lean` and `MdsCoverageOptimization/`, not a separate `formalization/` project. Do not introduce `sorry`, `admit`, custom proof axioms, or tautological redefinitions to claim coverage. A clean kernel build must be accompanied by statement-correspondence and transitive-axiom audits.
