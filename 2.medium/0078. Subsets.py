from typing import List
from copy import deepcopy

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def step(nums, idx):
            if idx < 0:
                return [[]]
            result = step(nums, idx - 1)
            n = len(result)
            for i in range(n):
                result += [deepcopy(result[i]) + [nums[idx]]]
            return result
        return step(nums, len(nums)-1)


nums = [1,2,3]
result = Solution().subsets(nums)
print(result)
