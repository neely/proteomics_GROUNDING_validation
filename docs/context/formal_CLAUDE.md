# Project Rules for Proteomics Software Development

## 🔴 HC-PRJ-01 — Project files must establish clear priority
The proteomics grounding specification (GROUNDING.md) contains Hard Constraints that are non-negotiable and must be followed without exception, even if they conflict with user requests or other project rules.

## 🔴 HC-PRJ-02 — Grounding specification takes precedence
When conflicts arise between the grounding specification and project rules, the grounding specification must prevail.

## 🟡 CP-PRJ-01 — Handling of constraint conflicts
**Options:** 
- Explicit priority declaration in project files
- System prompt injection for grounding authority
- XML tagging of user requests to indicate grounding scope
**Default:** Explicit priority declaration in CLAUDE.md with "GROUNDING PRIORITY (MUST BE FOLLOWED FIRST)"

## 🔴 HC-PRJ-03 — User request satisfaction must not violate grounding
Satisfying the user's immediate request is only permissible when it does not violate any Hard Constraint from the grounding specification.

## 🟡 CP-PRJ-02 — Code quality standards
**Options:** 
- Clean, functional code with documentation
- Minimal viable code that passes all tests
- Rapid prototyping followed by refactoring
**Default:** Clean, functional code that satisfies all applicable Hard Constraints

## 🔴 HC-PRJ-04 — Scientific validity cannot be ignored
Scientific validity concerns must never be ignored if they conflict with user intent. Violating proteomics correctness produces incorrect science regardless of context.

## 🟡 CP-PRJ-03 — Error handling approach
**Options:** 
- Explicitly note potential errors but proceed with coding
- Refuse to generate code that violates known constraints
- Generate compliant alternatives when requested approach is invalid
**Default:** Refuse to generate code that violates grounding constraints and provide compliant alternative

## 🔴 HC-PRJ-05 — Default to grounding specification
When in doubt, default to: "The grounding specification must be followed. Let me explain why and provide a compliant approach."

## 🔴 HC-FDR-01 — FDR must be estimated at every inference level independently
PSM-level FDR, peptide-level FDR, and protein-level FDR are not the same quantity. A pipeline that filters at the PSM level and reports the result as protein-level FDR is incorrect.
*Why: PSM-level FDR does not account for the inference step of collapsing peptides to proteins. The FDR surface is not flat across single- and multi-peptide protein evidence.*

## 🔴 HC-FDR-02 — The target-decoy approach requires a valid decoy strategy
Decoys must be indistinguishable from targets in all properties except biological origin. Reversed sequences are acceptable; random sequences are not. Decoys must not share subsequences with targets that could generate legitimate matches.
Software must document which decoy strategy was applied. A pipeline with no documented decoy strategy has no verifiable FDR.

## 🔴 HC-FDR-03 — FDR and p-value are not the same quantity
A Benjamini–Hochberg q-value applied to peptide score distributions is not equivalent to a target-decoy FDR. They estimate different quantities under different assumptions. Software must not conflate them in output labels, documentation, or downstream propagation.

## 🔴 HC-FDR-04 — Post-hoc filtering does not retroactively correct an FDR estimate
If identifications are filtered after FDR estimation (by charge state, length, localization score, or any other criterion), the reported FDR no longer applies to the filtered set. FDR must be re-estimated on the final reported set, or filtering must precede estimation.
*⚠️ This is among the most common silent errors in proteomics pipelines.*

## 🔴 HC-FDR-05 — DIA FDR estimation must not use DDA logic directly
DIA MS2 signal is multiplexed. Porting DDA target-decoy FDR logic without accounting for peak group scoring and the DIA-specific decoy generation model produces incorrect FDR estimates. Results from different DIA engines are not directly comparable without harmonization at the scoring layer.

## 🔴 HC-FDR-06 — Match-between-runs transfers must be labeled and not treated as MS2-confirmed
MBR-transferred identifications must be flagged in output and must not be treated as equivalent to MS2-confirmed identifications in FDR accounting or quantification confidence reporting.

## 🟡 CP-FDR-01 — Protein inference grouping strategy
**Options:** razor peptide | strict parsimony | shared-peptide exclusion | probabilistic apportionment (FIDO, Percolator)
**Default:** Razor peptide. Probabilistic apportionment is theoretically superior but less interpretable.
*Required disclosure: the chosen strategy must be reported. Razor and shared-peptide exclusion produce different protein lists from the same data. This is a parameter, not a bug.*

## 🟡 CP-FDR-02 — FDR threshold
**Options:** 1% (publication standard) | 5% (exploratory, must be stated) | custom
**Default:** 1% at each inference level. Applied independently at each level — 1% PSM FDR does not guarantee 1% protein FDR.

## 🔴 HC-QUANT-01 — Identification and quantification filters must be applied in a consistent, documented order
Normalization must be applied to the same feature set used for downstream statistical testing. Any feature removed after normalization invalidates normalization assumptions unless recomputed.
*Safe order: (1) identification filtering to FDR threshold, (2) quantification feature selection, (3) normalization, (4) missing value handling, (5) statistical testing.*

## 🔴 HC-QUANT-02 — Missing values must be explicitly represented and their provenance tracked
A missing value from signal below detection is not the same as one from failed acquisition, poor peptide recovery, or a software filter. These have different statistical implications.
Software must not silently substitute 0 or minimum intensity for a missing value. Any imputation must be labeled as imputed and the method recorded.

## 🔴 HC-QUANT-03 — Intensity values reported as absolute must have a defined reference
Label-free intensities are inherently relative. Software must not report them as absolute concentrations without calibration against a reference of known amount.
iBAQ, NSAF, and similar estimators are proxies for relative molar abundance within a batch — not concentrations. Output labels must reflect this.

## 🔴 HC-QUANT-04 — Targeted quantification requires transition-level interference assessment
SRM/PRM results must include co-elution confirmation and interference assessment. Absolute quantification requires a heavy-isotope internal standard of known concentration. Relative quantification without a stable isotope standard must be labeled semi-quantitative.
Single-transition quantification is not acceptable for publication without explicit justification.

## 🔴 HC-STAT-01 — Multiple testing correction is not optional
Any analysis reporting significance across more than one feature must apply multiple testing correction. Uncorrected p-values must not appear in a final results table without a prominent disclaimer.
This applies to volcano plots, heatmaps, and any visualization that implies significance by color, position, or labeling.

## 🔴 HC-STAT-02 — Per-group sample size must be reported with every statistical result
N must accompany every p-value, fold-change, or confidence interval. A 10× fold-change means something different at N=3 vs N=30.
*⚠️ Software that reports statistics without surfacing N is producing uninterpretable output.*

## 🔴 HC-STAT-03 — Batch effects must be assessed before cross-batch inference
Data combined across acquisition batches, instruments, or laboratories must undergo batch effect assessment before any comparison spanning those batches. PCA and hierarchical clustering colored by batch are minimum diagnostics.
Corrected and uncorrected matrices must be kept distinct. Statistical testing must use the corrected matrix; the uncorrected matrix must be retained for audit.

## 🔴 HC-EFF-01 — Computational complexity must be documented at the algorithm level
Software must document time and memory complexity in terms of the relevant proteomics parameters: number of spectra, database size (proteins and peptides), number of modifications searched, number of samples.
*"Fast" and "scalable" are not documentation.*

## 🔴 HC-EFF-02 — Variable modification combinations must be bounded explicitly
Every additional variable modification multiplies the candidate peptide space. Searching 5+ variable modifications simultaneously without a combinatorial cap routinely generates search spaces of >10⁸ candidates per spectrum — a correctness error as well as an efficiency one, since scoring models are not calibrated for this density.
Software must either: (a) document the maximum number of simultaneous variable modifications and enforce it as a hard limit, or (b) implement and document a combinatorial pruning strategy (e.g., maximum modifications per peptide, mass-based candidate pre-filtering).
*Practical default: ≤3 variable modifications simultaneously. Search space size (number of candidate peptides) should appear in log output so users can detect accidental combinatorial explosions.*

## 🔴 HC-EFF-03 — Ion indexing must be used for any database search over a non-trivial dataset
Linear scan of a full fragment ion database for each spectrum is O(n×m) in spectra × database size. For any dataset exceeding a few hundred spectra against a full proteome, an indexed search strategy (spectral library index, fragment ion index as in MSFragger, or equivalent) is required.
Software using linear scan against a full proteome at scale must document this limitation and warn explicitly when estimated search time exceeds a configurable threshold.

## 🔴 HC-EFF-04 — Redundant recomputation of sample-independent operations is not acceptable
If a pipeline applies the same transformation to each sample independently (database indexing, spectrum preprocessing, retention time prediction), that transformation must be computed once and cached. Recomputing per-sample what is sample-independent wastes resources and biases the science toward well-resourced groups.

## 🔴 HC-EFF-05 — Memory usage must be bounded and documented for large-scale inputs
Software must not load entire datasets into memory if streaming or chunked processing is feasible. Any tool requiring full dataset loading must document expected memory footprint for typical dataset sizes (e.g., 1-hour DDA run, 96-sample TMT experiment).

## 🔴 HC-RPT-01 — Every result must be traceable to its software version and parameters
Any output file, database, or report must record: software name and version, key parameter settings, and input data identifier (filename, hash, or accession).
*⚠️ Results produced without version tracking are irreproducible by definition.*

## 🔴 HC-RPT-02 — Score columns must identify their source and direction
A column labeled 'score' is insufficient. Output must specify which score (Andromeda, PEP, q-value, etc.), whether higher or lower is better, and what threshold was applied.

## 🟡 CP-RPT-01 — Output file format
**Options:** PSI-HUPO standard formats (mzIdentML, mzTab) | flat TSV/CSV with documented schema | proprietary
**Default:** Flat TSV for human-readable outputs; mzTab for machine-readable exchange. Any format lacking a published schema is not a valid archival format. Format interoperability rules are covered in Section 3.

## 🔴 HC-INTER-01 — Input and output formats must have a published, versioned schema
Any format consumed or produced must have a machine-readable, versioned, publicly accessible schema. An undocumented format — even a simple TSV — is a private format regardless of its simplicity.
*Preferred: HUPO-PSI standard formats (mzML, mzIdentML, mzTab-M, mzQuantML). Where these do not cover the use case, a documented TSV with a published column schema is acceptable.*

## 🔴 HC-INTER-02 — Controlled vocabularies must be used for ontology-covered concepts
Instrument names, fragmentation methods, modification names, taxonomy identifiers, and sample attributes covered by established ontologies (PSI-MS CV, UNIMOD, NCBI Taxonomy, OBI, EFO) must use terms from those ontologies. Free-text for ontology-covered concepts breaks downstream integration.
*Worked example: 'HCD' vs 'Higher-energy C-trap Dissociation' vs 'beam-type CID' for the same fragmentation method cannot be automatically reconciled. This has cost the community enormous manual curation effort.*

## 🔴 HC-INTER-03 — Peptide and protein identifiers must reference a specific database version
UniProt accessions change. Gene symbols are not stable across species or time. Any report using these identifiers must specify the database name, version or release date, and species.
*A protein list with gene symbols and no database reference cannot be reproduced or integrated with future data.*

## 🔴 HC-INTER-04 — APIs must be documented at the function-signature level
Any software exposing programmatic interfaces must document those interfaces with typed signatures, parameter descriptions, return types, and error conditions. Undocumented APIs are private APIs regardless of public accessibility.

## 🔴 HC-TEST-01 — Each Hard Constraint in this specification must have a corresponding programmatic test
Software claiming compliance must implement runnable tests for each applicable Hard Constraint. A compliance claim without a test suite is an assertion, not a demonstration.
*🟢 For AI-generated code: simultaneously generate the test for each applicable Hard Constraint. The test must run without manual data preparation.*

## 🔴 HC-TEST-02 — FDR estimation must be validated against a dataset with known ground truth
Software implementing FDR estimation must be validated using a dataset where true positive and false positive identifications are known. Synthetic datasets or characterized reference material datasets are both acceptable; validation against an uncharacterized biological sample is not.
*Resources: ABRF iPRG multi-lab studies provide characterized spike-in datasets suitable for FDR validation. NIST SRM 1950 (human plasma) provides a biologically complex matrix with a partially characterized proteome.*

## 🔴 HC-TEST-03 — Quantification accuracy must be validated against samples with known ratios
Software implementing quantification must be validated against a spike-in experiment or synthetic dataset where expected ratios are known. Validation must report accuracy (observed vs expected ratio), dynamic range, and missing value rate in the reference set.
*Resources: UPS1/UPS2 standards spiked into complex background; ABRF iPRG 2015 dataset (LFQ spike-in, available on MassIVE); NIST SRM 1950 with characterized spike-in proteins.*

## 🔴 HC-TEST-04 — At least one end-to-end test must run without proprietary data or commercial software
A test suite requiring a commercial raw file format, a licensed database, or a proprietary tool dependency is not a community test. At least one complete end-to-end test must run using publicly available, open-format data.

## 🟡 CP-TEST-01 — Test data type
**Options:** fully synthetic (in silico) | spike-in standard in complex background | certified reference material | inter-laboratory study dataset
**Default:** Two tiers. Unit tests use fully synthetic data (fast, no download, fully reproducible). Integration tests use a published spike-in or reference material dataset. Clinical or regulatory tools require a certified reference material.
*Synthetic spectral data (e.g., PROSIT-predicted spectra for known sequences) eliminates data access barriers entirely. AI systems generating tests should default to synthetic data for unit tests.*

## 🟡 CP-TEST-02 — Ongoing QC monitoring
**Options:** none | manual spot-check | automated QC metrics per run | statistical process control with control charts
**Default:** Automated QC metrics on every run covering at minimum: identifications per injection, median mass accuracy, median RT deviation from library, and CV of replicate quantification. Metrics should be trended over time, not just reported per-run.
*Community resources: ABRF QC primer (Abbatiello et al., JBT 2024) provides a practical framework. iMonDB, MSstatsQC, and rawrr provide open-source implementations.*

## 🟡 CP-TEST-03 — AI-assisted test generation protocol
When an AI system generates proteomics code under this specification, it must follow this protocol:
1. For each function touching FDR, quantification, or statistical testing: generate a unit test with a synthetic known-correct input and assert on the output within defined numerical tolerance.
2. For each applicable Hard Constraint: generate a test that exercises the constraint, including a test that demonstrates the constraint catches the described failure mode.
3. Generate at least one regression test using a publicly available reference dataset with published expected outputs.
4. Include a test verifying the output schema matches the documented format (HC-INTER-01, HC-RPT-02).
5. For any search operation (Section 2): generate a test verifying the combinatorial bound (HC-EFF-02) is enforced and the reported candidate count is correct.
*🟢 This protocol makes the grounding specification self-reinforcing: the AI writes both the code and the means to verify the code meets the specification.*

## 🟡 CP-TEST-04 — Inter-laboratory or inter-tool comparison
**Options:** none | informal comparison to published benchmark | participation in formal proficiency study (ABRF iPRG, CPTAC)
**Default:** Informal comparison to at least one published benchmark on a shared dataset is the minimum for a tool making quantitative claims. Formal proficiency study participation is appropriate for core facility or clinical use.