# Time Complexity:   O(n)
# Memory Complexity: O(log(n))
# Where n = size(tree)
# size - amount of nodes in tree

from utilities.TreeNode import TreeNode


class Solution(object):
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        
        def dive(left, right) -> bool:
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return dive(left.left, right.right) and dive(left.right, right.left)
        return dive(root.left, root.right)


# q = [1,2,3]
# q = TreeNode().arr2tree(q)
# print(Solution().isSymmetric(q))
