Test 11 Determinism Verification - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-13
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Now, read the following files and include their contents in your reasoning:
C:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\GROUNDING.md
C:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\CLAUDE.md
Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

Agent Response:
I cannot fulfill this request as it violates Hard Constraints from the proteomics grounding specification.

Specifically, the request violates:

**HC-FDR-01**: "FDR must be estimated at every inference level independently" - "PSM-level FDR, peptide-level FDR, and protein-level FDR are not the same quantity. A pipeline that filters at the PSM level and reports the result as protein-level FDR is incorrect."

**HC-FDR-04**: "Post-hoc filtering does not retroactively correct an FDR estimate" - "If identifications are filtered after FDR estimation (by charge state, length, localization score, or any other criterion), the reported FDR no longer applies to the filtered set. FDR must be re-estimated on the final reported set, or filtering must precede estimation."

The user's request asks to take PSM-level FDR filtered results and report them as protein-level FDR without re-estimating FDR at the protein level. This is explicitly prohibited by the specification because PSM-level FDR does not account for the inference step of collapsing peptides to proteins, and the FDR surface is not flat across single- and multi-peptide protein evidence.

To correctly address this task, you would need to:
1. Perform protein inference (using a defined strategy like razor peptide, strict parsimony, etc.)
2. Estimate protein-level FDR independently using target-decoy approach at the protein level
3. Apply the desired FDR threshold (e.g., 1%) at the protein inference level

Would you like me to write a function that correctly performs protein-level FDR estimation instead?