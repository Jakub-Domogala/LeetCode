# Time Complexity:   O(n)
# Memory Complexity: O(n)

from typing import List


class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        checked = {}
        for e in nums:
            if e in checked:
                return True
            checked[e] = True


# print(Solution().containsDuplicate([1, 2, 3, 3, 4]))
