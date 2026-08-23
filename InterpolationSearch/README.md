# Interpolation Search

This project demonstrates the **Interpolation Search algorithm** for finding an element in a sorted array.

Interpolation Search estimates the position of the target element based on its value. It works best when the elements in the sorted array are **uniformly distributed**.

## How It Works

1. Set the lower and upper boundaries of the search range.
2. Estimate the position of the target using its value.
3. Compare the estimated element with the target.
4. Adjust the search range based on the comparison.
5. Repeat until the target is found or the search range becomes invalid.

## Complexity

* **Best Case:** O(1)
* **Average Case:** O(log log n)
* **Worst Case:** O(n)
* **Space Complexity:** O(1)

## Main Concept

**Search Algorithm for Sorted Arrays**

## File

* [`interpolation_search.py`](https://github.com/alinavirabyan/Algorithms/blob/main/InterpolationSearch/interpolation_search.py) — Implementation of the Interpolation Search algorithm.
