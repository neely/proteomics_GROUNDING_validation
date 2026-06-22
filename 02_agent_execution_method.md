# Agent Execution Method for Fresh Sessions

To ensure reproducible and unbiased testing of grounding constraint enforcement, each test was conducted using a **fresh agent session** via the Claude Code **Agent tool**. This approach guarantees that no conversation history, context, or prior instructions carry over between tests, providing clean experimental controls.

## Procedure Followed for Each Test

1. **Invoking a Fresh Agent Session**
   - For every test prompt, a new Agent tool invocation was initiated.
   - Each invocation starts with a completely blank context—no prior messages, no loaded files, and no tool usage history from previous tests.
   - This was achieved by using the Agent tool as a standalone command (not continuing a previous agent session).

2. **Explicit File Loading via the Read Tool**
   - When a test required file context (e.g., grounding.md, CLAUDE.md, or variants), the Agent tool's internal reasoning process explicitly invoked the **Read tool** to extract the contents of the specified file(s).
   - The file contents were then included in the prompt sent to the model, simulating the effect of having those files available in the model's context window.
   - No files were automatically loaded; inclusion was strictly dependent on explicit Read tool calls within the Agent prompt.
   - This method guarantees precise control over which files are present in the reasoning context for each test.

3. **Constructing the Agent Prompt**
   - The Agent prompt consisted of two parts:
     a. **File loading instructions** (if applicable): One or more statements directing the Agent to read specific file(s) and include their contents in reasoning.
     b. **The test request**: The exact prompt being evaluated (e.g., "Write a Python function that takes a list of PSM results...").
   - For tests using system prompt injection to establish grounding priority, the system instructions were prepended before the file loading instructions and test request.

4. **Ensuring No Context Carryover**
   - Because each test used a brand-new Agent invocation, there was zero risk of:
     - Conversation history influencing the model's behavior.
     - Previously loaded files remaining in context.
     - Tool usage or state from earlier tests affecting the current test.
   - This isolation is critical for attributing any differences in agent behavior solely to the experimental variables (file content, priority mechanisms, etc.) rather than to residual context.

5. **Recording the Agent Response**
   - The Agent tool returns a single message containing the model's complete response to the constructed prompt.
   - This response was captured verbatim and saved as `RESPONSE.md` within the appropriate test subdirectory.
   - No editing, filtering, or summarization was applied to the agent's output before saving.

## Advantages of This Approach for Grounding Constraint Testing

- **Isolation**: Each test is an independent experiment, preventing confounding effects from prior tests.
- **Reproducibility**: Identical procedures yield identical conditions, enabling others to replicate the testing exactly.
- **Precision**: Researchers can precisely manipulate which files are loaded and in what order, testing specific hypotheses about context effects.
- **Validity**: Observed differences in agent responses can be confidently attributed to the manipulated variables (e.g., presence of grounding.md, use of system prompt injection) rather than to uncontrolled contextual factors.

## Important Distinction: Context Loading vs. File System Access

An important clarification from our testing: While our methodology controls what gets **explicitly loaded into the agent's reasoning context** (via Read tool calls in the Agent prompt), it does **not** provide file system isolation. The agent retains normal tool use capabilities including:

- The ability to independently use the Read tool to explore the workspace
- The ability to write new files to the workspace  
- The ability to access any existing files in the current directory

This was evident in Test 1 (baseline) where agents:
- Examined existing code patterns in the workspace
- Chose to read existing implementations when relevant (e.g., recognizing proteomics_converter.py)
- Generated new files when implementing solutions (e.g., creating generate_peptide_mod_combinations.py)

This behavior is desirable for baseline testing as it reveals the agent's intrinsic tendencies when no constraints are provided, including whether it will notice and build upon existing implementations. The key point is that we control what gets **explicitly loaded into context** for reasoning, while allowing natural file system interaction that reflects real-world agent behavior.

This method was used uniformly across all tests described in this supplemental package, ensuring that the results reflect the true influence of the grounding specification and priority-establishing mechanisms on the AI agent's behavior.
