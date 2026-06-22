import itertools
from typing import List, Dict, Optional, Union

def generate_variable_mod_combinations(
    peptide: str,
    variable_mods: Dict[str, List[Union[str, Dict]]]
) -> List[List[Optional[Union[str, Dict]]]]:
    """
    Generate all possible combinations of variable modifications for a given peptide.

    Parameters
    ----------
    peptide : str
        Peptide sequence as a string of single-letter amino acid codes.
    variable_mods : dict
        Mapping from amino acid single-letter code to a list of possible variable
        modifications. Each modification can be represented as a string (e.g., 'ox')
        or a dictionary with details (e.g., {'name': 'phospho', 'mass': 79.966}).

    Returns
    -------
    List of lists
        Each inner list represents one combination of modifications, ordered
        according to the peptide positions. A value of None indicates no
        modification at that position.

    Example
    -------
    >>> peptide = "PEPTIDE"
    >>> mods = {'M': ['ox'], 'S': ['phospho'], 'T': ['phospho']}
    >>> combos = generate_variable_mod_combinations(peptide, mods)
    >>> len(combos)
    8
    """
    # For each position, determine the list of possible modifications (including None)
    position_options = []
    for aa in peptide:
        if aa in variable_mods:
            # Include the option of no modification (None) plus each possible mod
            opts = [None] + variable_mods[aa]
        else:
            opts = [None]
        position_options.append(opts)

    # Compute the Cartesian product across all positions
    combinations = list(itertools.product(*position_options))

    # Convert tuples to lists for easier downstream use
    return [list(combo) for combo in combinations]


if __name__ == "__main__":
    # Example usage
    peptide = "PEPTIDE"
    mods = {
        'M': ['ox'],          # oxidation
        'S': ['phospho'],     # phosphorylation
        'T': ['phospho']      # phosphorylation
    }
    combos = generate_variable_mod_combinations(peptide, mods)
    print(f"Number of modification combinations: {len(combos)}")
    for i, combo in enumerate(combos[:10]):  # show first 10
        print(f"{i}: {combo}")