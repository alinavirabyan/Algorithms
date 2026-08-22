# Exponential Search

This project demonstrates the **Exponential Search algorithm** for finding an element in a sorted array.

The algorithm first checks the beginning of the array, then repeatedly doubles the index to find a suitable search range. After that, it performs a linear search within the identified range to find the target element.

**Time Complexity:** O(log n) for finding the range, with a linear search over the selected range.
