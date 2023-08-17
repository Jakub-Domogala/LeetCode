# Time Complexity:   O(n)
# Memory Complexity: O(c)

from typing import List


class Solution(object):
    # O(n^2) too much for larger examples
    # def maxArea(self, height: List[int]) -> int:
    #     best = 0
    #     for i in range(len(height)):
    #         for j in range(i+1, len(height)):
    #             best = max(best, (j - i) * min(height[j], height[i]))
    #     return best

    # O(n) greedy algorithm
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
