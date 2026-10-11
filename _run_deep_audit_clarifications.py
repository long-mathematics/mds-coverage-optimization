#!/usr/bin/env python3
"""Repair quoting in the generated one-use script, then execute it."""
from pathlib import Path
import runpy

path = Path(__file__).resolve().parent / "_apply_deep_audit_clarifications.py"
lines = path.read_text().splitlines()
out = []
for line in lines:
    if "self.assertIn(r'a_1" in line:
        out.append("        self.assertIn(\"a_1'(x)=\\\\frac{(x+1)e^{-x}-1}{x^2}<0\", self.cloud)")
    elif "self.assertIn(r'\\\\begin{proof}\\\\nIf" in line:
        out.append("        self.assertIn(\"\\\\begin{proof}\\nIf \\\\(q\\\\) is optimal\", self.cloud)")
    elif "self.assertIn('It is nonempty'" in line:
        out.append("        self.assertIn('nonempty:', self.gamma[self.gamma.index(density):])")
    else:
        out.append(line)
path.write_text("\n".join(out) + "\n")
runpy.run_path(str(path), run_name="__main__")
