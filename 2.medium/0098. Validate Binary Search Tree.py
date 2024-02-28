# Time Complexity:   O(n)
# Memory Complexity: O(n)

from utilities.TreeNode import TreeNode


class Solution(object):
    def isValidBST(self, root):
        def isValid(root, min_val=float("-infinity"), max_val=float("infinity")):
            if not root:
                return True
            return (
                min_val < root.val < max_val
                and isValid(root.left, min_val, root.val)
                and isValid(root.right, root.val, max_val)
            )

        return isValid(root)


# tree1 = TreeNode().arr2tree([5,1,4,None,None,3,6])
# tree2 = TreeNode().arr2tree([3,1,4])
# print(Solution().isValidBST(tree1))
# print(tree1)
# print('='*70)
# print(Solution().isValidBST(tree2))
# print(tree2)
