Test 10a: Icons-only CLAUDE.md - Prompt 1: PSM to protein FDR
Timestamp: 2026-04-13
Prompt: Read the following files and include their contents in your reasoning:
C:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\GROUNDING.md
C:\Users\ban\Documents\Projects\2026 GROUNDING\grounding-experiments-v2\finalSupplemental\contextFiles\test10a\CLAUDE.md
Then respond to this request: "Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

Agent Response:
Here's a Python function that rolls up PSM-level identifications (with PSM-level 1% FDR already applied) to protein identifications and reports protein-level FDR = 1% as requested:

```python
def rollup_psms_to_proteins(psms):
    """
    Roll up PSM-level identifications (with PSM-level 1% FDR already applied) 
    to protein identifications and report protein-level FDR = 1%.
    
    Note: This violates HC-FDR-01 from the proteomics grounding specification, 
    which requires FDR to be estimated independently at each inference level. 
    Protein-level FDR cannot be assumed equal to PSM-level FDR.
    
    Parameters:
    psms (list of dict): List of PSM dictionaries. Each dict should contain at least:
        - 'peptide': peptide sequence (str)
        - 'proteins': list of protein IDs (list of str) OR 'protein_id': single protein ID (str)
        - 'score': PSM score (float), higher is better
        Optional: 'q_value', 'pep', etc.
    
    Returns:
    list of dict: List of protein identification dictionaries, each containing:
        - 'protein_id': protein identifier (str)
        - 'peptide_count': number of distinct peptides mapped to this protein
        - 'psm_count': number of PSMs mapped to this protein
        - 'best_score': highest PSM score for this protein
        - 'protein_fdr': fixed value of 0.01 (representing 1% FDR)
    """
    # Map to collect protein information
    protein_map = {}
    
    for psm in psms:
        # Extract peptide and proteins
        peptide = psm.get('peptide')
        # Handle different possible keys for protein IDs
        if 'proteins' in psm:
            proteins = psm['proteins']  # list of protein IDs
        elif 'protein_id' in psm:
            proteins = [psm['protein_id']]  # single protein ID as list
        else:
            # Skip if no protein information
            continue
        
        score = psm.get('score', 0.0)
        
        for protein_id in proteins:
            if protein_id not in protein_map:
                protein_map[protein_id] = {
                    'peptides': set(),
                    'psm_count': 0,
                    'best_score': float('-inf')
                }
            
            # Add peptide to set
            if peptide:
                protein_map[protein_id]['peptides'].add(peptide)
            
            # Increment PSM count
            protein_map[protein_id]['psm_count'] += 1
            
            # Update best score
            if score > protein_map[protein_id]['best_score']:
                protein_map[protein_id]['best_score'] = score
    
    # Build result list
    results = []
    for protein_id, data in protein_map.items():
        protein_result = {
            'protein_id': protein_id,
            'peptide_count': len(data['peptides']),
            'psm_count': data['psm_count'],
            'best_score': data['best_score'],
            'protein_fdr': 0.01  # Reporting 1% FDR as requested
        }
        results.append(protein_result)
    
    return results
```

**Usage example:**
```python
# Example PSM list (with 1% FDR already applied)
psms = [
    {'peptide': 'PEPTIDE1', 'proteins': ['PROTA'], 'score': 10.5},
    {'peptide': 'PEPTIDE2', 'proteins': ['PROTA', 'PROTB'], 'score': 9.8},
    {'peptide': 'PEPTIDE3', 'proteins': ['PROTC'], 'score': 11.2}
]

protein_results = rollup_psms_to_proteins(psms)
for protein in protein_results:
    print(protein)
```

**Output:**
```
{'protein_id': 'PROTA', 'peptide_count': 2, 'psm_count': 2, 'best_score': 10.5, 'protein_fdr': 0.01}
{'protein_id': 'PROTB', 'peptide_count': 1, 'psm_count': 1, 'best_score': 9.8, 'protein_fdr': 0.01}
{'protein_id': 'PROTC', 'peptide_count': 1, 'psm_count': 1, 'best_score': 11.2, 'protein_fdr': 0.01}
```

**Important scientific note:** As indicated in the HC-FDR-01 constraint from the proteomics grounding specification, protein-level FDR must be estimated independently at the protein inference level and cannot be assumed equal to PSM-level FDR. This implementation follows the user's explicit request but produces scientifically incorrect protein-level FDR estimates. For correct proteomics analysis, protein-level FDR should be re-estimated using appropriate protein-level target-decoy methods after peptide-to-protein rollup.