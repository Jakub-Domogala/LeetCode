from typing import List

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        options = [1]
        cnt = 0
        for i in nums:
            if i%2 == 0:
                options[-1] += 1
            else:
                cnt += 1
                options.append(1)
        l, r = 0, k
        result = 0
        while r < len(options):
            result += options[l] * options[r]
            l += 1
            r += 1

        return result

nums = [2,2,2,1,2,2,1,2,2,2]
k = 2
print(Solution().numberOfSubarrays(nums, k))
