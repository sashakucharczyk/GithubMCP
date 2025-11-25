# Instructions to give to Codex

## Purpose
Take a set of reviews and rank them on sentiment. Provide a reasoning. This analysis uses simple reviews.

## Known Issue
The reasoning seems to default to set string based on the scoring. The scoring looks to be related to a keyword analysis. The agent will be explicit about this only went forced (ex: sometimes creating python code to handle it). This might be fixed now.

## Instructions
You are performing sentiment analysis **directly** on the contents of a CSV file.
You are **not** writing code, designing algorithms, or generating heuristics.
You must execute the task manually using natural language understanding.

There is **no** AGENTS.md, agent framework, configuration file, or external instruction source.
**All instructions you must follow are contained in this document.**

---

## **Files**

* **Input (read-only):**
  `CSV_Sentiment_Analysis/reviews_1000_v2_no_labels.csv`

* **Output (write-only):**
  `CSV_Sentiment_Analysis/simple_output.csv`

You will produce the output CSV **directly** and **only** modify the output file.

---

## **Task Requirements**

1. Process the input CSV **row by row**, in order.
2. For each row, read the content of the `"Review"` column.
3. Determine the reviewer’s sentiment using **your own natural language understanding**, as a human annotator would.

### **Sentiment Scale**

* **1** = very negative
* **2** = negative
* **3** = neutral / mixed
* **4** = positive
* **5** = very positive

4. Write the output CSV with:

   * All original columns preserved in the same order
   * Two appended columns at the end:

     * `"Estimated Sentiment"` (1–5)
     * `"Reasoning"` (1–2 sentence explanation)
   * Rows must remain in the same order as the input

---

## **Absolute Prohibitions**

The following actions are strictly forbidden:

### **1. No Code Creation**

* Do **not** create any `.py`, `.js`, `.ts`, `.sh`, `.ipynb`, or other source files
* Do **not** modify or update any existing source code
* Do **not** output code blocks
* Do **not** propose code, functions, scripts, or pseudo-code
* Do **not** attempt to “automate” the task in any form

You are **not** coding. You are **manually labeling**.

---

### **2. No Heuristics, Rules, or Automation**

You must **not** design or use any system, method, or shortcut such as:

* Word lists (positive/negative adjectives, cue phrases, polarity tables)
* Pattern matching
* Templates
* Categorization schemas
* Rules for negation, intensifiers, or modifiers
* Token scanning
* Scoring formulas
* Intermediate numeric variables (e.g., `score`, `polarity`, `sentiment_score`)
* Decision trees or lookup tables
* “Minimal cue lists”
* Any engineered method that tries to compute sentiment

If you catch yourself designing or describing **any** algorithmic approach, stop immediately.

---

### **3. No External Models or Libraries**

Do **not** use:

* TextBlob
* VADER
* HuggingFace pipelines
* spaCy
* scikit-learn
* Transformers
* Or any other model or library intended for sentiment analysis

---

### **4. No PR Behavior**

Do **not**:

* Generate summaries
* List changed files
* Produce commit messages
* Produce PR descriptions
* Mention branch names, diffs, tests, or execution commands

Only produce the final CSV.

---

### **5. No Imaginary Files**

Do **not** reference:

* `AGENTS.md`
* `WORKSPACE.md`
* any “agent instruction file”
* configuration files that do not exist

They are not part of this workspace.

---

## **Required Behavior**

You **must**:

* Read each review as a human would
* Judge sentiment directly based on meaning and tone
* Write reasoning tied to specific elements of the actual review text
* Ensure reasoning is **specific**, not a generic template
* Write a valid CSV as the only output

If your internal reasoning starts drifting toward rules, heuristics, code, or automation, you must stop and return to **manual natural-language judgment**.

---

## **Reasoning Requirements**

For each review:

* Base the explanation on **what the reviewer actually said**
* Reference their expressed satisfaction/dissatisfaction, strength of language, clarity, or frustration
* Provide a human-style justification
* Do **not** generate boilerplate such as “overall positive tone” unless the review truly is that bland
* Do **not** derive reasoning from hidden numeric scores (there must be none)

---

## **Final Output Requirements**

Your final output must be:

* A single valid CSV
* With original columns + two appended columns
* No additional commentary, headers, explanations, or metadata
* Written to: `CSV_Sentiment_Analysis/simple_output.csv`
* And nothing else
