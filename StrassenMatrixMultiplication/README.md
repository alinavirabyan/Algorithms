# Strassen Matrix Multiplication

This project demonstrates **Strassen's Matrix Multiplication algorithm** for multiplying two square matrices.

Strassen's algorithm uses a divide-and-conquer approach and reduces the number of recursive matrix multiplications from eight to seven, making it more efficient than standard matrix multiplication for sufficiently large matrices.

## How It Works

1. Divide each matrix into four smaller submatrices.
2. Calculate seven matrix products recursively.
3. Use matrix addition and subtraction to calculate the four parts of the result.
4. Combine the four parts to form the final matrix.
5. Repeat recursively until reaching 1×1 matrices.

## Complexity

- **Time Complexity:** O(n^log₂7) ≈ O(n²·⁸⁰⁷)
- **Space Complexity:** O(n²)

## Main Concept

**Divide-and-Conquer / Matrix Multiplication**

## File

- [`strassen_matrix_multiplication.py`](https://github.com/alinavirabyan/Algorithms/blob/main/StrassenMatrixMultiplication/strassen_matrix_multiplication.py) — Implementation of Strassen's Matrix Multiplication algorithm.
