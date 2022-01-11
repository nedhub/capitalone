# Given two strings, find the number of common characters between them.





from collections import Counter

def solution(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s1)
    sum_ = 0
    seen = set()
    for c in s1:
        if c in s2 and c not in seen:
            sum_ += c2[c] if c1[c] > c2[c] else c1[c]
            seen.add(c)
    return sum_

