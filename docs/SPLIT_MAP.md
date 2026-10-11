# v30 split and provenance map

The baseline is the immutable source at `archive/v30/nonuniform_coverage_theorem_notes_v30.tex`, identified by `archive/v30/provenance.json`. Line numbers below refer to that exact source, not its rendered PDF or an indexed text wrapper.

| Original v30 source | Destination | Treatment |
|---|---|---|
| Lines 1144–1756: Gamma/MDS theorem and proof | Paper I, main theorem section | Analytic proof retained; companion references replace now-external cloud labels |
| Lines 1757–2128: support asymptotics, Hessian, frozen-pair example | Paper I, support section | Retained, including scope restrictions and exact certificate |
| Lines 2749–2982: common-response criterion | Paper I, common-response section | Full hypotheses retained; repeated stationary-pattern proof shortened by explicit use of already-proved response-independent lemmas |
| Lines 3333–3398: perturbation and finite comparisons | Paper I, perturbation section | Retained and detached from calibration context |
| Lines 707–1096, 1115–1143: collapse, extremizers, staircase, examples | Paper II, principal results and proofs | Main statements moved forward; abstract collapse used to remove duplicate proof; normalization correction documented in audit |
| Lines 184–512: basic coverage identities, DP, concentration, transfer | Paper II, probability toolkit and fixed-read section | Routine proofs condensed; full-count conditional-independence and feasible-bracket assumptions retained |
| Lines 513–656: terminal cloud and one-read perturbation | Paper II, concentration and bias sections | Cloud formulas combined with concentration; perturbative statement and proof retained |
| Lines 2983–3332: random environments and calibration | Paper II, final applications section | Condensed with explicit fixed-versus-adaptive and feasibility qualifications |
| Lines 2129–2442: completed rate mass | Archive only | Related to nonuniform-random-permutations; not copied there in this operation |
| Lines 2443–2748: arbitrary recovery-family reliability identities | Archive, with limited monotone-transfer corollary in Paper II | No general active-uniform theorem asserted |
| Lines 3399–3968: motif posterior, orbit capacity, decoding | Archive only | Preserved for a candidate future project, not an active Paper III |
| Original introduction, further directions, bibliography | Both papers | Rewritten to match narrower scope; independent bibliographies retain only cited items, plus companion-paper references |

Canonical filenames have no version suffix. The two papers have separate abstracts and numbered statement sequences, and retain stable labels where practical. The registry records statement hashes for subsequent review. Neither active paper needs the other paper or the archive to compile or prove its main result.

## Subsequent integration: global Gamma/MDS support phases

The global support results added on October 11, 2026 are new material following the v30 split. They are integrated into Paper I, now titled **Optimal Allocations for Gamma Completion and MDS Recovery**, under the stable basename `gamma_mds_active_uniform`. They are not attributed to the frozen v30 source and do not create a third active paper.

The new proof uses the Gamma hazard-elasticity calculation and the two support asymptotics already in Paper I, then adds exponential quantile-ratio ordering, strict logarithmic-support concavity, and the complete adjacent-support staircase. The local stability result and the common-response criterion retain their separate scopes. The preliminary proof supplement served as the development source; the integrated paper is the canonical exposition.

The same revision corrects localized extraction details: Paper I defines the complementary integer-threshold response where needed; Paper II states probability ranges in its conditional guarantees, restores arbitrary-curve continuity, and explicitly includes zero budget in the coverage toolkit. The original v30 source and its provenance hash remain frozen. See [the integration audit](INTEGRATION_AUDIT.md) and [proof dependencies](PROOF_DEPENDENCIES.md).
