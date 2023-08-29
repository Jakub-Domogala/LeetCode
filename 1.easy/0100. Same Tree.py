# Time Complexity:   O(n)
# Memory Complexity: O(log(n))
# Where n = min(size(p), size(q))
# size - amount of nodes in tree

from utilities.TreeNode import TreeNode


class Solution(object):
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


# p = [1,2,3]
# q = [1,2,3]
# p = TreeNode().arr2tree(p)
# q = TreeNode().arr2tree(q)
# print(Solution().isSameTree(p, q))
