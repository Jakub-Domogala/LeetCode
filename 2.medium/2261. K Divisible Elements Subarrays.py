# Time Complexity:   O(n^2)
# Memory Complexity: O(n^2)
#
# making a set of hashes of arrays instead of arrays could be a quicker solution (also O(n^2))


from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        l,r = 0,0
        n = len(nums)
        div_count = 0
        arrays = set()
        result = 0
        while r < n:
            if nums[r] % p == 0:
                div_count += 1
            r += 1
            while div_count > k:
                if nums[l] % p == 0:
                    div_count -= 1
                l += 1
            result += r - l
            for i in range(l,r):
                arrays.add(tuple(x for x in nums[i:r]))
        return len(list(arrays))

# nums = [2,3,3,2,2]
# k = 2
# p = 2
# print(Solution().countDistinct(nums, k, p))
