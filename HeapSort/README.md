# Heap Sort

This project demonstrates the **Heap Sort algorithm** for sorting elements in an array.

Heap Sort uses a **binary heap** data structure to organize the elements. The algorithm first builds a max heap, then repeatedly moves the largest element to the end of the array and restores the heap structure.

## How It Works

1. Build a max heap from the array.
2. Find the largest element at the root of the heap.
3. Swap the root with the last unsorted element.
4. Reduce the heap size.
5. Restore the heap property.
6. Repeat until the array is sorted.

## Complexity

* **Best Case:** O(n log n)
* **Average Case:** O(n log n)
* **Worst Case:** O(n log n)
* **Space Complexity:** O(1)

## Main Concept

**Comparison-based Sorting Algorithm — Binary Heap**

## File

* `heap_sort.py` — Implementation of the Heap Sort algorithm.
