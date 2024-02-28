# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import List


class Solution(object):
    # greedy O(n)
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        left, right = 0, 0
        while right < len(nums) - 1:
            if left > right:
                return -1
            best_jump = 0
            for i in range(left, right + 1):
                best_jump = max(best_jump, i + nums[i])
            left, right, jumps = right + 1, best_jump, jumps + 1
        return jumps

    # # dynamic O(n^2)
    # def jump(self, nums):
    #     n = len(nums)
    #     jumps_done = [float("infinity")] * n
    #     jumps_done[0] = 0
    #     for i in range(n):
    #         for j in range(1, nums[i] + 1):
    #             if i + j < len(nums):
    #                 jumps_done[i + j] = min(jumps_done[i] + 1, jumps_done[i + j])
    #     print(nums)
    #     print(jumps_done)
    #     return jumps_done[-1]


# print(Solution().jump([2, 3, 1, 1, 4]))
