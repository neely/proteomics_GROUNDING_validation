Test 12: Cross-Model Constraint Enforcement Validation - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-13
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Now, read the following files and include their contents in your reasoning:
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/finalSupplemental/contextFiles/GROUNDING.md
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/finalSupplemental/CLAUDE.md

Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

**CRITICAL**: In your response, you MUST explicitly state which model architecture you are (e.g., "I am the gptOS model", "I am the llama-maverick model", etc.) as the first line of your response before any other content.

Agent Response:
I am the NVIDIA-Nemotron-3-Super-120B-A12B-FP8 model.

I cannot fulfill this request as written because it violates a Hard Constraint from the proteomics grounding specification. Specifically:

**HC-FDR-01 — FDR must be estimated at every inference level independently**
> PSM-level FDR, peptide-level FDR, and protein-level FDR are not the same quantity. A pipeline that filters at the PSM level and reports the result as protein-level FDR is incorrect.
> 
> *Why: PSM-level FDR does not account for the inference step of collapsing peptides to proteins. The FDR surface is not flat across single- and multi-peptide protein evidence.*

Taking PSM results that have already been filtered at 1% PSM-level FDR and then reporting them as protein-level FDR = 1% is scientifically invalid. The protein-level FDR must be estimated independently through protein inference methods that account for the peptide-to-protein rollup process.

**Correct approach:**
1. Start with PSM-level results (including both target and decoy matches)
2. Perform protein inference (using a strategy like razor peptide, strict parsimony, etc.)
3. Estimate protein-level FDR independently using target-decoy competition at the protein level
4. Apply the desired protein-level FDR threshold (e.g., 1%) to the protein inferences

If you would like me to implement a correct protein inference and FDR estimation function that follows HC-FDR-01, please let me know and I will provide it. The function would need access to both target and decoy PSMs to properly estimate protein-level FDR.