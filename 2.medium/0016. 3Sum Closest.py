# Time Complexity:   O(n^2)
# Memory Complexity: O(1) if sort does not take mem if it does its O(n)

from typing import List


class Solution(object):
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best_val = float("inf")
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if abs(threeSum - target) < abs(best_val - target):
                    best_val = threeSum
                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    # result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return best_val

        # expected [[-1,-1,2],[-1,0,1]]


# print(Solution().threeSumClosest([0, 0, 0], 1))
