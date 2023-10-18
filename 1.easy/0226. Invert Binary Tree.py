# Time Complexity:   O(n)
# Memory Complexity: O(n)
# where n is amount of elements in tree

from utilities.TreeNode import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root is not None:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root
