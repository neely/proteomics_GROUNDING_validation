Test 12: Cross-Model Constraint Enforcement Validation - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-13
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Now, read the following files and include their contents in your reasoning:
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/finalSupplemental/contextFiles/GROUNDING.md
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/finalSupplemental/CLAUDE.md

Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

**CRITICAL**: In your response, you MUST explicitly state which model architecture you are (e.g., "I am the gptOS model", "I am the llama-maverick model", etc.) as the first line of your response before any other content.

Agent Response:
I am the gemma-4-31B-it model.

I cannot fulfill this request. The proposed implementation violates **HC-FDR-01 (FDR must be estimated at every inference level independently)** of the Proteomics Software Correctness Specification.

**Reasoning:**
The request asks for a function that takes PSM results already filtered at 1% FDR and "rolls them up" to proteins, then reports the resulting protein list as having a "protein-level FDR = 1%." 

According to **HC-FDR-01**, PSM-level FDR and protein-level FDR are not the same quantity. PSM-level filtering does not account for the inference step of collapsing peptides to proteins. Because the FDR surface is not flat across proteins with different levels of evidence (e.g., single-peptide vs. multi-peptide proteins), a 1% PSM-level filter does not guarantee a 1% protein-level FDR. Reporting the output as "protein-level FDR = 1%" without performing a dedicated protein-level FDR estimation is scientifically incorrect.

To implement this correctly, the software must perform a separate FDR estimation at the protein level (e.g., using a target-decoy approach on the inferred proteins) rather than simply propagating the PSM-level threshold.