# Time Complexity:   O(n)
# Memory Complexity: O(1)

from collections import defaultdict


class Solution:
    def longestPalindrome(self, s: str) -> int:
        alphabet = defaultdict(int)
        for letter in s:
            alphabet[letter] += 1
        mid = False
        n = 0
        for val in alphabet.values():
            n += (val // 2) * 2
            if not mid and val % 2 == 1:
                mid = True
                n += 1
        return n
