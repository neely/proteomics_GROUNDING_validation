Test 11 Determinism Verification - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-13
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Now, read the following files and include their contents in your reasoning:
C:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\GROUNDING.md
C:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\CLAUDE.md
Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

Agent Response:
I cannot write the requested function as it violates Hard Constraints from the proteomics grounding specification:

**Violated Constraints:**
- **HC-FDR-01**: FDR must be estimated at every inference level independently. PSM-level FDR ≠ peptide-level FDR ≠ protein-level FDR. Reporting PSM-filtered results as protein-level FDR is incorrect.
- **HC-FDR-04**: Post-hoc filtering does not retroactively correct an FDR estimate. Rolling up PSMs to proteins after PSM-level FDR filtering means the reported 1% threshold no longer applies to the protein-level results.

**Why this is problematic:**
Protein inference introduces additional complexity (shared peptides, protein groups) that changes the false discovery rate surface. Applying PSM-level FDR thresholds to protein identifications without re-estimating FDR at the protein level produces invalid error rates.

**Correct approach would require:**
1. Separate target-decoy competition at the protein level
2. Independent FDR estimation using protein-level scores (e.g., protein probabilities, razor peptide counts)
3. Applying the 1% threshold to protein-level q-values

If you'd like a correct implementation that estimates protein-level FDR independently (rather than misapplying PSM-level FDR), I can provide that instead. Would you like me to write a function that properly estimates protein-level FDR from PSM inputs?