# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List


class Solution(object):
    def maxArea(self, height: List[int]) -> int:
        best = 0
        left = 0
        right = len(height) - 1
        while left < right:
            best = max(best, (right - left) * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return best


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
