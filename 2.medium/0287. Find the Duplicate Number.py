# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums) - 1
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        finder = 0
        while True:
            slow = nums[slow]
            finder = nums[finder]
            if slow == finder:
                return slow

# nums = [1,3,4,2,2]
# result = Solution().findDuplicate(nums)
# print(result)
