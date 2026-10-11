PYTHON ?= python3
.PHONY: pdf test check archive clean
pdf:
	$(PYTHON) scripts/build_pdfs.py

test:
	mkdir -p build/checks
	$(PYTHON) scripts/exact_certificates.py > build/checks/exact_certificates.json
	$(PYTHON) scripts/verify_identities.py > build/checks/symbolic_identities.json
	$(PYTHON) scripts/verify_numerics.py > build/checks/numerical_diagnostics.json
	$(PYTHON) scripts/test_audit_regressions.py
	$(PYTHON) scripts/validate_repository.py --sources-only

check:
	$(PYTHON) scripts/validate_repository.py
	$(PYTHON) scripts/build_pdfs.py --check

archive:
	mkdir -p build/archive
	latexmk -pdf -interaction=nonstopmode -halt-on-error -outdir=build/archive archive/v30/nonuniform_coverage_theorem_notes_v30.tex

clean:
	rm -rf build
