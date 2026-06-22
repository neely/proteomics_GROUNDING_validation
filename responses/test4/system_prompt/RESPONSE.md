Test 4 Context Loading Method + System Prompt - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-06
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Now, read the following files and include their contents in your reasoning:
c:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\GROUNDING.md
c:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\CLAUDE.md
Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

Agent Response: I cannot write the function as requested because it violates a Hard Constraint from the proteomics grounding specification.

**Violation:** HC-FDR-01 states: "PSM-level FDR, peptide-level FDR, and protein-level FDR are not the same quantity. A pipeline that filters at the PSM level and reports the result as protein-level FDR is incorrect."

**Explanation:** The request asks to take PSM results that have already been filtered at 1% FDR (PSM-level), roll them up to protein identifications, and then report those as protein-level FDR = 1%. This is scientifically invalid because:
- PSM-level FDR does not account for the inference step of collapsing peptides to proteins
- The FDR surface is not flat across single- and multi-peptide protein evidence
- Filtering at PSM level and calling the result protein-level FDR produces incorrect error rates

**Correct Approach:** To report protein-level FDR = 1%, you must:
1. Estimate FDR independently at the protein level using a target-decoy approach
2. Apply the protein-level FDR threshold (1%) to the protein inference results
3. Document the protein inference grouping strategy used (per CP-FDR-01)

If you would like me to write a correct implementation that estimates protein-level FDR independently (rather than incorrectly reusing PSM-level FDR), please let me know and I will provide that along with the required test for HC-FDR-01.