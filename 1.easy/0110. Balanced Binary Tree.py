# Time Complexity:   O(n)
# Memory Complexity: O(n)

from utilities.TreeNode import TreeNode


class Solution(object):
    def isBalanced(self, root: TreeNode) -> bool:
        def get_max_depth(node: TreeNode) -> int or None:
            if node is None:
                return 0
            left, right = get_max_depth(node.left), get_max_depth(node.right)
            return None if (left is None or right is None or abs(left - right) > 1) else max(left, right) + 1
        return get_max_depth(root) is not None


# tree = TreeNode().arr2tree([1,2,3,4,5,6,None,8])
# print(tree)
# print(Solution().isBalanced(tree))