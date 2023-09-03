# Time Complexity:   O(n)
# Memory Complexity: O(log(n))

from utilities.TreeNode import TreeNode


class Solution(object):
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        def check_sums(node: TreeNode = root, curr_sum: int = 0) -> bool:
            return node is not None and (
                (curr_sum + node.val == targetSum and not node.left and not node.right)
                or check_sums(node.left, curr_sum + node.val)
                or check_sums(node.right, curr_sum + node.val)
            )

        return check_sums()


# root = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, None, 1]
# target = 22
# root = TreeNode().arr2tree(root)
# print(root)
# print(Solution().hasPathSum(root, target))
