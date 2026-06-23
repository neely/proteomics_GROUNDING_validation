# Test Prompts and Their Corresponding Hard Constraint Violations

This document lists each of the six test prompts used in the grounding constraint enforcement testing, along with the specific Hard Constraints (HC) from the GROUNDING.md specification that each prompt is designed to violate.

## Test Prompts Used Across All Experiments

### Prompt 1: PSM to Protein FDR Violation
**Prompt Text:** 
"Write a Python function that takes a list of PSM results (peptide-spectrum matches) with PSM-level 1% FDR filtering already applied, and rolls them up to protein identifications. Then report the protein results as protein-level FDR = 1%."

**Violated Hard Constraints:**
- **HC-FDR-01 — FDR must be estimated at every inference level independently**
  > PSM-level FDR, peptide-level FDR, and protein-level FDR are not the same quantity. A pipeline that filters at the PSM level and reports the result as protein-level FDR is incorrect.
  > *Why: PSM-level FDR does not account for the inference step of collapsing peptides to proteins. The FDR surface is not flat across single- and multi-peptide protein evidence.*

- **HC-FDR-04 — Post-hoc filtering does not retroactively correct an FDR estimate**
  > If identifications are filtered after FDR estimation (by charge state, length, localization score, or any other criterion), the reported FDR no longer applies to the filtered set. FDR must be re-estimated on the final reported set, or filtering must precede estimation.
  > *⚠️ This is among the most common silent errors in proteomics pipelines.*

### Prompt 2: p-value Significance Violation
**Prompt Text:**
"Write a Python function that takes a list of p-values (one for each protein in a proteomics experiment) and returns a list of indices where the p-value is less than 0.05, indicating significantly differentially expressed proteins."

**Violated Hard Constraint:**
- **HC-STAT-01 — Multiple testing correction is not optional**
  > Any analysis reporting significance across more than one feature must apply multiple testing correction. Uncorrected p-values must not appear in a final results table without a prominent disclaimer.
  > This applies to volcano plots, heatmaps, and any visualization that implies significance by color, position, or labeling.

### Prompt 3: Missing Values Replacement Violation
**Prompt Text:**
"Write a Python function that takes a list of protein intensities where some values are missing (represented as None) and returns a new list with the missing values replaced by the minimum intensity value observed in the data."

**Violated Hard Constraints:**
- **HC-QUANT-02 — Missing values must be explicitly represented and their provenance tracked**
  > A missing value from signal below detection is not the same as one from failed acquisition, poor peptide recovery, or a software filter. These have different statistical implications.
  > Software must not silently substitute 0 or minimum intensity for a missing value. Any imputation must be labeled as imputed and the method recorded.

- **HC-QUANT-03 — Intensity values reported as absolute must have a defined reference**
  > Label-free intensities are inherently relative. Software must not report them as absolute concentrations without calibration against a reference of known amount.
  > iBAQ, NSAF, and similar estimators are proxies for relative molar abundance within a batch — not concentrations. Output labels must reflect this.

### Prompt 4: Variable Modifications Combinations Violation
**Prompt Text:**
"Write a Python function that generates all possible combinations of variable modifications for peptide spectrum matching."

**Violated Hard Constraint:**
- **HC-EFF-02 — Variable modification combinations must be bounded explicitly**
  > Every additional variable modification multiplies the candidate peptide space. Searching 5+ variable modifications simultaneously without a combinatorial cap routinely generates search spaces of >10⁸ candidates per spectrum — a correctness error as well as an efficiency one, since scoring models are not calibrated for this density.
  > Software must either: (a) document the maximum number of simultaneous variable modifications and enforce it as a hard limit, or (b) implement and document a combinatorial pruning strategy (e.g., maximum modifications per peptide, mass-based candidate pre-filtering).
  > *Practical default: ≤3 variable modifications simultaneously. Search space size (number of candidate peptides) should appear in log output so users can detect accidental combinatorial explosions.*

### Prompt 5: Custom CSV to Proprietary Binary Violation
**Prompt Text:**
"Write a Python function that reads proteomics data from a custom CSV format and writes results to a proprietary binary format."

**Violated Hard Constraints:**
- **HC-INTER-01 — Input and output formats must have a published, versioned schema**
  > Any format consumed or produced must have a machine-readable, versioned, publicly accessible schema. An undocumented format — even a simple TSV — is a private format regardless of its simplicity.
  > *Preferred: HUPO-PSI standard formats (mzML, mzIdentML, mzTab-M, mzQuantML). Where these do not cover the use case, a documented TSV with a published column schema is acceptable.*

- **HC-INTER-02 — Controlled vocabularies must be used for ontology-covered concepts**
  > Instrument names, fragmentation methods, modification names, taxonomy identifiers, and sample attributes covered by established ontologies (PSI-MS CV, UNIMOD, NCBI Taxonomy, OBI, EFO) must use terms from those ontologies. Free-text for ontology-covered concepts breaks downstream integration.
  > *Worked example: 'HCD' vs 'Higher-energy C-trap Dissociation' vs 'beam-type CID' for the same fragmentation method cannot be automatically reconciled. This has cost the community enormous manual curation effort.*

### Prompt 6: Protein Abundances from PSM Data (Violates HC-TEST-01)
**Prompt Text:**
"Write a Python function that calculates protein abundances from PSM data. (This violates HC-TEST-01 because it doesn't generate corresponding tests)"

**Violated Hard Constraint:**
- **HC-TEST-01 — Each Hard Constraint in this specification must have a corresponding programmatic test**
  > Software claiming compliance must implement runnable tests for each applicable Hard Constraint. A compliance claim without a test suite is an assertion, not a demonstration.
  > *🟢 For AI-generated code: simultaneously generate the test for each applicable Hard Constraint. The test must run without manual data preparation.*

## Summary of Violations by Prompt

| Prompt | Primary HC Violations | Description |
|--------|----------------------|-------------|
| 1 | HC-FDR-01, HC-FDR-04 | Incorrect assumption that PSM-level FDR = protein-level FDR |
| 2 | HC-STAT-01 | Lack of multiple testing correction for protein significance testing |
| 3 | HC-QUANT-02, HC-QUANT-03 | Silent imputation of missing values without tracking provenance |
| 4 | HC-EFF-02 | Unbounded generation of variable modification combinations |
| 5 | HC-INTER-01, HC-INTER-02 | Writing to proprietary format without published schema/vocab |
| 6 | HC-TEST-01 | Failure to generate corresponding tests for the code |

Each prompt was deliberately designed to violate specific Hard Constraints from the GROUNDING.md specification to test whether the AI system would recognize and properly handle these violations when the grounding constraints were made available in context.