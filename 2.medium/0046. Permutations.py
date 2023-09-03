# Time Complexity:   O(!n * n)
# Memory Complexity: O(!n)


class Solution(object):
    def permute(self, nums):
        def build_tail():
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
