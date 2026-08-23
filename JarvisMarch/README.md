# Jarvis March

This project demonstrates the **Jarvis March algorithm**, also known as the **Gift Wrapping algorithm**, for finding the convex hull of a set of points.

The algorithm starts from the leftmost point and repeatedly selects the point that makes the most counterclockwise turn. It continues until it returns to the starting point, forming the convex hull.

## How It Works

1. Find the leftmost point.
2. Select the next point that forms the most counterclockwise turn.
3. Add the selected point to the convex hull.
4. Repeat until the algorithm returns to the starting point.

## Complexity

* **Best Case:** O(n)
* **Worst Case:** O(n²)
* **Space Complexity:** O(h), where `h` is the number of points on the convex hull.

## Main Concept

**Computational Geometry — Convex Hull**

## File

* [`jarvis_march.py`](https://github.com/alinavirabyan/Algorithms/blob/main/JarvisMarch/jarvis_march.py) — Implementation of the Jarvis March algorithm.
