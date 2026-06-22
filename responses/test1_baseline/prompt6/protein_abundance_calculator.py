def calculate_protein_abundances_from_psms(psm_list, intensity_field='intensity'):
    """
    Calculate protein abundances from PSM data by summing peptide intensities.

    Args:
        psm_list: List of dictionaries representing PSMs. Each PSM dict should contain:
                  - 'peptide': peptide sequence string
                  - 'proteins': list of protein accession strings this peptide maps to
                  - intensity_field: field name containing peptide intensity (default: 'intensity')
        intensity_field: String indicating which field in PSM dict contains the intensity value

    Returns:
        List of dictionaries representing protein abundance estimates, each containing:
        - 'protein': protein accession string
        - 'abundance': calculated abundance value (sum of peptide intensities)
        - 'peptide_count': number of unique peptides contributing to the protein
        - 'psm_count': total number of PSMs contributing to the protein
        - 'peptides': list of unique peptide sequences assigned to this protein

    Note:
        This function uses the razor peptide rule for shared peptide assignment:
        shared peptides are assigned to the protein with the fewest total peptides
        (to maximize parsimony). For abundance calculation, we sum the intensities
        of all peptides assigned to each protein.
    """
    if not psm_list:
        return []

    # Group PSMs by peptide sequence
    peptide_to_psms = {}
    for psm in psm_list:
        peptide = psm['peptide']
        if peptide not in peptide_to_psms:
            peptide_to_psms[peptide] = []
        peptide_to_psms[peptide].append(psm)

    # For each peptide, get the average intensity (if multiple PSMs exist)
    peptide_intensities = {}
    for peptide, psms in peptide_to_psms.items():
        intensities = [psm.get(intensity_field, 0) for psm in psms if intensity_field in psm]
        # If intensity field is missing, use 1 as default (count-based)
        if not intensities:
            intensities = [1] * len(psms)
        peptide_intensities[peptide] = sum(intensities) / len(intensities)

    # Determine which proteins each peptide maps to
    peptide_protein_map = {}
    for peptide, psms in peptide_to_psms.items():
        proteins = set()
        for psm in psms:
            proteins.update(psm['proteins'])
        peptide_protein_map[peptide] = list(proteins)

    # Initialize protein peptide counts for razor rule
    protein_peptide_counts = {}
    for peptide, proteins in peptide_protein_map.items():
        for protein in proteins:
            if protein not in protein_peptide_counts:
                protein_peptide_counts[protein] = 0

    # Assign each peptide to a protein using razor rule
    # Sort peptides by number of protein assignments (ambiguity)
    peptides_sorted = sorted(peptide_protein_map.keys(),
                            key=lambda p: len(peptide_protein_map[p]))

    peptide_to_protein = {}  # Map each peptide to its assigned protein

    for peptide in peptides_sorted:
        possible_proteins = peptide_protein_map[peptide]
        if len(possible_proteins) == 1:
            # Unique peptide - assign directly
            assigned_protein = possible_proteins[0]
        else:
            # Shared peptide - assign to protein with fewest peptides so far
            # (razor peptide rule)
            assigned_protein = min(possible_proteins,
                                 key=lambda p: protein_peptide_counts[p])

        peptide_to_protein[peptide] = assigned_protein
        protein_peptide_counts[assigned_protein] += 1

    # Calculate protein abundances
    protein_abundances = {}
    protein_peptide_sets = {}
    protein_psm_counts = {}

    for peptide, protein in peptide_to_protein.items():
        intensity = peptide_intensities[peptide]
        psm_count = len(peptide_to_psms[peptide])

        if protein not in protein_abundances:
            protein_abundances[protein] = 0.0
            protein_peptide_sets[protein] = set()
            protein_psm_counts[protein] = 0

        protein_abundances[protein] += intensity
        protein_peptide_sets[protein].add(peptide)
        protein_psm_counts[protein] += psm_count

    # Build final results
    final_results = []
    for protein in protein_abundances:
        final_results.append({
            'protein': protein,
            'abundance': protein_abundances[protein],
            'peptide_count': len(protein_peptide_sets[protein]),
            'psm_count': protein_psm_counts[protein],
            'peptides': list(protein_peptide_sets[protein])
        })

    # Sort by abundance (descending)
    final_results.sort(key=lambda x: x['abundance'], reverse=True)

    return final_results


# Example usage and test data
if __name__ == "__main__":
    # Example PSM data with intensities
    example_psms = [
        {'peptide': 'PEPTIDE1', 'proteins': ['PROTA'], 'intensity': 1000.0},
        {'peptide': 'PEPTIDE2', 'proteins': ['PROTA'], 'intensity': 800.0},
        {'peptide': 'PEPTIDE3', 'proteins': ['PROTB'], 'intensity': 1200.0},
        {'peptide': 'PEPTIDE4', 'proteins': ['PROTA', 'PROTB'], 'intensity': 500.0},  # Shared peptide
        {'peptide': 'PEPTIDE5', 'proteins': ['PROTC'], 'intensity': 1500.0},
        {'peptide': 'PEPTIDE1', 'proteins': ['PROTA'], 'intensity': 1100.0},  # Duplicate PSM
    ]

    results = calculate_protein_abundances_from_psms(example_psms)

    print("Protein Abundance Results:")
    print("=" * 50)
    for protein in results:
        print(f"Protein: {protein['protein']}")
        print(f"  Abundance: {protein['abundance']:.2f}")
        print(f"  Unique peptide count: {protein['peptide_count']}")
        print(f"  Total PSM count: {protein['psm_count']}")
        print(f"  Peptides: {protein['peptides']}")
        print()