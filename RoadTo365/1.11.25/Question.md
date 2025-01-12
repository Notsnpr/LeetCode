# Check if a Parentheses String Can Be Valid

### Problem Description

A parentheses string is a non-empty string consisting only of `(` and `)`. It is valid if any of the following conditions are true:
1. It is `()`.
2. It can be written as `AB` (A concatenated with B), where A and B are valid parentheses strings.
3. It can be written as `(A)`, where A is a valid parentheses string.

You are given a parentheses string `s` and a string `locked`, both of length `n`. `locked` is a binary string consisting only of `'0'`s and `'1'`s. For each index `i` of `locked`:
- If `locked[i]` is `'1'`, you **cannot** change `s[i]`.
- If `locked[i]` is `'0'`, you **can** change `s[i]` to either `'('` or `')'`.

Return `true` if you can make `s` a valid parentheses string. Otherwise, return `false`.

---

### Links I Used

- [Problem on LeetCode](https://leetcode.com/problems/check-if-a-parentheses-string-can-be-valid/description/)
- [YouTube Explanation](https://www.youtube.com/watch?v=KMIIGDiXLhY)

---

### Example Input/Output

#### Example 1:
**Input:**
```plaintext
s = "))(()", locked = "01010"
