# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import List
from functools import reduce
from math import log2


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        def assign_or_xor(a, b):
            return b if a is None else a ^ b
        xored = reduce(lambda x, y: x ^ y, nums)
        group_selector = 1
        while not group_selector & xored:
            group_selector *= 2
        num1, num2 = None, None
        for num in nums:
            if num & group_selector:
                num1 = assign_or_xor(num1, num)
            else:
                num2 = assign_or_xor(num2, num)
        return sorted([num1, num2])

# nums = [0,1] # [1, 0]
# result = Solution().singleNumber(nums)
# print(result)
# nums = [1,2,1,3,2,5] # [3, 5]
# result = Solution().singleNumber(nums)
# print(result)
# nums = [43772400,1674008457,1779561093,744132272,1674008457,448610617,1779561093,124075538,-1034600064,49040018,612881857,390719949,-359290212,-812493625,124732,-1361696369,49040018,-145417756,-812493625,2078552599,1568689850,865876872,865876872,-1471385435,1816352571,1793963758,2078552599,-1034600064,1475115274,-119634980,124732,661111294,-1813882010,1568689850,448610617,1347212898,-1293494866,612881857,661111294,-1361696369,1816352571,-1813882010,-359290212,1475115274,1793963758,1347212898,43772400,-1471385435,124075538,-1293494866,-119634980,390719949]
# result = Solution().singleNumber(nums) # [-145417756, 744132272]
# print(result)
