# CSV NLP Classification Summary

## Goal:
Tools that allow NLP classification on csv (or similar) files.

## Assumptions:
Instruction files assume use of Codex Web. The Instructions will be referenced as a variable name in any prompt to the LLM.

## Examples:
1 - Take a csv and indentify all entries in a single common with a common or similar name. Provide an updated name in a new column. (ex: handle misspellings)

2 - Classify the purpose/subject matter for a specific block of text without resorting to keyword matching. Current LLMs will turn to generating keyword algorithms after a certain number of entries requiring either multiple runs or the creation of an agent environment.