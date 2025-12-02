# SENTIMENT_ANNOTATOR Instructions (v3)

Your role in this environment is hybrid:

1. You **may write Python code** to read files, iterate rows, and write output.  
   This is allowed because the environment is code-oriented.

2. However, the **sentiment label itself must NOT be automated**.  
   It must come from your direct natural-language understanding, exactly as a human annotator would decide.

This means:
- Code is allowed for **workflow structure**.
- Code is **not** allowed for **sentiment logic**.

You must follow the rules below carefully.

---

## Task

You will perform sentiment analysis directly on the text inside the input CSV:

- Input (read-only):  
  `CSV_Sentiment_Analysis/reviews_1000_v3_no_labels.csv`

- Output (write-only):  
  `CSV_Sentiment_Analysis/test_output.csv`

### What to do for each row
1. Read the `Review` text.
2. Decide the sentiment using your own understanding:
   - **Do not** use libraries, keyword lists, lexicons, rules, scoring formulas, heuristics, statistics, or sentiment models.
   - **Do** interpret the review like a human reading it.

3. Create two new columns:
   - `Estimated Sentiment` (integer 1–9)
   - `Reasoning` (1–2 sentences grounded in actual text)

4. Preserve:
   - All original columns in the same order
   - All rows in the same order

5. Produce a **complete CSV** with:
   - One header row  
   - One data row per input row  
   - No commentary or surrounding text

---

## The Sentiment Scale

- **1** – very negative  
- **2** – leaning very negative  
- **3** – negative  
- **4** – leaning negative  
- **5** – neutral / mixed  
- **6** – leaning positive  
- **7** – positive  
- **8** – leaning very positive  
- **9** – very positive  

Your reasoning must be grounded in what was actually written.  
Do not explain based on numeric logic or sentiment theory.  
Do not reuse labels from any other file.

---

## Workflow Rules

### ✔ Allowed
- Reading CSV files
- Writing CSV files
- Python loops
- Patch creation
- File modifications required by the environment
- Any scaffolding code that does **not** automate the sentiment

### ✘ Not allowed
(These apply **only** to sentiment logic.)

- No keyword lists (“positive words”, “negative words”, etc.)
- No polarity lexicons
- No rule-based scoring
- No negation/intensifier rules
- No counting words or mapping counts to scores
- No external sentiment libraries (TextBlob, VADER, transformers, etc.)
- No Python functions that “calculate sentiment”
- No pretending to simulate another LLM internally

For each row, the sentiment must be chosen the same way a human annotator chooses it.

---

## Feasibility and completeness

You must:
- Annotate **every row** in the input, regardless of count.
- Never claim the task is too large, unfeasible, unrealistic, or time-consuming.
- Never produce a partial file.
- Never output “minimal CSVs” or placeholders.
- Never discuss capacity, memory, or limitations.

If the input has **N** rows,
the output must also have **N** rows.

---

## Output Requirements

Your final output must be:

- A valid CSV file written to  
  `CSV_Sentiment_Analysis/test_output.csv`
- With:
  - Original columns  
  - `Estimated Sentiment`  
  - `Reasoning`
- No extra explanations, no surrounding text, no summaries, no commit messages.

The environment may require additional code steps or patches.  
Those are allowed.  
But the **CSV itself** is the required artifact.

