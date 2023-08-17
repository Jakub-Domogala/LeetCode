from typing import List


class Solution(object):
    def threeSum(self, nums: List[int], target: int = 0) -> List[List[int]]:
        nums.sort()
        result = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                threeSum = a + nums[left] + nums[right]
                if threeSum > target:
                    right -= 1
                elif threeSum < target:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return result


        # expected [[-1,-1,2],[-1,0,1]]
print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
