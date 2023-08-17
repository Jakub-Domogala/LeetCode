from collections import defaultdict


class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = defaultdict(int)
        back = 0
        front = 0
        longest = 0
        while front < len(s):
            letters[s[front]] += 1
            while letters[s[front]] > 1:
                letters[s[back]] -= 1
                back += 1
            longest = max(longest, front - back + 1)
            front += 1
        return longest


# print(Solution().lengthOfLongestSubstring('abcabcbb'))
