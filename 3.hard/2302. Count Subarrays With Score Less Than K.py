# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l_id, r_id = 0, 0
        c_score = 0
        cnt = 0
        while r_id < len(nums):
            c_score += nums[r_id]
            r_id += 1
            while c_score * (r_id - l_id) >= k:
                c_score -= nums[l_id]
                l_id += 1
            cnt += (r_id - l_id)
        return cnt

# nums = [2,1,4,3,5]
# k = 10
# print(Solution().countSubarrays(nums, k), 6)
# nums = [1,1,1]
# k = 5
# print(Solution().countSubarrays(nums, k), 5)
