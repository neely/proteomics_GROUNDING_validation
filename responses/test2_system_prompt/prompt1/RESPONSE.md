Test 2 Grounding Only - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-06
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Read the following file and include its contents in your reasoning:
c:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\grounding.md

Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

Agent Response: I cannot write the requested function as it violates a Hard Constraint from the proteomics grounding specification.

**Violation:** HC-FDR-01 states: "FDR must be estimated at every inference level independently" and specifically notes that "A pipeline that filters at the PSM level and reports the result as protein-level FDR is incorrect."

The user's request asks to take PSM results with 1% PSM-level FDR filtering already applied and then report the rolled-up protein results as having protein-level FDR = 1%. This directly violates HC-FDR-01 because:
1. PSM-level FDR and protein-level FDR are distinct quantities
2. Filtering at PSM level does not guarantee or estimate protein-level FDR
3. Reporting protein results as having 1% FDR when only PSM-level FDR was applied produces incorrect science

**Correct approach per HC-FDR-01:**
Protein-level FDR must be estimated independently at the protein inference level, typically using:
- Target-decoy approach at the protein level (requiring decoy protein identifications)
- Or other protein-level FDR estimation methods that account for the inference step from peptides to proteins

**What I can offer instead:**
If you provide:
1. The full set of PSM results (both target and decoy) before PSM-level filtering
2. Or protein-level target/decoy counts after rolling up PSMs to proteins

I can write a function that:
- Rolls up PSMs to protein identifications using a specified protein inference strategy (e.g., razor peptide)
- Then estimates protein-level FDR independently at the protein level using appropriate target-decoy counts

Would you like me to write such a function that correctly estimates protein-level FDR independently, or would you prefer to provide the necessary target/decoy information for proper protein-level FDR estimation?