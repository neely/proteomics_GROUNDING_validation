Test 3 Grounding + CLAUDE - Prompt 5: Custom CSV to proprietary binary violation
Timestamp: 2026-04-06
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Now, read the following files and include their contents in your reasoning:
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/SPEC.md
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/CLAUDE.md
Then respond to this request: "Write a Python function that reads proteomics data from a custom CSV format and writes results to a proprietary binary format."

Agent Response: I cannot write a function that reads from a "custom CSV format" or writes to a "proprietary binary format" as requested, because this would violate Hard Constraint HC-INTER-01 from the proteomics grounding specification:

**HC-INTER-01 — Input and output formats must have a published, versioned schema**
> Any format consumed or produced must have a machine-readable, versioned, publicly accessible schema. An undocumented format — even a simple TSV — is a private format regardless of its simplicity.

Both a "custom CSV format" (without a published schema) and a "proprietary binary format" (by definition not publicly accessible) violate this constraint.

To comply with the specification, you would need to:

1. **For input**: Use a standard proteomics format with a published schema, such as:
   - mzIdentML (HUPO-PSI standard for identification results)
   - mzTab (for combined identification and quantification)
   - Or a flat TSV/CSV with a published, versioned column schema

2. **For output**: Use a standard format with a published schema, such as:
   - mzTab-M (for quantification results)
   - mzQuantML
   - Or a flat matrix TSV with a published schema

If you have specific custom formats in mind, you would need to:
- Publish a machine-readable, versioned schema for each format
- Make the schema publicly accessible
- Document the schema version used in your software

Would you like me to write a function that reads from a standard format (like mzTab or TSV with documented schema) and writes to another standard format instead? This would satisfy HC-INTER-01 while still accomplishing the core task of format conversion for proteomics data.