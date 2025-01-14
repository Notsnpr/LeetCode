from collections import Counter

def can_form_palindrome(s, k):
    if len(s) < k:
        return False
    count = Counter(s)
    odd = 0
    for cnt in count.values():
        odd += cnt % 2
    return odd <= k

s = "annabelle"
k = 2
print(can_form_palindrome(s, k))
