# Time Complexity:   O(n^(k-1))
# Memory Complexity: O(n! / (k! * (n-k)!)) in worst case where all combinations give correct result

from typing import List


class Solution(object):
    def fourSum(self, nums: List[int], target: int, k: int = 4) -> List[List[int]]:
        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i] - 1:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return

            left = start
            right = len(nums) - 1
            while left < right:
                # threeSum = a + nums[left] + nums[right]
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    result.append(quad + [nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
            return result
        nums.sort()
        result = []
        quad = []
        kSum(k, 0, target)
        return result

        # expected [[-1,-1,2],[-1,0,1]]
print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
