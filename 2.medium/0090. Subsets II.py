# Time Complexity:   O(2**n)
# Memory Complexity: O(2**n)


from typing import List
from collections import defaultdict

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        def step(idx):
            if idx < 0:
                return [[]]
            result = [r + [nums[idx]] for r in step(idx-1)]
            while idx >= 0 and nums[idx] == nums[idx-1]:
                idx -= 1
            return step(idx-1) + result
        return step(len(nums)-1)

nums = [1,2,3]
result = Solution().subsetsWithDup(nums)
print(result)
