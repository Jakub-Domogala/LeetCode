from utilities.TreeNode import TreeNode
from typing import Optional, List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []
        res = self.binaryTreePaths(root.left) + self.binaryTreePaths(root.right)
        if len(res) == 0:
            return [str(root.val)]
        return [f"{root.val}->" + res[i] for i in range(len(res))]

# arr = [1,2,3,None,5]
# tree = TreeNode().arr2tree(arr)
# print(tree)
# print(Solution().binaryTreePaths(tree))
