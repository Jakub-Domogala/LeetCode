# Time Complexity:   O(n)
# Memory Complexity: O(n)


from typing import Optional
from utilities.TreeNode import TreeNode

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        sums = []
        def dive(node, level = 1):
            if node is None:
                return
            if len(sums) < level:
                sums.append(node.val)
            else:
                sums[level-1] += node.val
            dive(node.left, level + 1)
            dive(node.right, level + 1)
        dive(root)
        return sums.index(max(sums)) + 1

# arr = [1,7,0,7,-8,None,None]
# tree = TreeNode().arr2tree(arr)
# print(tree)
# result = Solution().maxLevelSum(tree)
# print(result)
