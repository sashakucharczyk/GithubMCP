"""
Sentiment Driver — Execution Harness

This driver file defines how the LLM should perform sentiment analysis on a CSV
using the skill instructions found in INSTRUCTIONS.md.

The LLM must follow these steps exactly and must not deviate from them.

===============================================================================
1. USER-SPECIFIED PARAMETERS (supplied in the prompt calling this driver)
===============================================================================

The user must provide:
- input_csv: path to the CSV file to read
- output_csv: path to write the annotated CSV
- text_column: name of the column containing text to analyze
- sentiment_labels: ordered list of allowed sentiment labels (e.g., ["1","2","3","4","5"])

===============================================================================
2. WHAT THE LLM MUST DO
===============================================================================

1. Load the input CSV (read-only).
2. For each row:
    a. Read the text in text_column.
    b. Interpret the sentiment using contextual understanding.
    c. Assign exactly one sentiment label from sentiment_labels.
    d. Write a reasoning sentence grounded in the row’s text.
3. Create a new CSV that:
    - preserves all original columns and ordering
    - appends:
        Sentiment
        Reasoning
4. Save the CSV to output_csv (write-only).

===============================================================================
3. HARD CONSTRAINTS
===============================================================================

- Do NOT create or modify any source code files.
- Do NOT implement algorithms, keyword rules, or sentiment lexicons.
- Do NOT compute internal numeric sentiment scores.
- Do NOT summarize, describe, or explain the results outside the output CSV.
- Do NOT reorder or modify the original columns.

===============================================================================
4. ANNOTATION LOGIC
===============================================================================

The LLM must:
- treat each row independently
- base sentiment on meaning, tone, and context
- produce 1–2 sentence reasoning that references the text
- avoid boilerplate templates

===============================================================================
5. OUTPUT
===============================================================================

The final and ONLY output of this task must be the CSV written to output_csv.
No tests, no summaries, no commentary.
"""

# No executable code is required.
# This file exists solely as a driver specification for the LLM.
