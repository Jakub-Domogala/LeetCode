# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        last_free = 0
        zero_cnt = 0
        for i in range(n):
            if nums[i] == 0:
                zero_cnt += 1
            else:
                nums[last_free] = nums[i]
                last_free += 1
        for i in range(n-zero_cnt, n):
            nums[i] = 0


# nums = [0,1,0,3,12]
# Solution().moveZeroes(nums)
# print(nums)
