# Time Complexity:   O(log(n))
# Memory Complexity: O(1)

from utilities.TreeNode import TreeNode


# I actually read description wrong, this solution works for any binary tree not only search tree
# class Solution:
#     def lowestCommonAncestor(
#         self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
#     ) -> "TreeNode":
#         if root is None:
#             return None

#         # answer was below
#         l = self.lowestCommonAncestor(root.left, p, q)
#         if type(l) == type(TreeNode()):
#             return l
#         r = self.lowestCommonAncestor(root.right, p, q)
#         if type(r) == type(TreeNode()):
#             return r

#         is_here = root.val == p.val or root.val == q.val
#         is_below = r or l
#         are_both_below = r == True and l == True

#         # answer is here
#         if (is_here and is_below) or are_both_below:
#             return root
#         return True if is_here or is_below else None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        curr = root
        while curr:
            if curr.val < p.val and curr.val < q.val:
                curr = curr.right
            elif curr.val > p.val and curr.val > q.val:
                curr = curr.left
            else:
                return curr
