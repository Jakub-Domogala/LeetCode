# Time Complexity:   O(n)
# Memory Complexity: O(n)

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)

nums = [2,2,1]
result = Solution().singleNumber(nums)
print(result)  # 1
