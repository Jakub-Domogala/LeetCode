# Time Complexity:   O(n)
# Memory Complexity: O(n)


from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last_seen = defaultdict(lambda: -inf)
        for i, e in enumerate(nums):
            if i - last_seen[e] <= k:
                return True
            last_seen[e] = i
        return False

# nums = [1,2,3,1]
# k = 3
# result = Solution().containsNearbyDuplicate(nums, k)
# print(result)
# nums = [1,0,1,1]
# k = 1
# result = Solution().containsNearbyDuplicate(nums, k)
# print(result)
# nums = [1,2,3,1,2,3]
# k = 2
# result = Solution().containsNearbyDuplicate(nums, k)
# print(result)
