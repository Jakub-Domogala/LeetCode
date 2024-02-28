# Time Complexity:   O(n)
# Memory Complexity: O(n)
# Where n is amount of elements in the Tree

from utilities.TreeNode import TreeNode


class Solution(object):
    def maxDepth(self, root: TreeNode) -> int:
        def get_depth(node: TreeNode) -> int:
            if node is None:
                return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        return get_depth(root)


# q = [3,9,20,None,None,15,7]
# q = TreeNode().arr2tree(q)
# print(Solution().maxDepth(q))
