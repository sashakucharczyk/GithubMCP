# OpenLLMSkills  
Reusable, agent-friendly skills for LLMs operating over structured data, files, and repeatable tasks.

**Goal:**  
Enable LLMs (ChatGPT, Claude, Gemini, etc.) to act like lightweight MCP-style agents using only GitHub folder structure, well-scoped skill instructions, and driver harnesses—no servers or APIs required.

This repository defines **skills** that an LLM can execute by reading instructions directly from the repo. Each skill is fully contained in its own folder.

---

## 🔧 How the System Works

Each skill lives inside:

```
skills/<skill_name>/
    INSTRUCTIONS.md    # how the skill behaves (rules & constraints)
    <driver>.py        # the execution harness defining the workflow
```

The LLM:
1. Loads the driver.
2. Follows INSTRUCTIONS.md.
3. Consumes user-provided parameters.
4. Executes the task by reading/writing CSVs in the repo.
5. Produces *only* the output file(s) the skill defines.

This pattern lets LLMs act consistently across:
- Codex-GitHub integrations
- ChatGPT file contexts
- Claude "Tool Use" or "Skills"
- Gemini Code Execution environment

---

## 📚 Skills Available

### **1. Sentiment Analysis**
Folder: `skills/CSV_Sentiment_Analysis/`

Purpose:
- Read a CSV  
- Interpret sentiment from a text column  
- Append a sentiment label + row-specific reasoning  

User specifies:
- input file  
- output file  
- text column  
- sentiment scale (any format, e.g. 1–5 or Positive/Neutral/Negative)

---

## 🧩 Adding New Skills

To add a skill:

1. Create a folder under `skills/`
2. Add:
   - `INSTRUCTIONS.md` (rules for the LLM)
   - `<driver>.py` (execution flow)
3. Update `SKILLS_MANIFEST.md` so selection agents can find it.

A skill should:
- Define one coherent task  
- Avoid hardcoded file paths  
- Be reusable across datasets  

---

## 🔍 SKILLS_MANIFEST.md

This file serves as a lightweight directory allowing an LLM to:

- Discover available skills  
- Understand what input/output shapes they operate on  
- Determine which one(s) match the user request  

---

## ⚖ License

This project is licensed under the **Apache 2.0 License**, which:

- Allows free use and modification  
- Permits commercial use  
- Protects contributors with explicit patent grants  
- Requires attribution but prevents others from claiming exclusive rights to your work  

---

## 🤝 Contributing

Pull requests adding:
- new skills  
- better INSTRUCTIONS.md designs  
- standalone drivers  
- new reusable patterns  

…are welcome.

---

## 💬 Purpose

This repo exists to answer a simple question:

**“Can GitHub itself act as a lightweight agent runtime for general-purpose LLM workflows?”**

Turns out: yes, it can.

