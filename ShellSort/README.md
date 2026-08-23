# Shell Sort

This project demonstrates the **Shell Sort algorithm** for sorting elements in an array.

Shell Sort is an optimization of Insertion Sort that compares elements that are far apart using a decreasing **gap**. As the gap becomes smaller, the algorithm gradually sorts the array until the gap reaches 1.

## How It Works

1. Start with an initial gap, usually half the array length.
2. Compare and sort elements that are separated by the gap.
3. Reduce the gap by half.
4. Repeat the process until the gap becomes 1.
5. The final pass works similarly to Insertion Sort and produces the sorted array.

## Complexity

* **Best Case:** O(n log n)
* **Average Case:** Depends on the gap sequence
* **Worst Case:** O(n²)
* **Space Complexity:** O(1)

## Main Concept

**Comparison-based Sorting Algorithm**

## File

* [`shell_sort.py`](https://github.com/alinavirabyan/Algorithms/blob/main/ShellSort/shell_sort.py) — Implementation of the Shell Sort algorithm.
