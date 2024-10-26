# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr_count = 0
        last_num = None
        last_free = 0
        for e in nums:
            if e == last_num:
                if curr_count == 2:
                    pass
                else:
                    curr_count += 1
                    nums[last_free] = e
                    last_free += 1
            else:
                last_num = e
                nums[last_free] = e
                last_free += 1
                curr_count = 1
        return last_free

# nums = [1,1,1,2,2,3]
# print(nums)
# result = Solution().removeDuplicates(nums)
# print(nums, result)
# nums = [0,0,1,1,1,1,2,3,3]
# print(nums)
# result = Solution().removeDuplicates(nums)
# print(nums, result)
