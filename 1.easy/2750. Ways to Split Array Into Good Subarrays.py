# Time Complexity:   O(n)
# Memory Complexity: O(n)


from typing import List

class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        options = [1]
        last = None
        cnt = 0
        for i in nums:
            if i == 0:
                options[-1] += 1
            else:
                cnt += 1
                options.append(1)
        options = options[1:cnt]
        def multi(A, i=0):
            if i == len(A):
                return 1
            return (A[i] * multi(A,i+1))%(10**9+7)
        if len(options) == 0:
            return 1 if cnt > 0 else 0
        return multi(options)

# nums = [0,1,0,0,1]
# result = Solution().numberOfGoodSubarraySplits(nums)
# print(result, 3)
# nums = [1,0,0,1]
# result = Solution().numberOfGoodSubarraySplits(nums)
# print(result, 3)
# nums = [1,0,0,1,0,0]
# result = Solution().numberOfGoodSubarraySplits(nums)
# print(result, 3)
# nums = [0,1,0]
# result = Solution().numberOfGoodSubarraySplits(nums)
# print(result, 0)
