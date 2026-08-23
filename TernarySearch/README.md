# Ternary Search

This project demonstrates the **Ternary Search algorithm** for finding a target element in a sorted array.

Ternary Search divides the search range into three parts using two middle positions. Based on the target value, it continues searching in the section where the target can be located. :contentReference[oaicite:0]{index=0}

## How It Works

1. Set the initial `low` and `high` boundaries.
2. Calculate two middle positions, `m1` and `m2`.
3. Compare the target with the elements at these positions.
4. If the target is found, return its index.
5. If the target is smaller than `arr[m1]`, search the left section.
6. If the target is greater than `arr[m2]`, search the right section.
7. Otherwise, search the middle section.
8. Continue until the target is found or the search range becomes empty.

## Complexity

- **Best Case:** O(1)
- **Average Case:** O(log₃ n)
- **Worst Case:** O(log₃ n)
- **Space Complexity:** O(1)

## Main Concept

**Divide-and-Conquer Searching Algorithm**

## File

- [`ternary_search.py`](https://github.com/alinavirabyan/Algorithms/blob/main/TernarySearch/ternary_search.py) — Implementation of the Ternary Search algorithm.
