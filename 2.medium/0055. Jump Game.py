from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        while i + nums[i] < len(nums) - 1:
            best = 0
            best_idx = None
            for jump in range(1, min(nums[i] + 1, len(nums))):
                if best < jump + nums[i + jump]:
                    best = jump + nums[i + jump]
                    best_idx = i + jump
            if best == 0:
                return False
            i = best_idx
        return True


# nums1 = [2, 3, 1, 1, 4]  # true
# nums2 = [1, 0, 3]  # false

# print(Solution().canJump(nums1))
# print(Solution().canJump(nums2))
