# Longest Palindromic Substring

This project demonstrates a **Brute-Force algorithm** for finding the longest palindromic substring in a given string.

The algorithm checks every possible substring, determines whether it is a palindrome, and keeps track of the longest palindrome found.

## How It Works

1. Generate all possible substrings of the input string.
2. Check whether each substring reads the same forward and backward.
3. Compare its length with the longest palindrome found so far.
4. Store the longest palindromic substring.
5. Print the result.

## Complexity

- **Time Complexity:** O(n³)
- **Space Complexity:** O(n)

where `n` is the length of the input string.

## Main Concept

**String Manipulation / Brute-Force Search / Palindrome Checking**

## File

- [`longest_palindromic_substring.py`](https://github.com/alinavirabyan/Algorithms/blob/main/LongestPalindromicSubstring/longest_palindromic_substring.py) — Implementation of the Longest Palindromic Substring algorithm.
