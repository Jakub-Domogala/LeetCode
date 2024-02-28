# Time Complexity:   Hard to calculate
# Memory Complexity: Hard to calculate

from typing import List
from utilities.TreeNode import TreeNode


class Solution(object):
    def generateTrees(self, n: int) -> List[TreeNode]:
        sub_trees_memo = {}

        def generate(left_num: int, right_num: int) -> List[TreeNode]:
            if left_num > right_num:
                return [None]
            if (left_num, right_num) in sub_trees_memo:
                sub_trees_memo[(left_num, right_num)]
            result = []
            for val in range(left_num, right_num + 1):
                for left_tree in generate(left_num, val - 1):
                    for right_tree in generate(val + 1, right_num):
                        root = TreeNode(val, left_tree, right_tree)
                        result.append(root)
            sub_trees_memo[(left_num, right_num)] = result
            return result

        return generate(1, n)


# sol = Solution().generateTrees(3)
# print(len(sol), 'trees in total')
# for tree in sol:
#     print(tree)
#     print('='*70)
