# PDF visual review

## Deep-audit clarity revisions, October 11, 2026

The clean-runner PDFs contain **28 pages** in Paper I and **14 pages** in Paper II. Before-and-after PDFs were retained in the workflow artifact, rendered with the repository PDF tools, and compared page by page. All pages of both revised manuscripts were inspected in contact sheets. Paper I pages 5, 6, 9, 12, 19, 21, 22, and 23 and Paper II pages 4, 5, 7, and 11 were additionally inspected individually at full rendered resolution because they contain the principal deep-audit clarifications.

Paper I pages 1--4 render identically to the preceding version. The added proof details begin on page 5 and cause normal downstream reflow, increasing the manuscript from 27 to 28 pages. The explicit mixed-Gamma parameters and endpoint expansion, normalized Newton inequality, boundary-activation calculations, density-ratio details, inverse-asymptotic rules, Prékopa hypotheses, and renamed beta-form Laplace parameter are all legible. Paper II pages 1--3 and 6 render identically; the compactness sentence, threshold-one derivative, support-localization proof, and averaging step appear cleanly on pages 4, 5, 7, and 11.

No clipping, overlapping text or equations, broken mathematical glyphs, unexpected blank pages, isolated headings, or margin violations were found. The added page in Paper I is a normal consequence of the expanded proof text rather than a typography change. Both papers retain 11pt text and 1.1-inch margins, and both TeX builds are warning-free. This is a visual/layout review, not mathematical or proof-assistant certification.

## Global-support integration, October 11, 2026

The current PDFs contain **27 pages** in Paper I and **14 pages** in Paper II. Both were rendered with PyMuPDF at 1.35x scale. All pages were inspected in contact sheets. Paper I pages 1–4, 12, 17–23, and 27 and Paper II pages 1–2 and 8–14 were additionally inspected individually at the rendered resolution.

The new complete support staircase is Theorem 1.1, entirely on page 2. A deliberate page break prevents its heading and initial hypothesis from being stranded at the foot of the title page. After that adjustment, pages 1–4 were rendered and reviewed again; rendered pages 5–27 were unchanged. The original Gamma optimizer classification remains Theorem 2.1, on pages 3–4. The pairwise crossing theorem begins on page 17; the support-concavity statement, cumulative-hazard geometry, quantile argument, strict Prékopa argument, ordered phases, and numerical table occupy pages 18–23.

After combining the first-audit corrections from PR #3, the only changed rendered page in Paper I was page 12; its new global-support proof and all other pages were unchanged. Paper II changed pages 2 and 8–13 and added bibliography page 14. All of these affected pages were inspected individually after rebuilding.

Paper II's zero-budget toolkit and continuity correction appear on pages 8–9; the zero-read case is on page 10; the explicit probability ranges and annealed hypotheses appear on page 12; the calibration rule and further questions appear on page 13; the updated companion citation is on page 14. The principal expected-cloud results and their positive-budget hypotheses are retained.

No clipping, overlapping equations, broken mathematical glyphs, unexpected blank pages, or isolated theorem headings remain in the inspected output. Both papers retain 11pt text and 1.1-inch margins. All TeX builds are warning-free. The source/PDF hashes and page counts are recorded in [pdf_manifest.json](pdf_manifest.json).

## Initial split (historical record)

October 11, 2026. Both PDFs were rendered with PyMuPDF at 1.15x scale. All 21 pages of Paper I and 13 pages of Paper II were reviewed in contact sheets, and the main-theorem pages (Paper I page 3; Paper II page 2) were inspected individually. No clipping, overlapping equations, broken mathematical glyphs, or unexpected blank pages were observed. The standard 11pt font and 1.1-inch margins are unchanged; the reduced length comes from scope and exposition, not smaller typography.

The main Gamma theorem is on page 3. The two cloud main statements begin on page 2, with the staircase statement continuing onto page 3. Long proofs continue normally across pages.

This is a layout review, not an independent mathematical certification. Future source changes require fresh inspection of affected pages. CI checks compile warnings and PDF text correspondence but does not certify visual appearance.

## First-audit corrections, October 11, 2026 (historical record)

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
