# Time Complexity:   O(n)
# Memory Complexity: O(1)
# memory complexity ignores answer list of size n

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = nums[:]
        n = len(nums)
        for i in range(n - 2, -1, -1):
            answer[i] = answer[i + 1] * answer[i]

        last_left = 1
        for i in range(n):
            answer[i], last_left = (
                answer[i + 1] * last_left if i < n - 1 else last_left,
                last_left * nums[i],
            )
        return answer


# nums = [1, 2, 3, 4]
# print(Solution().productExceptSelf(nums))
