# Time Complexity:   O(!n * n)
# Memory Complexity: O(!n)


from typing import List


class Solution(object):
    def permute(self, nums: List[int]) -> List[List[int]]:
        def build_tail() -> List[List[int]]:
            if len(nums) == 0:
                return [[]]
            result = []
            for i in range(len(nums)):
                val = nums.pop(i)
                ending = build_tail()
                nums.insert(i, val)
                result += [[val] + arr for arr in ending]
            return result

        return build_tail()


# print(Solution().permute([1, 2, 3]))
