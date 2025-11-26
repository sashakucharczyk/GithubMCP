# CSV Taxonomy Analysis Skill

## Overview
This skill performs two tasks: (1) inducing a taxonomy from a subsample of a CSV
dataset, and (2) classifying all rows into that taxonomy. It is useful for
building lightweight categorical structures for datasets without predefined
labels.

## Folder Contents
- `taxonomy_driver.py` – Driver instructions for Codex.
- `TAXONOMY_INDUCTOR.md` – Specification and constraints for taxonomy induction
  and classification.
- `raw_input.csv` – Example input dataset.
- `taxonomy.csv` – Induced taxonomy (generated).
- `labeled_output.csv` – Full labeled dataset (generated).

## Input Format
The input CSV must contain:
- `ID`
- `Text` or analogous free-text field (the classification target)

## Output Format

### Activity 1 – Taxonomy induction  
Produces:
- `taxonomy.csv` with 5–15 categories, each with:
  - Category ID
  - Category Name
  - Description
  - Inclusion Criteria
  - Example IDs

### Activity 2 – Full classification  
Produces:
- `labeled_output.csv` with:
  - original columns
  - `Primary Category ID`
  - `Secondary Category IDs`
  - `Classification Reasoning` (exactly one sentence)

## How to Invoke the Skill
Example one-shot invocation:

Use the instructions in taxonomy_driver.py and TAXONOMY_INDUCTOR.md
to perform Activity 1 and 2 in series.

Activity 1: write taxonomy.csv
Activity 2: classify all rows and write labeled_output.csv

## Hard Constraints
- Do not create or modify code files.
- Do not exceed 15 categories.
- Use a subsample of at most ~200 rows for induction.
- Classification reasoning must be grounded in the text and exactly one sentence.
- No summaries, PR notes, or logs; only the required output files.

## Skill Logic Summary
In Activity 1, the model reviews a subsample of rows and infers a compact set of
categories that cover the dataset. In Activity 2, the model uses those categories
to label all rows, assigning a primary category and optional secondary categories
with a one-sentence justification.

## Examples
Example category (taxonomy.csv):

C03,Billing errors,"Incorrect charges or unexpected fees.","Complaints about duplicate charges or wrong invoices.","12,45,301"

Example classification (labeled_output.csv):

ID,Text,Primary Category ID,Secondary Category IDs,Classification Reasoning
42,"The invoice charged me twice.",C03,,"The user reports a duplicate charge, matching the billing errors category."