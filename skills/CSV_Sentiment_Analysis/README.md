# 📘 **Sentiment Analysis Skill**

This skill performs contextual sentiment analysis on text stored in a CSV file.
It assigns one sentiment label per row and provides a short, text-grounded reasoning.

This skill uses **INSTRUCTIONS.md** for its behavioral rules and
**sentiment_driver.py** as its execution harness.

---

## 🔧 **What This Skill Does**

Given:

* an input CSV
* a target text column
* a user-defined sentiment scale (e.g., `"1–5"`, `"positive/negative"`, `"low/med/high"`)
* an output CSV path

The skill:

1. Reads each row of the input file.
2. Interprets the text in the target column using contextual understanding.
3. Assigns exactly *one* sentiment label from the provided scale.
4. Writes a brief (1–2 sentence) reasoning referencing the specific row.
5. Produces a new CSV that preserves the original columns and appends:

   * `Sentiment`
   * `Reasoning`

All rule-level constraints for how the LLM must behave are defined in `INSTRUCTIONS.md`.

---

## 📂 **Files in This Folder**

```
CSV_Sentiment_Analysis/
│
├── INSTRUCTIONS.md              # Skill rules, constraints, and allowed behavior
├── /tools/sentiment_driver.py   # The execution harness for running the skill
└── README.md                    # (this file)
```

No code execution happens inside this folder; the driver file only describes
the workflow that the LLM must follow.

---

## 🧠 **How an LLM Should Use This Skill**

When an LLM is instructed to perform sentiment analysis:

1. Load and read **sentiment_driver.py**
2. Read **INSTRUCTIONS.md**
3. Wait for the user to supply:

   * `input_csv`
   * `output_csv`
   * `text_column`
   * `sentiment_labels`
4. Follow the driver exactly and produce the output CSV.
5. Output **only** the CSV — no summaries, logs, tests, or commentary.

---

## 🧪 **Example Usage (LLM Prompt)**

```
Use the skill in `skills/CSV_Sentiment_Analysis/`.

input_csv: data/raw_reviews.csv
output_csv: data/annotated_reviews.csv
text_column: Review
sentiment_labels: ["1","2","3","4","5"]

Follow the rules in INSTRUCTIONS.md and sentiment_driver.py.
Only output the annotated CSV.
```
