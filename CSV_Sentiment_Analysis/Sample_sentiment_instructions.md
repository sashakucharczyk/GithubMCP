# Instructions to give to Codex

## Purpose
Take a set of reviews and rank them on sentiment. Provide a reasoning. This analysis uses simple reviews.

## Known Issue
File has labels which might create a problem.

## Instructions
You are evaluating reviews to understand the sentiment of the person who wrote them. The sentiment can range from very negative to very position (1 to 5 scale).

Your input file is: `CSV_Sentiment_Analysis/reviews_1000_with_classification.csv`
Your output file is: `CSV_Sentiment_Analysis/simple_output.csv`

Create two new columns:
1 - Estimated Sentiment,
2 - Reasoning

Please do the following:

1 - Go line-by-line in the csv,
2 - Analyze the column 'Review'
3 - Rank the review based on sentiment on a 5 point scale. 1 being very negative and 5 being very position.
4 - Put the ranking in the 'Estimated Sentiment' column,
5 - Put the reasoning for your results in the 'Reasoning' column.
6 - Repeat until all entries in the csv are completed.

You are only to touch the output file.