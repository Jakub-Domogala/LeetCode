# Time Complexity:   O((logn)**2)
# Memory Complexity: O(logn)

from utilities.TreeNode import TreeNode

class Solution:
    '''
    If you want to beat leetcode rating I recommend swapping recursion for loops, but recursion feels cleaner to use for trees
    '''
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        lh, rh = self.dive_left(root.left), self.dive_right(root.right)
        if lh == rh:
            return 2**lh - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    def dive_left(self, root: TreeNode):
        return 1 if root is None else self.dive_left(root.left) + 1
    def dive_right(self, root: TreeNode):
        return 1 if root is None else self.dive_right(root.right) + 1
    # return 0 if root is None else self.countNodes(root.left) + 1 + self.countNodes(root.right) # Time O(n), Memo O(logn)


# root = [1,2,3,4,5,6]
# tree = TreeNode().arr2tree(root)
# print(tree)
# result = Solution().countNodes(tree)
# print(result)
