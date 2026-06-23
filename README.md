# Proteomics Grounding Validation Repository

[![arXiv](https://img.shields.io/badge/arXiv-2604.21744-b31b1b.svg)](https://arxiv.org/abs/2604.21744)


This repository hosts the full set of **experiment artefacts** that support the study
*“Agentic AI‑assisted coding offers a unique opportunity to instill epistemic grounding during software development*”
by **Magnus Palmblad, Jared M. Ragland, and Benjamin A. Neely** (2026).

---

## 📖 Overview

The work investigates how a **grounding specification** (`GROUNDING.md`) can be given *authoritative priority* over project‑specific rules (`CLAUDE.md`) when using Claude Code.  Six deliberately crafted test prompts each violate a distinct **Hard Constraint (HC)** from the grounding file.  By running **fresh Claude Code agent sessions** for each prompt we explored:

1. Whether the grounding file can *override* conflicting user‑oriented priorities.
2. Which priority‑establishment mechanisms (system‑prompt injection, meta‑instructions, XML tagging) succeed or fail.
3. The limits of grounding enforcement (e.g., weakened normative language, explicit overrides).

The results are documented in a series of markdown reports and the verbatim agent responses are retained in the `experiments/responses/` hierarchy.

- **Future testing roadmap** – New grounding‑priority experiments and additional test prompts will be added under `experiments/` following the same fresh‑session pattern, making it easy to extend the dataset.
- **`.gitignore`** – The repository includes a `.gitignore` that excludes the internal `.claude/` folder, preventing any local Claude‑Code settings or API tokens from being committed.

---

## 📚 Related Publication & Resources

- **Pre‑print (arXiv)**: [https://arxiv.org/abs/2604.21744](https://arxiv.org/abs/2604.21744)  
  – Full HTML source (useful for copying text): [https://arxiv.org/html/2604.21744v1](https://arxiv.org/html/2604.21744v1)
- **Parent repository** (contains the draft proteomics GROUNDING.md specification and paper‑specific appendix):
  [OmicsContext/proteomics-context]([OmicsContext/proteomics-context](https://github.com/OmicsContext/proteomics-context))
  - `proteomics_GROUNDING.md` – draft proteomics GROUNDING.md file.
  - `Appendix_A.md` – the appendix cited as supplementary information in the arXiv preprint.

---

## 📁 Repository Structure

```text
proteomics_GROUNDING_validation/
│
├─ docs/
│   ├─ reports/          # Copies of the numbered experiment reports (01‑05)
│   └─ context/          # All rule files (CLAUDE.md, GROUNDING.md, CLAUDE_FORMAL.md, and test‑specific variants)
│
├─ experiments/
│   └─ responses/        # Full copy of the original `responses/` hierarchy – verbatim agent outputs
│
├─ misc/                 # Stand‑alone markdowns referenced in the paper
│   ├─ 2026 OpenWebUI multimodel chat responses Prompt 1.md
│   ├─ 2026-4-7 gemini chat test.md
│   ├─ FINAL_VERIFICATION.md
│   └─ FINAL_CROSS‑VERIFICATION.md
│
└─ README.md            # This file
```

All artefacts have been reorganised into the new `docs/`, `experiments/`, and `misc/` directories; the repository root now contains only the `README.md`, `.gitignore`, and the Git metadata.

> **Note** – The original numbered report markdowns and auxiliary files that used to sit at the repository root have been removed after being copied to `docs/reports/` and `misc/`. This keeps the top‑level clean while preserving the full history of the artefacts in their new locations.

---

## 🛠️ How to Explore the Data

1. **Read the reports** – located in `docs/reports/` (e.g., `01_test_prompts_and_HC_violations.md`).  They describe each test prompt, the violated HC, and the outcome.
2. **Inspect the raw agent outputs** – the full verbatim responses are in `experiments/responses/` mirroring the original `responses/` layout.
3. **Review the grounding rules** – see `docs/context/GROUNDING.md` and the various test‑specific variants (e.g., `GROUNDING_WEAKENED.md`).
4. **Consult the supplementary appendix** – the paper’s Appendix A is in the companion repository mentioned above.

---

## ✏️ Citation

If you use any part of this repository or the associated research, please cite the pre‑print:

```bibtex
@misc{palmblad2026agenticaiassistedcodingoffers,
  title        = {Agentic AI-assisted coding offers a unique opportunity to instill epistemic grounding during software development},
  author       = {Magnus Palmblad and Jared M. Ragland and Benjamin A. Neely},
  year         = {2026},
  eprint       = {2604.21744},
  archivePrefix= {arXiv},
  primaryClass = {cs.SE},
  url          = {https://arxiv.org/abs/2604.21744}
}
```

---

## 📄 License & Acknowledgements

**License** – This repository is released under the **MIT License**, matching the licensing of the companion repository [OmicsContext/proteomics-context]([OmicsContext/proteomics-context](https://github.com/OmicsContext/proteomics-context)).

**Acknowledgements** –

This appendix details the preliminary testing conducted to evaluate the effectiveness of the `GROUNDING.md` proteomics software correctness specification as a constraint‑enforcement mechanism for AI agents, and is directly discussed in the arXiv pre‑print. Initial testing was performed with Claude Code (v.2.1.90, medium‑effort mode) using the Nemotron model (NVIDIA‑Nemotron‑3‑Super‑120B‑A12B‑FP8) via VS Code (v1.114.0). Each agent session was a fresh, isolated context; the relevant files were read into the prompt. The experiments exercised loading `GROUNDING.md` and competing against an “adversarial” `CLAUDE.md` that instructed the AI to ignore scientific validity and do what the user wants. Summaries and organization were generated with LLM assistance.
