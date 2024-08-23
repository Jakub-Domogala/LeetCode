# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List
from functools import reduce

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = reduce(lambda x, y: x ^ y, nums)
        return result


nums = [2,2,1]
result = Solution().singleNumber(nums)
print(result)  # 1
