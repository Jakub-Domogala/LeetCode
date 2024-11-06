# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import List
from math import inf

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        def sbits(n):
            return bin(n).count("1")

        cmin = nums[0]
        cmax = nums[0]
        pmax = -inf
        for e in nums:
            if sbits(e) == sbits(cmin):
                cmin = min(cmin, e)
                cmax = max(cmax, e)
            else:
                if cmin < pmax:
                    return False
                pmax = cmax
                cmin = e
                cmax = e
        return cmin >= pmax


# nums = [8,4,2,30,15]
# print(Solution().canSortArray(nums), True)
# nums = [6,8,4,2,30,15]
# print(Solution().canSortArray(nums), False)
