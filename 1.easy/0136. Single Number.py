from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        print(2 * sum(set(nums)) - sum(nums))

nums = [2,2,1]
Solution().singleNumber(nums)
