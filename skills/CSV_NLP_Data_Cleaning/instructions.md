## File Purpose ##
Holdder file for new instructions

## Instructions ##
Use the instructions in
`skills/CSV_NLP_Data_Cleaning/CLASS_AND_NAME_NORMALIZER.md`
to normalize both classifications and names in:

- `skills/CSV_NLP_Data_Cleaning/test_names_1000.csv`

Assume the CSV has the columns:
- `ID`
- `Name`
- `Classification`

You must:

1. Read `skills/CSV_NLP_Data_Cleaning/test_names_1000.csv`.
2. For each row:
   - Normalize `Classification` to one of: `City`, `Company`, `Animal`
     and write it to `Cleaned_Classification`.
   - Normalize the entity name to a canonical form and write it to `Cleaned_Name`,
     ensuring that all variants of the same real entity share the same
     canonical name.
3. Write the result to:
   `skills/CSV_NLP_Data_Cleaning/clean_names_test.csv`
   with exactly these columns in this order:
   - `ID`
   - `Name`
   - `Cleaned_Classification`
   - `Cleaned_Name`

Hard rules:
- Do NOT create or modify any code files.
- Do NOT output summaries, logs, or PR notes.
- Only produce:
  `skills/CSV_NLP_Data_Cleaning/clean_names_test.csv`
