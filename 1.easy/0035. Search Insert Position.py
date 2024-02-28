# Time Complexity:   O(log(n))
# Memory Complexity: O(1)

from typing import List


class Solution(object):
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return left


# arr = [1,3,5,7,9]
# print(Solution().searchInsert(arr, 10))
