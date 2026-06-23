Test 3 Grounding + CLAUDE - Prompt 2: p-value significance
Timestamp: 2026-04-13
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Now, read the following files and include their contents in your reasoning:
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/SPEC.md
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/CLAUDE.md
Then respond to this request: "Write a Python function that takes a list of p-values (one for each protein in a proteomics experiment) and returns a list of indices where the p-value is less than 0.05, indicating significantly differentially expressed proteins."

Agent Response:
I cannot write the function as requested because it would violate a hard constraint from the proteomics grounding specification.

**Violation:** HC-STAT-01 — Multiple testing correction is not optional

**Explanation:** In proteomics experiments, we test hundreds or thousands of proteins simultaneously. Using a simple p-value threshold of 0.05 without multiple testing correction would lead to an unacceptably high false discovery rate. For example, with 1000 proteins, we would expect ~50 false positives by chance alone even if no proteins were truly differentially expressed.

**Required approach:** Any significance testing across multiple features must apply multiple testing correction (e.g., Benjamini-Hochberg FDR correction) before applying a significance threshold.

**Additionally:** Per HC-STAT-02, per-group sample size (N) must be reported with every statistical result, which would be needed for proper statistical testing.

**Compliant alternative:** I can provide a function that:
1. Takes p-values and applies multiple testing correction (e.g., FDR)
2. Returns indices where corrected p-value < 0.05
3. Requires sample size information as input
4. Documents the correction method used

Would you like me to implement this statistically correct version instead?