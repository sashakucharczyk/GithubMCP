# Instructions to give to Codex

## Purpose
Take a set of reviews and rank them on sentiment. Provide a reasoning. This analysis uses simple reviews.

## Known Issue
The reasoning seems to default to set string based on the scoring. The scoring looks to be related to a keyword analysis. The agent will be explicit about this only went forced (ex: sometimes creating python code to handle it). This might be fixed now.

## Instructions
You are performing sentiment analysis directly on the contents of a CSV file, *not* implementing a rule-based, heuristic-based, or keyword-based sentiment engine.

There is no AGENTS.md, agent framework, or external instruction file. All instructions you must follow are contained directly in this prompt.

**Files**

* Input (read-only): `CSV_Sentiment_Analysis/reviews_1000_v2_no_labels.csv`
* Output (write-only): `CSV_Sentiment_Analysis/simple_output.csv`

**Task**

1. Process the input CSV **row by row**, in order.
2. For each row, read the value in the `"Review"` column.
3. Infer the author’s sentiment using your general understanding of language and context, not explicit rules, algorithms, or word lists.

   * Sentiment scale:

     * 1 = very negative
     * 2 = negative
     * 3 = neutral / mixed
     * 4 = positive
     * 5 = very positive
4. Produce an output CSV that:

   * Preserves all original columns and their order.
   * Appends **two new columns at the end**:

     * `"Estimated Sentiment"` (integer 1–5)
     * `"Reasoning"` (a short explanation of why you chose that rating, 1–2 sentences max).
   * Preserves row order exactly.

**Hard constraints**

* **Do NOT create any new source code files** (no `.py`, `.js`, etc.).
* **Do NOT modify any existing source code files.**
* **Do NOT call or implement any sentiment-analysis library or model** (e.g., TextBlob, VADER, Hugging Face sentiment pipelines, custom sentiment classes).
* **Do NOT output any summary, testing notes, file lists, or commentary.** Only produce the final `simple_output.csv` content.
* **Do NOT implement or rely on any explicit sentiment or polarity lexicon.**

  * Do not define lists or sets of “positive words,” “negative words,” or similar.
  * Do not implement custom scoring rules, negation handling, or intensifier rules.
  * Do not design *any* algorithm whose main purpose is to compute sentiment from tokens or regex matches.
* **Do NOT compute intermediate numeric sentiment scores.**

  * Do not define variables such as `score`, `polarity`, `sentiment_score`, or similar to accumulate or compute sentiment.
  * Do not map numeric scores to ratings (e.g., via ranges or thresholds).
* **Do NOT use keyword-based scoring or pattern matching.**

  * Do not base sentiment primarily on the presence/absence or counts of specific tokens, stems, or regex matches.

Instead:

* For each review, read it as natural language and judge sentiment the way a human would.
* Decide the 1–5 rating directly from the meaning and tone of that specific review.
* Then write a brief natural-language reasoning that reflects *what the reviewer actually expressed*.

The final result must be a valid CSV with the original columns plus the two new columns, and nothing else.

**Reasoning Rules**

* Your reasoning for each review must be based on a **contextual interpretation** of that review (e.g., what they praised, what they complained about, whether they sound satisfied or frustrated).
* The reasoning should explain **why** you chose that specific rating in plain language, referencing aspects of the text (e.g. “mentions slow service and being disappointed, but still likes the food”).
* The reasoning must **not** be a generic template tied only to the numeric score (e.g., avoid boilerplate like “overall positive tone with minor issues” repeated across many rows).
* The reasoning must come from the review’s content, not from any hidden or explicit scoring logic.

If you find yourself defining word lists, numeric scores, or rule-based logic to determine sentiment, stop and instead directly read each review and rate it using natural language understanding.