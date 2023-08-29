# Time Complexity:   O(n)
# Memory Complexity: O(n)

from typing import List
from utilities.TreeNode import TreeNode


class Solution(object):
    def sortedArrayToBST(self, nums: List[int]):
        def make_tree(nums):
            if len(nums) == 0:
                return None
            mid = len(nums)//2
            return TreeNode(nums[mid], make_tree(nums[:mid]), make_tree(nums[mid+1:]))
        return make_tree(nums)

# arr = [-10,-3,0,5,9]
# print(Solution().sortedArrayToBST(arr))