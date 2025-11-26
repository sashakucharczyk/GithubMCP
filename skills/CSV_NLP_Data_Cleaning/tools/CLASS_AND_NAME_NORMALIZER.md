# Class + Name Normalizer (City / Company / Animal)

## Purpose

Given a CSV file with:
- an ID column
- a free-text entity name column
- a noisy classification column

1. Normalize the classification into **one of three canonical types**:
   - `City`
   - `Company`
   - `Animal`

2. Normalize the entity names so that all variants of the same underlying
   entity share a single canonical `Cleaned_Name`.

The classification and the name should inform each other. For example:
- A misspelled "Meta" with a classification that normalizes to `Company`
  should map to a company-like canonical representation (e.g. "Meta").
- A name that looks like food but is classified as a city should be treated
  as a city if that is the most plausible interpretation.

## Input

- CSV file path and column names are provided at runtime.
- Required columns:
  - `ID`
  - `Name` (or equivalent)
  - `Classification` (noisy type label)

## Output

Produce a new CSV file that:

- Preserves the original `ID` and `Name` columns.
- Adds these new columns:
  - `Cleaned_Classification` → one of: `City`, `Company`, `Animal`
  - `Cleaned_Name` → canonical, cleaned entity name

All rows must have exactly one of the three canonical class labels.

## Hard Constraints

- Do NOT create or modify any code files.
- Do NOT write any additional output files besides the specified CSV.
- Do NOT introduce new columns other than:
  - `Cleaned_Classification`
  - `Cleaned_Name`
- Do NOT use pure keyword rules (e.g., "if it contains 'Inc' then Company").
  You may notice lexical hints, but decisions must use overall meaning and
  context, not a single token.
- Do NOT output logs, summaries, PR notes, or commentary. Only write the CSV.

## Normalization Rules

### Classification

- Map all noisy labels in `Classification` down to:
  - `City`
  - `Company`
  - `Animal`
- Use general world knowledge and the entity name to resolve ambiguity.
- If the original classification is clearly wrong, prefer a corrected
  classification that matches the entity name.

### Name

- Group entries that clearly refer to the same real-world entity.
- For each group, choose a canonical `Cleaned_Name` that:
  - is correctly spelled,
  - is reasonably formatted (capitalization, spacing, etc.),
  - is appropriate for the cleaned class (City / Company / Animal).

- All rows in the same entity group must share the same `Cleaned_Name`.

## CSV Hygiene

- The final file must parse cleanly as CSV with exactly the columns:
  - `ID`
  - `Name`
  - `Cleaned_Classification`
  - `Cleaned_Name`
- If any commas appear in text fields, they must be properly quoted so they
  do NOT create extra columns during import.
