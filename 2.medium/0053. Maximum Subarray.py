# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = nums[0]
        best = curr
        for val in nums[1:]:
            curr = max(curr, 0)
            curr += val
            best = max(best, curr)
        return best


# print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
