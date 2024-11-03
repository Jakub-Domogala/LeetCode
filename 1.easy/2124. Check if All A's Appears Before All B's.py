# Time Complexity:   O(nlogn)
# Memory Complexity: O(n)
# easy to do O(n), O(1), but not worth to bother with max n = 100

class Solution:
    def checkString(self, s: str) -> bool:
        ss = "".join(sorted(s))
        for a, b in zip(s, ss):
            if a != b:
                return False
        return True


# s = "aaabbb"
# print(Solution().checkString(s), True)
# s = "ababbb"
# print(Solution().checkString(s), False)
