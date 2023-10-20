from typing import Optional

from utilities.TreeNode import TreeNode


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def longest_path(node):
            if node is None:
                return -1, -1
            l = longest_path(node.left)
            r = longest_path(node.right)
            return max(l[0], r[0], l[1] + 2 + r[1]), max(l[1], r[1]) + 1

        return longest_path(root)[0]


lst = [1, 2, 3, 4, 5]
tree = TreeNode().arr2tree(lst)
print(tree)
print(Solution().diameterOfBinaryTree(tree))
