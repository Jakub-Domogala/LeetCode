# Time Complexity:   O(n)
# Memory Complexity: O(n)


from utilities.TreeNode import TreeNode
from typing import List, Optional


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dive(node: Optional[TreeNode]):
            nonlocal result
            if node is None:
                return
            else:
                result += [node.val]
                dive(node.left)
                dive(node.right)

        dive(root)
        return result


# arr = [1, 2, 3, 4]
# tree = TreeNode().arr2tree(arr)
# print(tree)
# result = Solution().preorderTraversal(tree)
# print(result)
