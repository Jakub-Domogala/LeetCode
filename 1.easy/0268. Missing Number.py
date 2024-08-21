# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        return int(n * (n + 1) * 0.5 - sum(nums))

nums = [3,0,1]
result = Solution().missingNumber(nums)
print(result)  # 2
