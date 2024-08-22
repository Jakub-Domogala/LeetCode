# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        singles = 0
        doubles = 0
        for num in nums:
            singles = (singles ^ num) & (~doubles)
            doubles = (doubles ^ num) & (~singles)
        return singles
        # return int((3 * sum(set(nums)) - sum(nums))*0.5) # Memo O(n), Time O(n)

nums = [2,2,3,2]
result = Solution().singleNumber(nums)
print(result)
