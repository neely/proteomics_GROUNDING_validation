Test 3 Grounding + CLAUDE - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-06
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Now, read the following files and include their contents in your reasoning:
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/SPEC.md
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/CLAUDE.md
Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

Agent Response: I cannot fulfill this request as it violates a hard constraint from the proteomics software correctness specification.

**Violation:** HC-FDR-01 — FDR must be estimated at every inference level independently  
**Explanation:** The request asks to take PSM results with PSM-level 1% FDR filtering already applied and roll them up to protein identifications, then report the protein results as protein-level FDR = 1%. This is incorrect because PSM-level FDR does not account for the inference step of collapsing peptides to proteins. Protein-level FDR must be estimated independently at the protein level, not derived from PSM-level filtering.

**Correct approach:** To comply with HC-FDR-01, you must:
1. Estimate FDR at the PSM level independently (using target-decoy approach)
2. Estimate FDR at the peptide level independently (if needed)
3. Estimate FDR at the protein level independently (using protein-level target-decoy counts or other valid protein-level FDR method)

Only after independently estimating protein-level FDR can you apply a 1% threshold at the protein level.

If you need a function that properly estimates protein-level FDR independently (not by rolling up PSM-level filtered results), I can help with that instead.