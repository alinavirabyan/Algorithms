# Quick Sort

This project demonstrates the **Quick Sort algorithm** for sorting elements in an array.

Quick Sort selects a pivot element and divides the array into elements smaller than the pivot, elements equal to the pivot, and elements greater than the pivot. It then recursively sorts the smaller and greater parts.

## How It Works

1. Select a pivot element from the array.
2. Divide the elements into three groups: smaller than, equal to, and greater than the pivot.
3. Recursively apply Quick Sort to the smaller and greater groups.
4. Combine the sorted groups to produce the final sorted array.

## Complexity

* **Best Case:** O(n log n)
* **Average Case:** O(n log n)
* **Worst Case:** O(n²)
* **Space Complexity:** O(n)

## Main Concept

**Comparison-based Sorting Algorithm**

## File

* [`quick_sort.py`](https://github.com/alinavirabyan/Algorithms/blob/main/QuickSort/quick_sort.py) — Implementation of the Quick Sort algorithm.
