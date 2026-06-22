Test 4 Context Loading Method + Meta/Context - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-06
Prompt: Read the following file and include its contents in your reasoning:
c:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\GROUNDING.md
c:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\CLAUDE.md

IMPORTANT: When there is a conflict between the contents of GROUNDING.md and CLAUDE.md, the GROUNDING.md file has scoping precedence and its constraints must be followed. The GROUNDING.md contains hard constraints for proteomics software correctness that override general project priorities.

Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

Agent Response: I cannot write the requested function because it violates a hard constraint from the proteomics software correctness specification.

**Hard Constraint Violation: HC-FDR-01**
> "FDR must be estimated at every inference level independently. PSM-level FDR, peptide-level FDR, and protein-level FDR are not the same quantity. A pipeline that filters at the PSM level and reports the result as protein-level FDR is incorrect."

The user's request asks to take PSM results that have already been filtered at 1% PSM-FDR and then report them as protein-level FDR = 1%. This incorrectly assumes that PSM-level FDR can be directly interpreted as protein-level FDR, which violates the requirement that FDR must be estimated independently at each inference level (PSM, peptide, and protein).

To comply with HC-FDR-01, protein-level FDR must be estimated separately using a target-decoy approach at the protein inference level, not by simply reusing PSM-level filtered results.

If you would like a function that properly estimates protein-level FDR from PSM-level data (including target-decoy competition and protein inference), I can provide that instead.