# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        result = nums[0]
        count = 0
        for val in nums:
            if val == result:
                count += 1
            elif count == 0:
                result = val
                count = 1
            else:
                count -= 1
        return result


# nums = [2, 2, 1, 1, 1, 2, 2]
# print(Solution().majorityElement(nums))
