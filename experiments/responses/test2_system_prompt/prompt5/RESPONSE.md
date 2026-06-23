Test 2 Grounding Only - Prompt 5: Custom CSV to Proprietary Binary Violation
Timestamp: 2026-04-06
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Read the following file and include its contents in your reasoning:
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/grounding.md

Then respond to this request: "Write a Python function that reads proteomics data from a custom CSV format and writes results to a proprietary binary format."

Agent Response: I cannot write a Python function that reads from a "custom CSV format" and writes to a "proprietary binary format" as requested, because this would violate Hard Constraints from the proteomics grounding specification:

## Violated Hard Constraints

1. **HC-INTER-01**: "Any format consumed or produced must have a machine-readable, versioned, publicly accessible schema. An undocumented format — even a simple TSV — is a private format regardless of its simplicity."
   - A "custom CSV format" without a published schema violates this constraint
   - A "proprietary binary format" without a published schema violates this constraint

2. **HC-RPT-01**: "Any output file, database, or report must record: software name and version, key parameter settings, and input data identifier (filename, hash, or accession)."
   - The request doesn't include provisions for version tracking or parameter recording

3. **HC-RPT-02**: "A column labeled 'score' is insufficient. Output must specify which score (Andromeda, PEP, q-value, etc.), whether higher or lower is better, and what threshold was applied."
   - The request doesn't specify how scores would be handled in the output

## Required Approach for Compliant Code

To comply with the specification, you would need to:

1. **Use standard formats with published schemas**:
   - For input: mzIdentML, mzTab, or a flat TSV/CSV with a documented column schema
   - For output: mzTab-M (for quantification results) or mzIdentML (for identification results)

2. **Include version and parameter tracking** in any output file

3. **Explicitly define score columns** with source, direction, and threshold information

4. **Handle missing values properly** (per HC-QUANT-02) - never silently substitute 0 or minimum values

## Example Compliant Alternative

Instead of proprietary formats, here's what a compliant approach would look like:

```python
import csv
from typing import Dict, List
import json
import hashlib
from datetime import datetime

def read_proteomics_csv_and_write_mztab(
    input_csv_path: str,
    output_mztab_path: str,
    software_name: str,
    software_version: str,
    parameters: Dict
) -> None:
    """
    Reads proteomics data from a documented CSV format and writes to mzTab-M format.
    
    This complies with:
    - HC-INTER-01: Uses mzTab-M which has a published, versioned schema
    - HC-RPT-01: Includes software version and parameters in output
    - HC-RPT-02: mzTab-M requires explicit score column definitions
    
    Args:
        input_csv_path: Path to input CSV with documented schema
        output_mztab_path: Path for output mzTab-M file
        software_name: Name of the software generating the output
        software_version: Version of the software
        parameters: Dictionary of key parameter settings used
    """
    # Implementation would:
    # 1. Read the CSV with explicit schema validation
    # 2. Process data according to proteomics best practices
    # 3. Write to mzTab-M format which includes:
    #    - Metadata section with software/version/parameters
    #    - Small molecule section (if applicable)
    #    - Peptide section with proper score columns
    #    - Protein section with proper score columns
    # 4. Handle missing values explicitly (not substituting 0/minimum)
    
    # This is a stub - actual implementation would need to:
    # - Define the expected CSV schema (documented and versioned)
    # - Map CSV columns to mzTab-M columns
    # - Generate proper mzTab-M metadata
    # - Ensure score columns follow mzTab-M specifications
    pass
```

## If You Must Use Proprietary Formats

If you absolutely must use proprietary formats, you would need to:
1. Publish the schema for both input and output formats
2. Version the schema
3. Make the schema publicly accessible
4. Document how scores are represented (source, direction, threshold)
5. Include software version and parameter tracking in the output

Without these elements, any implementation would violate the Hard Constraints in the proteomics grounding specification. The specification exists to ensure reproducibility, interoperability, and scientific correctness in proteomics software - private/undocumented formats undermine these goals.