# Time Complexity:   O(!n * n)
# Memory Complexity: O(!n)


from typing import List


class Solution(object):
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)

        def build_tail() -> List[List[int]]:
            if len(nums) == 0:
                return [[]]
            result = []
            for i in range(len(nums)):
                if i > 0 and nums[i - 1] == nums[i]:
                    continue
                val = nums.pop(i)
                ending = build_tail()
                nums.insert(i, val)
                result += [[val] + arr for arr in ending]
            return result

        return build_tail()


# print(Solution().permuteUnique([1, 1, 2]))
