# 1400. Construct K Palindrome Strings

### Problem Description

Given a string `s` and an integer `k`, return `true` if you can use all the characters in `s` to construct `k` palindrome strings, or `false` otherwise.

---

### Links I Used

- [Problem on LeetCode](https://leetcode.com/problems/construct-k-palindrome-strings/description/?envType=daily-question&envId=2025-01-11)
- [YouTube Explanation](https://www.youtube.com/watch?v=D00qGvqmqN0)

---

### Thought Process

1. Count the frequency of each character in the string `s`.
2. Determine the number of odd-frequency characters because each odd-frequency character will require its own palindrome.
3. Check if the total number of odd frequencies is less than or equal to `k` and if `k` is less than or equal to the length of `s`.

For further insights, watch the [YouTube explanation](https://www.youtube.com/watch?v=D00qGvqmqN0).

---


