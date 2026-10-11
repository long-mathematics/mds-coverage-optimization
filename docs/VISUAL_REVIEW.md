# Initial PDF visual review

October 11, 2026. Both PDFs were rendered with PyMuPDF at 1.15x scale. All 21 pages of Paper I and 13 pages of Paper II were reviewed in contact sheets, and the main-theorem pages (Paper I page 3; Paper II page 2) were inspected individually. No clipping, overlapping equations, broken mathematical glyphs, or unexpected blank pages were observed. The standard 11pt font and 1.1-inch margins are unchanged; the reduced length comes from scope and exposition, not smaller typography.

The main Gamma theorem is on page 3. The two cloud main statements begin on page 2, with the staircase statement continuing onto page 3. Long proofs continue normally across pages.

This is a layout review, not an independent mathematical certification. Future source changes require fresh inspection of affected pages. CI checks compile warnings and PDF text correspondence but does not certify visual appearance.

## First-audit corrections, October 11, 2026

Rendered the locally rebuilt corrected sources with MuPDF and compared
page renders against the corresponding initial local PDFs. The only
changed page in Paper I is page 12. Paper II changes pages 2 and 8--13
and adds bibliography page 14; all other corresponding pages render
identically in this local comparison. Inspected all affected pages at
readable resolution: the comparison formula, toolkit hypotheses,
continuity proof, zero-read case, random-environment domains, annealed
assumptions, calibration rule, and reference continuation are legible,
with no clipping, overlap, or broken glyphs. The local PDFs are 21 and
14 pages. Font size and margins are unchanged.

This is a visual check of local builds of the corrected sources, not an
independent mathematical audit or a claim of byte-identical output across
TeX installations. GitHub Actions separately rebuilds and validates the
tracked source/PDF pair on its runner.
