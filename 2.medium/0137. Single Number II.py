from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return int((3 * sum(set(nums)) - sum(nums))*0.5)

nums = [2,2,3,2]
result = Solution().singleNumber(nums)
print(result)
