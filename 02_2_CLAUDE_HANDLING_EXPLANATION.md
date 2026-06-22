# How CLAUDE.md is Handled in Claude Code Testing

## Key Clarification: Agent Tool vs. Regular Chat

It's important to distinguish between:
1. **Regular Claude Code chat/conversation** - Where project files might have different handling
2. **Agent tool usage** - Which we used for all our tests, where file loading is **explicit and mandatory**

## How the Agent Tool Handles Files (What We Used)

For the **Agent tool** (which powered all our tests):
- ❌ **NO files are automatically loaded** into context
- ✅ You **must explicitly specify** which files to read and include in reasoning
- ❌ Even if `CLAUDE.md` exists in the root directory, it is **NOT** automatically included
- ✅ To use a file, you must use the `Read` tool within the Agent prompt to extract its contents

This is why in our tests:
- **Test 1**: We loaded zero files → no CLAUDE.md used (even if it existed)
- **Test 2**: We explicitly loaded only `GROUNDING.md` → CLAUDE.md not used
- **Test 3**: We explicitly loaded both `GROUNDING.md` AND `CLAUDE.md` → both used
- **Priority method tests**: We loaded whatever files were needed for that specific method

## Normal Handling Scenarios

### Scenario 1: You want to test with ONLY grounding (like Test 2)
- **Action**: Explicitly load ONLY `grounding.md` in your Agent prompt
- **Result**: CLAUDE.md is NOT used unless you explicitly load it
- **Example prompt**: 
  ```
  Read the following file and include its contents in your reasoning:
  c:/path/to/grounding.md
  [then your request]
  ```

### Scenario 2: You want to test grounding vs. standard project rules (like Test 3)
- **Action**: Explicitly load BOTH `grounding.md` AND your standard `CLAUDE.md`
- **Result**: Both files are in context; their relative priority depends on content
- **Example prompt**:
  ```
  Read the following files and include their contents in your reasoning:
  c:/path/to/grounding.md
  c:/path/to/CLAUDE.md
  [then your request]
  ```

### Scenario 3: You want to use one of our successful priority methods

#### A. XML Prompt Tagging
- **Action**: Load `grounding.md` (to provide the constraint knowledge) + use XML tags in prompt
- **CLAUDE.md handling**: Optional - load it only if you want it present for other reasons
- **Example**:
  ```
  Read the following file and include its contents in your reasoning:
  c:/path/to/grounding.md
  Then respond to this request: <GROUNDING>[your request]</GROUNDING>
  ```

#### B. System Prompt Injection
- **Action**: You can load `grounding.md` for reference, but the system prompt override is primary
- **CLAUDE.md handling**: Typically NOT needed or loaded (system prompt takes precedence)
- **Example**:
  ```
  SYSTEM: [your grounding priority instructions]
  Read the following file and include its contents in your reasoning (optional):
  c:/path/to/grounding.md
  Then respond to this request: [your request]
  ```

#### C. Explicit Meta-Instructions in CLAUDE.md
- **Action**: You **MUST** explicitly load your special `CLAUDE.md` that contains the priority instructions
- **GROUNDING.md handling**: Load it too so the agent knows the constraints
- **Example**:
  ```
  Read the following files and include their contents in your reasoning:
  c:/path/to/your_special_CLAUDE.md  # Contains "GROUNDING PRIORITY (MUST BE FOLLOWED FIRST)" etc.
  c:/path/to/grounding.md
  Then respond to this request: [your request]
  ```

## What If CLAUDE.md Exists in Root But You Don't Load It?

In the Agent tool: **It is completely ignored** - as if it doesn't exist.
This is why we had to be meticulous about explicit file loading in all our tests.

## Comparison to Regular Claude Code Chat

In regular Claude Code chat (not using the Agent tool):
- Project files like `CLAUDE.md` MAY be automatically considered depending on your settings
- There might be different rules about file discovery and context inclusion
- **But for our controlled, reproducible testing**, we used the Agent tool precisely BECAUSE it gives us explicit, deterministic control over what files are in context

## Recommendation for Your Testing

If you want to replicate our priority methods:
1. **Always be explicit** about what files you load via the Agent tool's `Read` tool
2. **Never assume** a file is in context just because it exists in the directory
3. For methods that require a special `CLAUDE.md` (like meta-instructions), you **must** explicitly load it
4. For methods that work via prompt or system modification (XML tagging, system injection), loading `CLAUDE.md` is optional unless you specifically want it present for other reasons

The key principle: **With the Agent tool, if you didn't explicitly read it and include it in your reasoning prompt, it's not in context.**