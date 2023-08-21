# Time Complexity:   O(n)
# Memory Complexity: O(1)

class Solution(object):
    def nextPermutation(self, nums):
        def reverse_in_range(nums, a, b):
            while a < b:
                swap(nums, a, b)
                a += 1
                b -= 1
        def swap(nums, a, b):
            nums[a], nums[b] = nums[b], nums[a]
        first_to_swap_idx = len(nums) - 2
        # first smaller than next
        while first_to_swap_idx > -1 and \
          nums[first_to_swap_idx] >= nums[first_to_swap_idx+1]:
            first_to_swap_idx -= 1
        if first_to_swap_idx > -1:
            next_bigger_idx = len(nums) - 1
            while next_bigger_idx > -1 and \
              nums[next_bigger_idx] <= nums[first_to_swap_idx]:
                next_bigger_idx -= 1
            swap(nums, first_to_swap_idx, next_bigger_idx)
        reverse_in_range(nums, first_to_swap_idx+1, len(nums)-1)


# nums = ['a', 'e', 'd', 'c', 'b']
# print(nums)
# Solution().nextPermutation(nums)
# print(nums)
