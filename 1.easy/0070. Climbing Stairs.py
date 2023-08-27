# Time Complexity:   O(n) with cache
# Memory Complexity: O(n) with cache

from functools import cache


class Solution(object):
    @cache
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)


print(Solution().climbStairs(5))