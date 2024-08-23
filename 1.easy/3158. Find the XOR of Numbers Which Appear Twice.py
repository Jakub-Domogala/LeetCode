# Time Complexity:   O(n)
# Memory Complexity: O(n)


from typing import List
from collections import defaultdict

class Solution:
    def duplicateNumbersXOR(self, nums: List[int]) -> int:
        counter = defaultdict(int)
        result = 0
        for num in nums:
            counter[num] += 1
            if counter[num] == 2:
                result ^= num
        return result


# nums = [1,2,1,3] # 1
# result = Solution().duplicateNumbersXOR(nums)
# print(result)
# nums = [1,2,3] # 0
# result = Solution().duplicateNumbersXOR(nums)
# print(result)
# nums = [1,2,2,1] # 3
# result = Solution().duplicateNumbersXOR(nums)
# print(result)
