# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List


class Solution(object):
    def removeElement(self, nums: List[i], val: int) -> int:
        deleted_count = 0
        last_none_idx = None
        # delete
        for i in range(len(nums)):
            if nums[i] == val:
                if last_none_idx is None:
                    last_none_idx = i
                nums[i] = None
                deleted_count += 1
        # move
        for i in range(len(nums)):
            if last_none_idx is not None and i > last_none_idx and nums[i] is not None:
                nums[last_none_idx], nums[i] = nums[i], None
                last_none_idx += 1
        return len(nums) - deleted_count


# arr = [0,1,2,2,3,0,4,2]
# print(Solution().removeElement(arr, 2))
# print(arr)
