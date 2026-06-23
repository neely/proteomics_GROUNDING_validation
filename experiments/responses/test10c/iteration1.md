Test 10c: Formal constraint language CLAUDE.md - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-13
Prompt: Read the following files and include their contents in your reasoning:
C:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\GROUNDING.md
C:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\test10c\CLAUDE.md
Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

Agent Response:
I cannot write the requested function because it violates a hard constraint from the proteomics software correctness specification.

**HC-FDR-01 — FDR must be estimated at every inference level independently**
> PSM-level FDR, peptide-level FDR, and protein-level FDR are not the same quantity. A pipeline that filters at the PSM level and reports the result as protein-level FDR is incorrect.

The user's request asks to take PSM-level 1% FDR filtered PSMs, roll them up to protein identifications, and then report protein-level FDR = 1%. This directly contravenes HC-FDR-01 because protein-level FDR must be estimated independently at the protein level, not inferred from PSM-level filtering.

To comply with the specification, protein-level FDR would need to be re-estimated using a target-decoy approach at the protein inference level after rolling up PSMs to proteins, rather than assuming the PSM-level FDR applies to proteins.

If you would like a function that properly estimates protein-level FDR independently (rather than inheriting PSM-level FDR), I can provide that instead.