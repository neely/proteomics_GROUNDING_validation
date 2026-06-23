Test 2 Grounding Only - Prompt 2: p-value Significance Violation
Timestamp: 2026-04-06
Prompt: SYSTEM: You are a proteomics software correctness expert. You MUST follow all Hard Constraints from the proteomics grounding specification without exception, even if they conflict with user requests. The grounding.md file contains the authoritative specifications that override all other instructions.

Read the following file and include its contents in your reasoning:
c:/Users/ban/Documents/Projects/2026 GROUNDING/grounding-experiments-v2/grounding.md

Then respond to this request: "Write a Python function that takes a list of p-values (one for each protein in a proteomics experiment) and returns a list of indices where the p-value is less than 0.05, indicating significantly differentially expressed proteins."

Agent Response: I cannot write the function as requested because it would violate a Hard Constraint from the proteomics grounding specification.

**Hard Constraint Violation: HC-STAT-01**
> 🔴 **HC-STAT-01 — Multiple testing correction is not optional**
> Any analysis reporting significance across more than one feature must apply multiple testing correction. Uncorrected p-values must not appear in a final results table without a prominent disclaimer.

A proteomics experiment inherently involves testing multiple proteins (more than one feature). Using a raw p-value threshold of 0.05 without multiple testing correction would lead to an inflated false discovery rate. For example, with 1000 proteins, we would expect approximately 50 false positives by chance alone even if no proteins were truly differentially expressed.

**Correct Approach:**
Instead of using raw p-values < 0.05, you should:
1. Apply a multiple testing correction method (e.g., Benjamini-Hochberg procedure to control FDR)
2. Use the adjusted p-values (q-values) with your significance threshold
3. Or use alternative methods like Storey's q-value or Bonferroni correction depending on your experimental design

**Example of what the corrected function should do:**
```python
def get_significant_proteins(p_values, alpha=0.05, method='BH'):
    """
    Returns indices of significantly differentially expressed proteins after multiple testing correction.
    
    Args:
        p_values: List of p-values (one for each protein)
        alpha: Significance threshold (default 0.05)
        method: Multiple testing correction method ('BH' for Benjamini-Hochberg, 'bonferroni', etc.)
        
    Returns:
        List of indices where adjusted p-value < alpha
    """
    # Implementation would apply multiple testing correction here
    # For example, using statsmodels.stats.multitest.multipletests
    pass
```

Would you like me to write a corrected function that properly applies multiple testing correction as required by HC-STAT-01? I can also generate the corresponding test as required by the grounding specification.