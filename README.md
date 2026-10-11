# MDS coverage optimization

Research manuscripts by **Christopher D. Long** on two closely related allocation problems: Gamma/MDS deadline success and the expected terminal low-count cloud.

## Papers

| Paper | Main result | Manuscript |
|---|---|---|
| **I. Active-Uniform Laws for Gamma Completion and MDS Recovery** | Complete common-Gamma optimizer classification; support asymptotics, local stability, and a common-response criterion | [PDF](gamma_mds_active_uniform.pdf) · [LaTeX](gamma_mds_active_uniform.tex) |
| **II. Nonuniform Coverage and the Terminal-Cloud Staircase** | Active-uniform expected-defect minimizers and an exact adjacent-support staircase | [PDF](terminal_cloud_staircase.pdf) · [LaTeX](terminal_cloud_staircase.tex) |

The initial PDFs have **21 pages** (Paper I) and **13 pages** (Paper II). Both manuscripts are standalone. The principal theorem is stated near the beginning of each paper. Their cross-references are bibliographical: neither flagship theorem depends on the companion theorem.

### Paper I: deadline success

Let $F_\tau$ be the unit-rate Gamma distribution function with common shape $\tau>0$. For independent $B_i$ with success probabilities $F_\tau(\lambda_i)$ and total intensity $\sum_i\lambda_i=M$,

$$
\max_{\lambda_i\ge0,\,\sum_i\lambda_i=M}\mathbb P\!\left(\sum_i B_i\ge k\right)
=\max_{k\le q\le n}\mathbb P\!\left(\mathrm{Bin}(q,F_\tau(M/q))\ge k\right).
$$

For $\tau>1$, **every maximizer is uniform on its positive support**, with an optimal support size on the right. For $0<\tau<1$, full uniformity is uniquely optimal. At $\tau=1$, full uniformity is uniquely optimal for $k\ge2$, whereas every allocation ties for $k=1$. For $\tau>1,k=1$, optimal support has size one. Integer shapes recover the Poissonized MDS model.

The paper supplies an analytic proof using Bernoulli-shadow equations and a real-parameter Gamma tail-ratio inequality. It also proves small-budget support selection, eventual full support for $k\ge2$, and an exact constrained-Hessian test. **Global MDS crossing uniqueness, support re-entry, and skipped-support transitions remain open.** A local maximum on a fixed face need not be globally optimal.

### Paper II: expected terminal cloud

For integer $t\ge2$, put $\psi_t(x)=\mathbb P(\mathrm{Poisson}(x)<t)$. Then

$$
\min_{\lambda_i\ge0,\,\sum_i\lambda_i=M}\sum_i\psi_t(\lambda_i)
=\min_{1\le q\le n}\left(n-q+q\psi_t(M/q)\right).
$$

All minimizers are active-uniform. The optimal support grows through a **proved adjacent-support staircase**, with unique ordered crossings and no skipped supports. At $t=1$, full uniformity is uniquely optimal. Fixed-read transfer, concentration, and calibration guarantees are included as tools for specified sampling laws.

The expected-defect objective is not the MDS success probability. The staircase theorem does **not** establish a staircase for Paper I.

## Status and scope

These are research manuscripts with analytic proofs, **not proof-assistant-certified results**. Numerical diagnostics are not proofs. See [theorem status](THEOREM_STATUS.md), the [statement registry](docs/statement_registry.json), [integration audit](docs/INTEGRATION_AUDIT.md), and [formalization roadmap](FORMALIZATION_STATUS.md).

This is not a general DNA-storage or transfer-calculus collection. Motif-channel posterior inference, capacity, orbit methods, and decoding are excluded from the active papers. The completed-rate-mass theorem is also excluded; its natural connection is to [nonuniform-random-permutations](https://github.com/long-mathematics/nonuniform-random-permutations). Cross-referencing that project does not import its proofs or its formalization status.

The exact 69-page v30 **source** is frozen in [archive/v30](archive/v30/README.md), including the material omitted from these papers. It is historical, not a third active manuscript. See the [split and provenance map](docs/SPLIT_MAP.md). No other repository is modified by this initialization.

## Reproduce

Requirements: Python 3.12 or later, `latexmk`, `pdflatex`, Latin Modern and the standard AMS/geometry/enumitem/hyperref/microtype packages, and Poppler (`pdfinfo`, `pdftotext`). Python dependencies are pinned in [requirements.txt](requirements.txt).

```sh
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
make test
make pdf
make check
```

`make test` runs exact rational certificates, symbolic identities, and deterministic finite numerical diagnostics. Results are written to `build/checks/`; recorded initial outputs are in [scripts/results](scripts/results/README.md). `make pdf` builds both PDFs and updates the source/PDF hash manifest. `make check` checks provenance, stable statements, internal references, local README links, and warning-free rebuilds, and compares rebuilt PDF text against the tracked PDFs. Different TeX versions need not produce byte-identical PDFs; hashes certify the stored source/PDF pair, while rebuild checks compare extracted text.

`make archive` optionally compiles the frozen master. `make clean` removes build products, not the tracked PDFs or archive. No Lean project or placeholder theorem is included; see [formalization audit policy](FORMALIZATION_AUDIT.md).

## Workflow and licensing

Use feature branches, focused pull requests, review of mathematical statement changes, passing **Build and audit manuscripts** checks, and squash merges. Do not substitute computational tests for proof or silently promote archival material. Instructions for future contributors are in [AGENTS.md](AGENTS.md).

Manuscripts and exposition: **CC BY 4.0**. Code and build tooling: **MIT**. See [LICENSE](LICENSE) and [citation metadata](CITATION.cff).
