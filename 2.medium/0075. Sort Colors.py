# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        first_non_0_id = 0
        last_non_2_id = n - 1

        def get_non_0(first_non_0_id):
            while first_non_0_id < n and nums[first_non_0_id] == 0:
                first_non_0_id += 1
                print(0)
            return first_non_0_id

        def get_non_2(last_non_2_id):
            while last_non_2_id >= 0 and nums[last_non_2_id] == 2:
                last_non_2_id -= 1
                print(2)
            return last_non_2_id

        def swap_nums(a, b):
            nums[a], nums[b] = nums[b], nums[a]

        first_non_0_id = get_non_0(first_non_0_id)
        last_non_2_id = get_non_2(last_non_2_id)
        i = 0
        while i < n:
            if i < first_non_0_id:
                pass
            elif i > last_non_2_id:
                return
            elif nums[i] == 0:
                swap_nums(i, first_non_0_id)
                first_non_0_id = get_non_0(first_non_0_id)
                continue
            elif nums[i] == 2:
                swap_nums(i, last_non_2_id)
                last_non_2_id = get_non_2(last_non_2_id)
                continue
            i += 1


# nums = [0, 2, 0, 2, 1, 1, 2]
# Solution().sortColors(nums)
# print(nums)
