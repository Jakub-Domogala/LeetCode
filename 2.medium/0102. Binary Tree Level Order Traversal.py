# Time Complexity:   O(n)
# Memory Complexity: O(n)
# where n is amount of nodes

from typing import List, Optional
from utilities.TreeNode import TreeNode


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def traverse(node, level=0):
            if not node:
                return
            if len(result) - 1 < level:
                result.append([])
            traverse(node.left, level + 1)
            traverse(node.right, level + 1)
            result[level].append(node.val)

        traverse(root)
        return result


arr = [3, 9, 20, None, None, 15, 7]
tree = TreeNode().arr2tree(arr)
print(tree)
result = Solution().levelOrder(tree)
print(result)
