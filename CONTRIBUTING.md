# Contributing to OpenLLMSkills

Thanks for your interest in contributing. This project builds self-contained,
LLM-executable “skills” using nothing more than GitHub and a coding-oriented
LLM (e.g., OpenAI Codex Web). The goal is to keep things lightweight,
transparent, and reproducible.

This guide explains how to add new skills, improve existing ones, or contribute
supporting materials.

---

## How This Repository Works

Each skill is a standalone folder containing:

- **A driver file**  
  (`*_driver.py`) — a strictly worded meta-instruction file that Codex reads.

- **A specification file**  
  (`*_SPEC.md`) — constraints, rules, and required behavior for the LLM.

- **Input data**  
  Usually CSV files.

- **Output target files**  
  Places where the LLM is allowed to write results.

A coding LLM uses the files in a skill folder to execute the workflow
deterministically.

---

## Adding a New Skill

Follow these steps:

1. **Create a new folder**  
   Use a descriptive name. Example:  
   `CSV_Entity_Extraction/`

2. **Include the required files:**
   - `<skill>_driver.py`  
     High-level instructions and output rules.
   - `<skill>_SPEC.md`  
     Detailed constraints, forbidden behaviors, and examples.
   - Example input data (CSV recommended)
   - Placeholder output files (optional)

3. **Test the skill using a coding LLM**  
   Ensure:
   - No unintended files are created  
   - Outputs follow the spec  
   - No code is written unless explicitly allowed  
   - Execution is deterministic

4. **Open a pull request**  
   Include:
   - What the skill does  
   - How it should be invoked  
   - A sample Codex invocation message  
   - Any edge cases the LLM must handle

---

## Updating Existing Skills

Before modifying any existing skill:

1. Check whether the change affects backwards compatibility.
2. Update both the driver and specification files if behavior changes.
3. Test the workflow end-to-end.

---

## Coding Style (For Driver Files)

Driver files must:
- Read like instructions written *to an LLM*
- Avoid Python that actually executes anything
- Define what the LLM *must* and *must not* do
- Clearly specify allowed output paths

Examples of acceptable content:
- Multi-step workflows
- File read/write restrictions
- Hard constraints (e.g., “Do NOT create new code files”)

Examples of unacceptable content:
- Executable Python logic
- Helper functions
- Anything that implies script automation

---

## Submitting PRs

PRs should:
- Modify only the necessary files
- Describe the intent and reasoning
- Include example prompts for Codex/Web
- Avoid adding heavy dependencies or actual runtime code

We accept:
- New skills  
- Improvements to existing skills  
- Better documentation  
- Additional input samples  
- Bug fixes in instruction wording  

We do *not* accept:
- Large libraries  
- Execution engines  
- Backend infrastructure  
- “Agent frameworks” that violate the repo’s purpose

---

## Code of Conduct

Be constructive. No one here is trying to build AGI out of CSV files.  
We’re just making LLM workflows less painful.

Thanks for contributing!
