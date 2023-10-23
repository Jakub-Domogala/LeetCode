# Time Complexity:   O(n)
# Memory Complexity: O(log(n))

from utilities.TreeNode import TreeNode


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        if root is None:
            return None

        # answer was below
        l = self.lowestCommonAncestor(root.left, p, q)
        if type(l) == type(TreeNode()):
            return l
        r = self.lowestCommonAncestor(root.right, p, q)
        if type(r) == type(TreeNode()):
            return r

        is_here = root.val == p.val or root.val == q.val
        is_below = r or l
        are_both_below = r == True and l == True

        if (is_here and is_below) or are_both_below:
            return root
        return True if is_here or is_below else None


# arr = [3, 1, 2, 8, 4, 9, 10, 12]
# tree = TreeNode().arr2tree(arr)
# print(tree)
# node1 = tree.left
# node10 = tree.right.right
# node9 = tree.right.left
# print(Solution().lowestCommonAncestor(tree, node9, node10))
