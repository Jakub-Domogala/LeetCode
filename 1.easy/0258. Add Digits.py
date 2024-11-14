# Time Complexity:   O(1)
# Memory Complexity: O(1)

# https://en.wikipedia.org/wiki/Digital_root

class Solution:
    def addDigits(self, num: int, base = 10) -> int:
        return num if num < base else 1 + (num-1) % (base-1)

# print(Solution().addDigits(38), 2)
# print(Solution().addDigits(40), 4)
# print(Solution().addDigits(41), 5)
# print(Solution().addDigits(55), 1)
