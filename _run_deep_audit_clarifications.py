#!/usr/bin/env python3
"""Repair quoting in the generated one-use script, execute it, and normalize text."""
from pathlib import Path
import runpy

root = Path(__file__).resolve().parent
path = root / "_apply_deep_audit_clarifications.py"
lines = path.read_text().splitlines()
out = []
for line in lines:
    if "self.assertIn(r'a_1" in line:
        out.append("        self.assertIn(\"a_1'(x)=\\\\frac{(x+1)e^{-x}-1}{x^2}<0\", self.cloud)")
    elif "self.assertIn(r'\\begin{proof}\\nIf" in line:
        out.append("        self.assertIn(r'If \\(q\\) is optimal, Theorem', self.cloud)")
    elif "self.assertIn('It is nonempty'" in line:
        out.append("        self.assertIn('nonempty:', self.gamma[self.gamma.index(density):])")
    else:
        out.append(line)
path.write_text("\n".join(out) + "\n")
runpy.run_path(str(path), run_name="__main__")

# Keep the generated patch clean.  This removes only trailing horizontal
# whitespace and leaves all mathematical content and line structure intact.
for relative in [
    "gamma_mds_active_uniform.tex",
    "terminal_cloud_staircase.tex",
    "README.md",
    "THEOREM_STATUS.md",
    "FORMALIZATION_STATUS.md",
    "FORMALIZATION_AUDIT.md",
    "docs/DEEP_AUDIT_CLARIFICATIONS.md",
    "docs/INTEGRATION_AUDIT.md",
    "docs/PROOF_DEPENDENCIES.md",
    "docs/deep_audit_validation.json",
    "scripts/test_audit_regressions.py",
]:
    target = root / relative
    text = target.read_text()
    target.write_text("\n".join(row.rstrip() for row in text.splitlines()) + "\n")
