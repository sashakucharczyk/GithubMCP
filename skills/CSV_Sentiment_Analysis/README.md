# CSV Sentiment Analysis Skill

## Overview
This skill applies human-style sentiment assessment to each row of a CSV file.
The model reads natural language text (e.g., reviews) and assigns a sentiment
score from 1 to 5, along with a short explanation grounded in the text. It does
not use heuristics, keyword lists, or rule-based scoring.

## Folder Contents
- `sentiment_driver.py` – Driver instructions for Codex.
- `SENTIMENT_ANNOTATOR.md` – Specification and constraints.
- `reviews_1000_v2_no_labels.csv` – Example input data.
- `simple_output.csv` – Example output.

## Input Format
The input CSV must include a column named:
- `Review`

This column contains the free-text content to analyze.

## Output Format
The output CSV contains:
1. All original columns in their original order.
2. Two new appended columns:
   - `Estimated Sentiment` (integer 1–5)
   - `Reasoning` (1–2 sentence justification)

## How to Invoke the Skill
Example invocation via Codex:

Use the instructions in:

skills/CSV_Sentiment_Analysis/sentiment_driver.py
skills/CSV_Sentiment_Analysis/SENTIMENT_ANNOTATOR.md

Process:
skills/CSV_Sentiment_Analysis/reviews_1000_v2_no_labels.csv

Write results to:
skills/CSV_Sentiment_Analysis/simple_output.csv

## Hard Constraints
- No creation or modification of any code files.
- No summaries, logs, or commentary; output only the final CSV.
- No heuristic keyword lists, polarity dictionaries, or scoring algorithms.
- No intermediate numerical sentiment calculations.
- Sentiment decisions must be based on natural language understanding.

## Skill Logic Summary
The model reads each review as a human would, interprets tone and context, and
assigns a sentiment score directly without numerical scoring logic. Reasoning is
explicit and specific to each review.

## Examples
Input:

ID,Review
12,"App works sometimes, but freezes often."

Output:
D,Review,Estimated Sentiment,Reasoning
12,"App works sometimes, but freezes often.",2,
"The reviewer expresses ongoing frustration with instability despite minor functionality."