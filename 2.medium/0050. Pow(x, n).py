# Time Complexity:   O(logn)
# Memory Complexity: O(1)

from math import log2, floor

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Idea behind algo: x^7 = (x^2)^2 * x^2 * x
        if n < 0:
            x = 1/x
            n = -n
        result = 1
        while n > 0:
            times = floor(log2(n))
            n -= 2**times
            new_elem = x
            for i in range(times):
                new_elem *= new_elem
            result *= new_elem
        return result

# print(Solution().myPow(2, 7))
