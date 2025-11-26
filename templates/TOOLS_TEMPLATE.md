# ✔ **2. `TOOLS_TEMPLATE.md`**

# Skill Template for OpenLLMSkills

Use this template when adding a new skill folder.

---

## Folder Structure

```

<SKILL_NAME>/
│
├── <skill>_driver.py          # meta-instructions for Codex
├── <skill>_SPEC.md            # strict behavior rules and constraints
│
├── input_example.csv          # sample input (optional but recommended)
└── output_placeholder.csv     # placeholder to show output shape (optional)

````

---

## 1. Driver File Template (`<skill>_driver.py`)

This file should define:

- The workflow steps  
- Exactly which files the LLM may read  
- Exactly which files the LLM may write  
- Hard constraints (no code creation, no heuristics, etc.)  
- Output specs  

Example template:

```python
"""
You are performing the <SKILL NAME> skill.

Using the instructions in <skill>_SPEC.md, perform:

1. <step description>
2. <step description>
3. ...

You may read:
- <input files>

You may write ONLY:
- <output files>

Hard constraints:
- Do NOT create or modify any code files.
- Do NOT output summaries, logs, PR notes, or commentary.
- Follow all rules in <skill>_SPEC.md.
"""
````

---

## 2. Specification Template (`<skill>_SPEC.md`)

This file defines:

* Constraints
* Forbidden behaviors
* Allowed behaviors
* Requirements for final output
* Reasoning rules (if applicable)
* Format rules

Example:

# <Skill Name> Specification

## Purpose
Describe what the skill accomplishes.

## Hard Constraints
- Do NOT create code files.
- Do NOT use heuristics, keyword matching, or rule-based logic.
- Do NOT modify unrelated files.
- Do NOT output anything except the designated output CSV.

## Requirements
- Describe exactly what the LLM must do.
- Describe the format of each output column.
- Describe how to handle ambiguous or problematic cases.

## Reasoning Requirements (if needed)
- Reasoning must be grounded in the row text.
- Reasoning must reference specific details.
- Reasoning must not be reused across many rows.

## Output Format
Provide an explicit CSV schema.

## Examples
(Optional)

---

## 3. Input Data Guidelines

* Prefer CSV format
* Keep examples small (10–50 rows)
* Full datasets should be placed in branches or working folders, never `main`

---

## 4. Output Guidelines

* Output files MUST be reproducible
* No extra commentary
* No extra files created
* No logging

---

Use this template for new skills so the repo stays consistent and easy to extend.

