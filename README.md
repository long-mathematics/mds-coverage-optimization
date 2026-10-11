# MDS coverage optimization

Research manuscripts by **Christopher D. Long** on two closely related allocation problems: Gamma/MDS deadline success and the expected terminal low-count cloud.

## Papers

| Paper | Main result | Manuscript |
|---|---|---|
| **I. Optimal Allocations for Gamma Completion and MDS Recovery** | Complete common-Gamma optimizer classification and global support staircase, with unique transverse crossings and exact boundary ties | [PDF](gamma_mds_active_uniform.pdf) · [LaTeX](gamma_mds_active_uniform.tex) |
| **II. Nonuniform Coverage and the Terminal-Cloud Staircase** | Active-uniform expected-defect minimizers and an exact adjacent-support staircase | [PDF](terminal_cloud_staircase.pdf) · [LaTeX](terminal_cloud_staircase.tex) |

Both manuscripts are standalone, with principal results stated near the beginning. Their cross-references are bibliographical: neither paper's optimizer or staircase theorem depends on the companion theorem. The [PDF manifest](docs/pdf_manifest.json) records the current page counts and source/PDF hashes. Stable filenames are retained when a title or result changes.

### Paper I: deadline success

Let $F_\tau$ be the unit-rate Gamma distribution function with common shape $\tau>0$, let $1\le k\le n$, and let $M>0$. For independent $B_i$ with success probabilities $F_\tau(\lambda_i)$ and total intensity $\sum_i\lambda_i=M$,

$$
\max_{\lambda_i\ge0,\,\sum_i\lambda_i=M}\mathbb P\!\left(\sum_i B_i\ge k\right)
=\max_{k\le q\le n}\mathbb P\!\left(\mathrm{Bin}(q,F_\tau(M/q))\ge k\right).
$$

For $\tau>1$, **every maximizer is uniform on its positive support**, with an optimal support size on the right. For $0<\tau<1$, full uniformity is uniquely optimal. At $\tau=1$, full uniformity is uniquely optimal for $k\ge2$, whereas every allocation ties for $k=1$. For $\tau>1,k=1$, optimal support has size one. Integer shapes recover the Poissonized MDS model.

For $\tau>1$ and $2\le k\le n$, write

$$
V_q(M)=\mathbb P\!\left(\mathrm{Bin}(q,F_\tau(M/q))\ge k\right),
\qquad c(q)=\frac{\binom qk}{q^{\tau k}},
$$

and let $q_0$ be the **largest** integer maximizing $c(q)$ over $k\le q\le n$. The global support theorem gives the full phase diagram:

- For $q<r$, if $c(r)\ge c(q)$, then $V_r(M)>V_q(M)$ for every positive budget, including a tie of leading coefficients. Otherwise the curves have exactly one crossing, with $V_q>V_r$ before it and $V_r>V_q$ afterward; at the crossing $V_r'>V_q'>0$.
- A real-support interpolation of $V_q(M)$ is strictly log-concave as a function of $\log q$. An adjacent equality is a global tie, and two nonadjacent supports cannot both maximize.
- If $q_0<n$, the adjacent crossing budgets satisfy $0<\beta_{q_0}<\cdots<\beta_{n-1}<\infty$. Set $\beta_{q_0-1}=0$ and $\beta_n=\infty$. Support $q$ is uniquely optimal for $\beta_{q-1}<M<\beta_q$, and exactly $q,q+1$ tie at $M=\beta_q$. If $q_0=n$, full support is uniquely optimal for every $M>0$.

Thus **there is no support re-entry and no skipped transition after the initial support $q_0$**. Supports below $q_0$ are permanently dominated. The initial support can exceed $k$: for $k=10$, $\tau=2$, and $n=16$, the successive optimal supports are $12,13,14,15,16$.

| Transition | Budget $M$ (approximately) |
|---|---:|
| $12\to13$ | $3.751806808726$ |
| $13\to14$ | $8.851172168188$ |
| $14\to15$ | $14.333018261348$ |
| $15\to16$ | $20.197931039196$ |

The proof combines Gamma cumulative-hazard geometry, a strict quantile-ratio comparison for exponential order statistics, and the Prékopa–Leindler inequality. It reuses the active-uniform theorem and support asymptotics already proved in the paper. The [finite diagnostics](scripts/verify_support_phases.py) reproduce these transition values; they are supplementary evidence. The exact constrained-Hessian test is retained as a separate local result: a local maximum on a fixed face need not be globally optimal.

### Paper II: expected terminal cloud

For integer $t\ge2$, put $\psi_t(x)=\mathbb P(\mathrm{Poisson}(x)<t)$. Then

$$
\min_{\lambda_i\ge0,\,\sum_i\lambda_i=M}\sum_i\psi_t(\lambda_i)
=\min_{1\le q\le n}\left(n-q+q\psi_t(M/q)\right).
$$

All minimizers are active-uniform. The optimal support grows through a **proved adjacent-support staircase**, with unique ordered crossings and no skipped supports. At $t=1$, full uniformity is uniquely optimal. Fixed-read transfer, concentration, and calibration guarantees are included as tools for specified sampling laws.

The expected-defect objective and the MDS success probability have **separate analytic staircase proofs**. Optimizing one objective does not optimize the other. Fixed-read probability transfer likewise does not identify the exact higher-threshold fixed-read optimizer.

## Status and scope

These are research manuscripts with analytic proofs, **not proof-assistant-certified results**. Numerical diagnostics are not proofs. See [theorem status](THEOREM_STATUS.md), the [context-sensitive statement registry](docs/statement_registry.json), [integration audit](docs/INTEGRATION_AUDIT.md), [first-audit corrections](docs/FIRST_AUDIT_CORRECTIONS.md), [deep-audit clarifications](docs/DEEP_AUDIT_CLARIFICATIONS.md), and [formalization roadmap](FORMALIZATION_STATUS.md).

This is not a general DNA-storage or transfer-calculus collection. Motif-channel posterior inference, capacity, orbit methods, and decoding are excluded from the active papers. The completed-rate-mass theorem is also excluded; its natural connection is to [nonuniform-random-permutations](https://github.com/long-mathematics/nonuniform-random-permutations). Cross-referencing that project does not import its proofs or its formalization status.

The exact 69-page v30 **source** is frozen in [archive/v30](archive/v30/README.md), including the material omitted from these papers. It is historical, not a third active manuscript. The global MDS support results are a subsequent addition to Paper I. See the [split and provenance map](docs/SPLIT_MAP.md).

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

`make test` runs exact rational certificates, symbolic identities, deterministic finite numerical diagnostics including the MDS support transitions, and localized-audit regression tests. Results are written to `build/checks/`; recorded outputs and their scope are in [scripts/results](scripts/results/README.md). `make pdf` builds both PDFs and updates the source/PDF hash manifest. `make check` checks provenance, the statement and source-context registry, internal references, local README links, and warning-free rebuilds, and compares rebuilt PDF text against the tracked PDFs. Registry schema 2 fingerprints each statement, its complete source prefix, and the whole manuscript. Different TeX versions need not produce byte-identical PDFs; hashes identify the stored source/PDF pair, while rebuild checks compare extracted text.

`make archive` optionally compiles the frozen master. `make clean` removes build products, not the tracked PDFs or archive. No Lean project or placeholder theorem is included; see [formalization audit policy](FORMALIZATION_AUDIT.md).

## Workflow and licensing

Use feature branches, focused pull requests, review of mathematical statement changes, passing **Build and audit manuscripts** checks, and squash merges. Do not substitute computational tests for proof or silently promote archival material. Instructions for future contributors are in [AGENTS.md](AGENTS.md).

Manuscripts and exposition: **CC BY 4.0**. Code and build tooling: **MIT**. See [LICENSE](LICENSE) and [citation metadata](CITATION.cff).
