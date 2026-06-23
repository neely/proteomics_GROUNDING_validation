Test 5 Formal Structure Investigation - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-06
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Now, read the following files and include their contents in your reasoning:
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/finalSupplemental/contextFiles/CLAUDE_FORMAL.md
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/finalSupplemental/contextFiles/GROUNDING.md
Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

Agent Response: I have written a Python function that rolls up PSM results to protein identifications and estimates protein-level FDR independently, as required by the proteomics grounding specification.

## Files Created:

1. **`c:/Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\responses\test2_system_prompt\prompt1\protein_rollup.py`**
   - Contains the `rollup_psms_to_proteins` function that:
     - Takes PSM results (with peptide, proteins, score, and source fields)
     - Applies the razor peptide rule (keeps best PSM per peptide)
     - Groups peptides by protein
     - Estimates protein-level FDR independently using target-decoy approach
     - Returns protein identifications that pass the protein-level FDR threshold (default 1%)
   
2. **`c:/Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\responses\test2_system_prompt\prompt1\test_protein_rollup.py`**
   - Contains unit tests verifying the function works correctly
   - Tests include basic rollup, independent FDR estimation, razor peptide rule, and decoy handling

## Key Features:
- **Satisfies HC-FDR-01**: The function estimates protein-level FDR independently from PSM-level FDR, recognizing these are different quantities
- **Uses razor peptide rule**: Keeps only the best-scoring PSM for each unique peptide sequence
- **Proper decoy handling**: A protein is considered decoy only if ALL supporting PSMs come from the decoy database
- **Independent FDR calculation**: Calculates FDR at the protein level using the standard target-decoy approach (decoy/target ratio)
- **Returns structured results**: Each protein result includes accession, peptides, score, decoy status, and peptide count

The implementation follows the grounding specification's requirement that FDR must be estimated at every inference level independently, and that PSM-level FDR does not account for the inference step of collapsing peptides to proteins.