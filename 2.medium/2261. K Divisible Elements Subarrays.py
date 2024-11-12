from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        options = [1]
        cnt = 0
        for i in nums:
            if i%p == 0:
                options[-1] += 1
            else:
                cnt += 1
                options.append(1)
        print(options)
        l, r = 0, k
        result = 0
        while r < len(options):
            result += options[l] * options[r]
            l += 1
            r += 1

nums = [2,3,3,2,2]
k = 2
p = 2
print(Solution().countDistinct(nums, k, p))
