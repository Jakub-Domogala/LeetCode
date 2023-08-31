# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List


class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for i in range(len(nums)):
            nums_map[nums[i]] = i
        for i, num in enumerate(nums):
            if target - num in nums_map and i != nums_map[target - num]:
                return [i, nums_map[target - num]]


# print(Solution().twoSum([2,7,11,15], 9))
