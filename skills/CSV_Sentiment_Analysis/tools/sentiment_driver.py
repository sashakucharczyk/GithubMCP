"""
sentiment_driver.py

Driver for CSV sentiment analysis using a virtual Anthropic-style model.

This file is written as Python to keep tools happy, but the core logic is meant
to be "simulated" by an LLM/agent rather than actually executed as code.
"""

import csv
from typing import List


def read_csv_chunk(input_path: str, start: int, end: int) -> str:
    """
    Read rows [start, end) from the CSV at `input_path` and return them as a
    minimal CSV string (including header) for annotation.

    This helper is here for structure; tools may ignore the body and instead
    directly provide CSV chunks to `annotate_chunk`.
    """
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    header = reader[0]
    rows = reader[1:][start:end]
    output = [header] + rows

    # Re-encode as CSV text
    from io import StringIO

    buf = StringIO()
    writer = csv.writer(buf)
    for row in output:
        writer.writerow(row)
    return buf.getvalue()


def annotate_chunk(csv_chunk: str, min_score: int = 1, max_score: int = 10) -> str:
    """
    MODEL-ONLY FUNCTION: DO NOT EXECUTE AS REAL PYTHON.

    You are an orchestrator of a virtual Anthropic-style model called
    VIRTUAL_SENTIMENT_LLM.

    Your job inside this function is to:

      1. Read the `csv_chunk` string, which contains a header row and a subset
         of the dataset rows.
      2. For each data row:
         - Conceptually call VIRTUAL_SENTIMENT_LLM(review_text, rubric) once.
         - Receive an integer sentiment score in [min_score, max_score].
         - Receive a short, text-grounded explanation (1–2 sentences).
      3. Produce a CSV string that:
         - Preserves all original columns and their order.
         - Appends two new columns at the end:
             - "Estimated Sentiment"
             - "Reasoning"
         - Includes the header row with those appended column names.

    STRICT CONSTRAINTS:

    - You MUST NOT implement heuristic rules, keyword lists, or lexicon-based
      scoring. No "if contains 'bad' then score=2" logic.
    - You MUST NOT derive sentiment by clustering or comparing rows to each other.
      Each row should be treated as if it got its own LLM call.
    - You MAY describe orchestration in abstract or pseudo-code terms
      (e.g., "for each row, call VIRTUAL_SENTIMENT_LLM(...)"), but the actual
      sentiment decision is always delegated to that virtual model.
    - Do NOT complain about dataset size; assume that all per-row calls succeed.
    - Do NOT skip rows or use placeholders; every input row must receive a score
      and reasoning.

    Sentiment Scale:

      - The allowable range is [min_score, max_score], inclusive.
      - If the caller does not specify, assume min_score=1 and max_score=10.
      - Interpret low values as negative sentiment, high values as positive,
        and middle values as mixed/neutral, but without explicit keyword rules.

    Output:

      - Return a CSV string with the same rows in the same order as `csv_chunk`,
        but with "Estimated Sentiment" and "Reasoning" appended as columns.
      - Do not include logs, debug messages, or commentary in the returned text.
    """
    # This body will not actually run; the LLM/agent is expected to "execute"
    # the above instructions by directly emitting the annotated CSV text.
    raise NotImplementedError("annotate_chunk is intended for LLM simulation only.")


def write_full_output(
    input_path: str,
    output_path: str,
    chunk_size: int = 300,
    min_score: int = 1,
    max_score: int = 10,
) -> None:
    """
    High-level orchestration for tools that actually execute Python.

    Intended flow for a coding agent:

      1. Determine the total number of rows in `input_path`.
      2. For i in 0..N (step chunk_size):
           - Read rows [i, i+chunk_size) as a CSV chunk string.
           - Pass that string into `annotate_chunk(...)` (simulated by the model).
           - Collect the annotated CSV output.
      3. Merge all annotated chunks into a single CSV and write it to `output_path`.

    NOTE:
      - The LLM is responsible for simulating annotate_chunk and may choose to
        ignore this function body entirely, instead directly producing the final
        output CSV as if it had processed all chunks.
    """
    # This is a reference orchestration. Tools can implement or ignore it.
    with open(input_path, newline="", encoding="utf-8") as f:
        reader = list(csv.reader(f))
    header = reader[0]
    rows = reader[1:]
    total = len(rows)

    from io import StringIO

    all_output_rows: List[List[str]] = []
    for start in range(0, total, chunk_size):
        end = min(start + chunk_size, total)
        chunk_rows = [header] + rows[start:end]

        buf = StringIO()
        writer = csv.writer(buf)
        for row in chunk_rows:
            writer.writerow(row)
        chunk_csv = buf.getvalue()

        # In real execution this would call a model. Here we just document intent.
        annotated_chunk_csv = annotate_chunk(
            chunk_csv, min_score=min_score, max_score=max_score
        )
        chunk_reader = list(csv.reader(StringIO(annotated_chunk_csv)))

        # First row is header; keep only data rows when merging.
        data_rows = chunk_reader[1:]
        all_output_rows.extend(data_rows)

    # Write merged CSV (single header + all annotated rows)
    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Header: original + two new columns
        extended_header = header + ["Estimated Sentiment", "Reasoning"]
        writer.writerow(extended_header)
        for row in all_output_rows:
            writer.writerow(row)
