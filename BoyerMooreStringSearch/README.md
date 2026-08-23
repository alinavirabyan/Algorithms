# Boyer-Moore String Search

This project demonstrates the **Boyer-Moore string search algorithm** for finding a pattern within a text.

The algorithm compares the pattern with the text from **right to left** and uses a shift table to skip unnecessary comparisons after a mismatch.

## How It Works

1. Build a shift table based on the characters in the pattern.
2. Align the pattern with the text.
3. Compare the pattern and text from right to left.
4. When a mismatch occurs, use the shift table to determine how far to shift the pattern.
5. Continue until the pattern is found or the end of the text is reached.

## Complexity

* **Best Case:** O(n / m)
* **Average Case:** O(n)
* **Worst Case:** O(n × m)
* **Space Complexity:** O(m)

where `n` is the length of the text and `m` is the length of the pattern.

## Main Concept

**String Pattern Matching**

## File

* [`boyer_moore_string_search.py`](https://github.com/alinavirabyan/Algorithms/blob/main/Moore/boyer_moore_string_search.py) — Implementation of the Boyer-Moore string search algorithm.
