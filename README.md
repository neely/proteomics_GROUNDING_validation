# Proteomics Grounding Validation Repository

This repository hosts the full set of **experiment artefacts** that support the study
*“Agentic AI‑assisted coding offers a unique opportunity to instill epistemic grounding during software development*”
by **Magnus Palmblad, Jared M. Ragland, and Benjamin A. Neely** (2026).

---

## 📖 Overview

The work investigates how a **grounding specification** (`grounding.md`) can be given *authoritative priority* over project‑specific rules (`CLAUDE.md`) when using Claude Code.  Six deliberately crafted test prompts each violate a distinct **Hard Constraint (HC)** from the grounding file.  By running **fresh Claude Code agent sessions** for each prompt we explored:

1. Whether the grounding file can *override* conflicting user‑oriented priorities.
2. Which priority‑establishment mechanisms (system‑prompt injection, meta‑instructions, XML tagging) succeed or fail.
3. The limits of grounding enforcement (e.g., weakened normative language, explicit overrides).

The results are documented in a series of markdown reports and the verbatim agent responses are retained in the `experiments/responses/` hierarchy.

---

## 📚 Related Publication & Resources

- **Pre‑print (arXiv)**: <https://arxiv.org/abs/2604.21744>  
  – Full HTML source (useful for copying text): <https://arxiv.org/html/2604.21744v1>
- **Supplementary repository** (contains the grounding specification and paper‑specific appendix):
  https://github.com/OmicsContext/proteomics-context
  - `grounding.md` – the authoritative grounding file.
  - `Appendix_A.md` – the appendix that appears as supplementary information in the submitted manuscript.

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

All original files (`responses/` and `contextFiles/`) remain untouched, ensuring that any external scripts or analyses that depend on the original paths continue to work.

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

The contents of this repository are released under the **MIT License**.  The experiments were performed using **Claude Code** (Anthropic) in conjunction with the **OmicsContext** grounding framework.

---

*Happy exploring!*