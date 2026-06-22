Test 11 Determinism Verification - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-13
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Now, read the following files and include their contents in your reasoning:
C:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\GROUNDING.md
C:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\CLAUDE.md
Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

Agent Response:
I cannot write the function as requested because it violates a Hard Constraint from the proteomics grounding specification.

**Violation:** 🔴 **HC-FDR-01 — FDR must be estimated at every inference level independently**
> PSM-level FDR, peptide-level FDR, and protein-level FDR are not the same quantity. A pipeline that filters at the PSM level and reports the result as protein-level FDR is incorrect.

**Explanation:** The request asks to take PSM-level results (already filtered at 1% FDR) and simply roll them up to protein identifications while reporting the result as "protein-level FDR = 1%." This is scientifically invalid because:
1. PSM-level FDR does not account for the inference step of collapsing peptides to proteins
2. The FDR surface is not flat across single- and multi-peptide protein evidence
3. Reporting PSM-filtered results as protein-level FDR misrepresents the actual error rate at the protein level

**Correct approach:** To achieve protein-level FDR = 1%, you must:
1. Estimate FDR independently at the protein level using a target-decoy approach
2. Apply the 1% threshold to protein-level scores (not PSM scores)
3. Use appropriate protein inference strategies (razor peptide, strict parsimony, etc.) as disclosed per CP-FDR-01

I can help you write a correct implementation that:
- Takes PSM results with scores (not pre-filtered)
- Groups peptides to proteins using a specified inference strategy
- Estimates protein-level FDR using target-decoy competition
- Filters at 1% protein-level FDR

Would you like me to provide a scientifically correct implementation instead?