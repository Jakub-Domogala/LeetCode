# Time Complexity:   O(n)
# Memory Complexity: O(n)

from utilities.TreeNode import TreeNode


class Solution(object):
    def minDepth(self, root: TreeNode) -> int:
        def get_min_depth(node: TreeNode) -> int:
            if not node:
                return 0
            if not node.right and not node.left:
                return 1
            return (
                min(
                    get_min_depth(node.left) if node.left else float("infinity"),
                    get_min_depth(node.right) if node.right else float("infinity"),
                )
                + 1
            )

        return get_min_depth(root)


# tree = TreeNode().arr2tree([3,9,20,None,None,15,7])
# print(tree)
# print(Solution().minDepth(tree))
