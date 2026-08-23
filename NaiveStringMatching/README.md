# Naive String Matching

This project demonstrates the **Naive String Matching algorithm** for finding a pattern within a text.

The algorithm checks the pattern at every possible position in the text and compares the characters one by one until the pattern is found or a mismatch occurs.

## How It Works

1. Start from the first possible position in the text.
2. Compare the pattern with the corresponding characters in the text.
3. If all characters match, the pattern is found.
4. If a mismatch occurs, move the pattern one position forward.
5. Continue until all possible positions have been checked.

## Complexity

* **Best Case:** O(n)
* **Average Case:** O(n × m)
* **Worst Case:** O(n × m)
* **Space Complexity:** O(1)

where `n` is the length of the text and `m` is the length of the pattern.

## Main Concept

**String Pattern Matching**

## File

* [`naive_string_matching.py`](https://github.com/alinavirabyan/Algorithms/blob/main/NaiveStringMatching/naive_string_matching.py) — Implementation of the Naive String Matching algorithm.
