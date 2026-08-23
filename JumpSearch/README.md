# Jump Search

This project demonstrates the **Jump Search algorithm** for finding an element in a sorted array.

Jump Search works by jumping through the array in fixed-size blocks and then performing a linear search within the block where the target element may be located.

## How It Works

1. Calculate the jump size, usually √n.
2. Jump through the sorted array by this block size.
3. Stop when the current block may contain the target.
4. Perform a linear search within that block.
5. Return the index if the element is found.

## Complexity

* **Best Case:** O(1)
* **Average Case:** O(√n)
* **Worst Case:** O(√n)
* **Space Complexity:** O(1)

## Main Concept

**Search Algorithm for Sorted Arrays**

## File

* [`JumpSearch`](https://github.com/alinavirabyan/Algorithms/blob/main/JumpSearch) — Implementation of the Jump Search algorithm.
