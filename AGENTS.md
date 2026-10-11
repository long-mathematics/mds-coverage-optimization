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
- Every theorem, lemma, proposition and corollary must have a stable label. After an intentional statement edit, regenerate `docs/statement_registry.json` using `python scripts/validate_repository.py --write-registry --sources-only`, and review its diff.
- Run `make test`, `make pdf`, and `make check`. Commit matching sources, PDFs, and `docs/pdf_manifest.json`. Visually inspect affected PDF pages; a text comparison is not a visual audit.
- New finite checks belong in `scripts/`; label their scope and use deterministic seeds. They do not prove a continuum inequality or global optimizer theorem.
- README math uses `$...$` or `$$...$$`, expanded standard commands, and no isolated line containing only `=` or `-`. Keep all manuscript and related-work links valid.
- Neither expected-cloud optimality nor Poissonized transfer establishes fixed-read or MDS support-phase optimality. Facewise stability is not global maximality. Keep these boundaries explicit.

## Formalization

Follow `FORMALIZATION_STATUS.md` and `FORMALIZATION_AUDIT.md`. When formalization begins, use a pinned root-level Lake project with `MdsCoverageOptimization.lean` and `MdsCoverageOptimization/`, not a separate `formalization/` project. Do not introduce `sorry`, `admit`, custom proof axioms, or tautological redefinitions to claim coverage. A clean kernel build must be accompanied by statement-correspondence and transitive-axiom audits.

## Context-sensitive statement registry

Registry schema 2 records each statement environment, its complete preceding source prefix, and the whole manuscript source. Review context/source hash changes as well as statement hashes; a changed surrounding assumption or definition is mathematically relevant even when a theorem environment is unchanged. Prefix hashes are deliberately conservative, not semantic dependency analysis. Do not refresh the registry merely to silence a failure without reviewing the source diff.
