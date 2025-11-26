## Purpose ##

## Known Issues ##
Sampling too large of a subset for the taxonomy causes Codex to crash. Unsure about other CLIs. Works well when breaking into 2 steps (taxonomy creation and then classification using a subsample of less than 200 for class creation).

Reasoning output (explaination) looks to be generic. 
No use of secondary categories - may need to force.

## Instructions ##
Use the instructions in `CSV_Taxonomy_Analysis/tools/taxonomy_driver.py` 
and `CSV_Taxonomy_Analysis/tools/TAXONOMY_INDUCTOR.md` to perform the full 
taxonomy induction and classification process.

You must:
1. Induce the taxonomy using a representative subsample of `raw_input.csv`.
2. Write the taxonomy to `CSV_Taxonomy_Analysis/taxonomy.csv`.
3. Then classify *all* rows from `CSV_Taxonomy_Analysis/raw_input.csv` using that taxonomy.
4. Write the final labeled dataset to `CSV_Taxonomy_Analysis/labeled_output.csv`.

Do NOT create or modify any code files.
Do NOT output any summaries, PR notes, test logs, or explanations.

Only produce the two files:
- `CSV_Taxonomy_Analysis/taxonomy.csv`
- `CSV_Taxonomy_Analysis/labeled_output.csv`


