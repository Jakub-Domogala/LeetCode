# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List


class Solution(object):
    def removeDuplicates(self, nums: List[int]):
        if len(nums) == 0:
            return 0
        last_swapped = 0
        for i in range(len(nums)):
            if nums[i] > nums[last_swapped]:
                nums[last_swapped + 1] = nums[i]
                last_swapped += 1
        return last_swapped + 1

# print(Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
