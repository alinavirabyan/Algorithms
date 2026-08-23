# Binary Search

This project demonstrates the **Binary Search algorithm** for finding a target element in a sorted array.

Binary Search repeatedly divides the search range in half and compares the middle element with the target. Based on the comparison, it continues searching in either the left or right half.

## How It Works

1. Set the initial `low` and `high` boundaries.
2. Calculate the middle position.
3. Compare the middle element with the target.
4. If they are equal, the target is found.
5. If the target is smaller, search the left half.
6. If the target is larger, search the right half.
7. Continue until the target is found or the search range becomes empty.

## Complexity

- **Best Case:** O(1)
- **Average Case:** O(log n)
- **Worst Case:** O(log n)
- **Space Complexity:** O(1)

## Main Concept

**Divide-and-Conquer Searching Algorithm**

## File

- [`binary_search.py`](https://github.com/alinavirabyan/Algorithms/blob/main/BinarySearch/binary_search.py) — Implementation of the Binary Search algorithm.
