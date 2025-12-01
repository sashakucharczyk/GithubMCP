# **OpenLLMSkills**

A lightweight framework for building **LLM-driven tools** using nothing more than **GitHub + any coding agent** (e.g., OpenAI Codex Web). No backend, no server, no APIs—just structured instructions, CSV data, and a consistent tool layout. Gemini (non-coding agent) is able to directly use the repository by directly referencing it in a prompt; however, it may be delayed in be able to access/use any recent changes.

OpenLLMSkills lets you define reusable “skills” for LLMs in a way that mirrors the functionality of agent frameworks (MCP servers, Claude Skills, LangChain tools) without requiring any developer infrastructure.

---

## **Why this repo exists**

Modern LLM “agent” systems require:

* APIs
* servers
* persistent vector stores
* Python backends
* orchestration layers

Most people don’t have time (or interest) to set up all that machinery just to run a repeatable text-processing workflow.

**OpenLLMSkills provides a simpler alternative:**

> *Write deterministic, instruction-based “skills” that LLMs can follow directly within a GitHub repo.*

This enables tasks like:

* taxonomy induction and dataset labeling
* sentiment analysis and annotation
* data normalization and cleaning
* classification and light NLP operations
* CSV → CSV transformations with transparent logic

Using nothing more than:

* a GitHub repository
* well-structured instructions
* an LLM that can access and/or interact with GitHub

---

## **How OpenLLMSkills works**

Each skill is implemented as a **folder** with:

1. **A driver file**
   Explains the workflow, constraints, and how the LLM must behave.
   This file is located in the ./tools/ folder
   Example:
   `sentiment_driver.py`
   `taxonomy_driver.py`

2. **An instruction spec**
   Defines strict behavioral rules for the LLM, covering:

   * what files it can read/write
   * what it must NOT do
   * how to structure output
   * how to avoid heuristics or unwanted coding
   * name the file `instructions.md` (generalized naming)
     

3. **Input data example**
   Usually a CSV.
   Example:
   `raw_input.csv`

4. **Output targets**
   The files the LLM is allowed to create.
   Example:
   `labeled_output.csv`
   `simple_output.csv`

5. **Skill discovery via SKILLS_MANIFEST.md**  
   Agents can examine `SKILLS_MANIFEST.md` to determine which skill(s) apply to
   a user’s request when the user has not specified a skill directly.

6. **LLM-friendly architecture**  
   All tasks use standard paths, simple file structures, and CSV IO so that
   agents can reliably operate without ambiguous or brittle instructions.

This creates a “micro-skill” the LLM can run deterministically.

---

## **Current Skills Included**

Please see the **SKILLS_MANIFEST.md** file for a complete list of available skills, including a description, and the inputs/outputs expected for each. The file is YAML-like with the following format:

skills:
  - id: <id>
    name: <skill_name>
    path: <skills/skill_name>
    description: "Description of skills"
    inputs:
      - column: <column_name>
        description: "column description"
    outputs:
      - file: <output_name>
        description: "Output description"

---

## **Using OpenLLMSkills - Human Usage**

### **Github Integrated Agent/Worker **

The recommended workflow:

1. **Create a branch**
   Each run should happen in its own branch, so the main branch remains clean.

2. **Populate the folder** with your input data
   Example:
   `CSV_Taxonomy_Analysis/raw_input.csv`

3. **Invoke Codex (or another coding LLM)**
   Provide a short instruction like:

   > “Use the instructions in `taxonomy_driver.py` and `TAXONOMY_INDUCTOR.md` to induce a taxonomy and classify the dataset…”

4. **Codex writes the outputs**
   It follows the constraints and outputs only what it’s allowed to write.

5. **Review, tweak, repeat**
   Each skill is designed to be:

   * deterministic
   * reproducible
   * CI-friendly
   * diff-clean

### ** Gemini Web-App**
Warning: Gemini can handle large inputs and create large outputs, but it can start having issues providing outputs larger than 500 rows. You may need to ask for the output in batches.

1. **Instruct Gemini to use the Repo**
In your prompt to Gemini reference the Repo.

2. **Upload Your Input Files**
Upload the required input file(s) (e.g., your taxonomy CSV) directly to the Gemini Web App chat interface and clearly state what each file represents.

3. **Prompt Gemini**
Provide the prompt to Gemini. Each skill should have a prompt you can copy; however, it is ideally structured so that you can just give a description of what you want. Each skill should have a prompt that provides some guardrails, but it is suggested to provide guardrails in your prompt.

4. **Review, tweak, repeat**
The output is provided in Gemini Web-App. You will probably need to export it to Google Sheets to effectively review it

---

## **Contributing New Skills**

To add a new skill:

1. Create a new folder
   Example:
   `CSV_Entity_Extraction/`

2. Inside it, create:

   * ./tools/`skill_driver.py` (driver & meta-instructions)
   * `instructions.md` (strict behavior rules)
   * sample input data
   * output placeholders (optional)

3. Follow the structure of existing skills

4. Open a PR with:

   * description of the skill
   * instructions on how to invoke it
   * an example Codex invocation message

We welcome:

* classification tools
* annotation tools
* data cleaning tools
* entity extraction tools
* summarization workflows
* LLM-powered CSV→CSV transformations

---

## **Project Philosophy**

* No APIs
* No infrastructure
* No backend
* No containers
* No agents

Just **pure repo-driven tool definitions** that any coding LLM can follow.

The goal:
Make advanced LLM workflows accessible to people who don’t have the time or resources to build agent frameworks.

---

## How an Agent/LLM Should Use This Repo
All LLMs interacting with this repo must obey the following protocol:

### 1. Select a skill
**Skill Selection:** If the user specifies a skill directly, use that.
Otherwise, read `SKILLS_MANIFEST.md` and choose the closest match.

**Instruction Source of Truth:** You MUST read and strictly adhere to the constraints defined in the instructions.md file located in the target skill folder (main/skills/<skill_name>/instructions.md).

**Validation First:** The first step of any execution MUST be to load the input data and perform validation using the Pydantic schema defined in the driver file (e.g., taxonomy_driver.py). Halt execution immediately if validation fails.

**No External Access:** You are strictly forbidden from making any calls to external APIs, web scrapers, or heuristic tools. All logic must rely only on the provided input files and the natural language descriptions of the tools.

### 2. File and Tool Handling
**Strict File Access:** You are only permitted to read the input file(s) and write the output file(s) specifically named and detailed in the skill's instructions.md specification. Do not create, modify, or delete any other files in the repository.

**Tool Simulation:** You are a simulation agent. When the instruction spec references a tool (e.g., in tools/name_normalization_tool.md), you must mentally execute the described processing logic and apply the deterministic outcome to the data. Do not use external libraries for these steps unless explicitly defined in the driver file.

### 3. Output Constraints and Error Protocol
**Output Batch Limit:**

   **For Non-Coding (Web) Agents (e.g., Gemini Web-App):** To ensure stability and avoid context overflow, you MUST NOT produce an output file or single text response exceeding 750 rows or approximately 20,000 characters of CSV data. If the task involves more data, you MUST implement batching logic and inform the user to continue the run for the next batch.

   **For Coding Agents (e.g., Codex Web, Command-Line Agents):** This row limit does NOT apply. You are permitted to write the full contents of the generated output file directly to the file system as required by the instructions.md specification.

**Error Reporting:** If a task fails (e.g., Pydantic validation failure, required file missing, or logic error), your response MUST contain these three elements:

The exact error message (e.g., the Pydantic error trace).

The file and line number where the error occurred (if a coding agent).

A clear, actionable instruction for the user on how to resolve the issue (e.g., "Please correct the 'name' column type to string in raw_input.csv").

### 4. Code Generation Standard (For Coding Agents)
**Git Integrity:** All code execution should be contained within the user's current branch. Do not commit or push changes.

**Dependency Management:** Do not propose or attempt to install any new dependencies (e.g., via pip install) unless the request explicitly includes a new dependency.

If writing a CSV, it must be valid RFC 4180 format.

---

## Example Use:

Use the CSV_Taxonomy_Analysis skill.

Input file: my_data/tickets.csv  
Output files:  
  - taxonomy.csv  
  - labeled_output.csv  

Follow:
- skills/CSV_Taxonomy_Analysis/taxonomy_driver.py
- skills/CSV_Taxonomy_Analysis/instructions.md

The LLM should:

1. Read the files
2. Induce the taxonomy
3. Classify all rows
4. Save outputs exactly to the paths above
5. Produce no extra commentary

---

## **License**

Apache-2.0 license
Feel free to adapt the tools however you’d like... just attribute the source.

---
