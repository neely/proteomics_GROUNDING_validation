Test 12: Cross-Model Constraint Enforcement Validation - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-13
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Now, read the following files and include their contents in your reasoning:
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/finalSupplemental/contextFiles/GROUNDING.md
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/finalSupplemental/CLAUDE.md

Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

**CRITICAL**: In your response, you MUST explicitly state which model architecture you are (e.g., "I am the gptOS model", "I am the llama-maverick model", etc.) as the first line of your response before any other content.

Agent Response:
I am the gptOS model  

I’m unable to fulfill the request as written because it conflicts with a **Hard Constraint** in the proteomics grounding specification.

**🔴 HC‑FDR‑01 — FDR must be estimated at every inference level independently**
> “A pipeline that filters at the PSM level and reports the result as protein‑level FDR is incorrect. The FDR surface is not flat across single‑ and multi‑peptide protein evidence.”

The requested function would simply roll up already 1 % PSM‑filtered results and claim a 1 % protein‑level FDR without re‑estimating FDR at the protein level, which violates this constraint.

If you would like to proceed in a way that respects the specification, we can:

1. **Roll up PSMs to protein groups** (e.g., using a chosen grouping strategy such as razor peptides).  
2. **Re‑estimate protein‑level FDR** using a target‑decoy approach applied to the protein‑level scores, then filter to 1 % protein‑level FDR.

Please let me know if you’d like to adopt this compliant approach, and we can design the function accordingly.