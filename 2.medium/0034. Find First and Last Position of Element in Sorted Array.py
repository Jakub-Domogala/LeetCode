# Time Complexity:   O(log(n))
# Memory Complexity: O(1)

from typing import List


class Solution(object):
    def searchRange(self, nums: List[int], target: int) -> int:
        def binary_search_furthest(target, is_left):
            back, front= 0, len(nums)-1
            idx = -1
            while back <= front:
                pivot = (back + front) // 2
                if nums[pivot] < target:
                    back = pivot + 1
                elif nums[pivot] > target:
                    front = pivot - 1
                else:
                    idx = pivot
                    if is_left:
                        front = pivot - 1
                    else:
                        back = pivot + 1
            return idx
        back = binary_search_furthest(target, True)
        front = binary_search_furthest(target, False)
        return [back, front]


# arr = [5,7,7,8,8,10]
# print(Solution().searchRange(arr, 8))