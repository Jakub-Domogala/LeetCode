# Time Complexity:   O(n)
# Memory Complexity: O(c)

from typing import List
from math import inf


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        buy = inf
        for p in prices:
            if p < buy:
                buy = p
            best = max(best, p - buy)
        return best


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # expected 5
