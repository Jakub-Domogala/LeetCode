# Time Complexity:   O(n)
# Memory Complexity: O(n)

from typing import List
from utilities.TreeNode import TreeNode


class Solution(object):
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        def travel(node):
            if node is None:
                return []
            return travel(node.left) + [node.val] + travel(node.right)

        return travel(root)


# root = [1,None,2,None,None,3]
# root = TreeNode().arr2tree(root)
# print(root.tree2arr())
# print(root)
# print(Solution().inorderTraversal(root))
