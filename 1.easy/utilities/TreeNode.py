from typing import Any, Type, List
from math import ceil, log2, inf

# All functions in this class relate to an unordered tree, elements inside aren't sorted in any way, it is simplest representation of tree
class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        # TODO Empty Branches Are Still Drawn
        arrs = self.tree2arr_of_arr()
        n = len(arrs)
        level = 1
        result = ""
        for i in range(n-1, -1, -1):
            result = (('\t'*(level//2) + ('-'*(level*8) + '    '*(level*2))*(2**(i)) + '\n') if i < n-1 else "") + result
            result = '\t'*(level) + ('\t\t'*level).join([str(elem if elem is not None else "") for elem in arrs[i]] ) + '\n' + result
            level *= 2
        return result

    def get_depth(self) -> int:
        return max(self.left.get_depth() if self.left else 0, self.right.get_depth() if self.right else 0) + 1
    
    def get_count(self) -> int:
        return (self.left.get_count() if self.left else 0) + (self.right.get_count() if self.right else 0) + 1
    
    def get_min(self) -> int:
        return min(self.left.get_min() if self.left else inf, self.right.get_min() if self.right else inf, self.val)
    
    def get_max(self) -> int:
        return max(self.left.get_max() if self.left else -inf, self.right.get_max() if self.right else -inf, self.val)
    
    def get_sum(self) -> int:
        return (self.left.get_sum() if self.left else 0) + (self.right.get_sum() if self.right else 0) + self.val

    def arr2tree(self, arr: List[int]) -> Type["TreeNode"]:
        n = len(arr)
        def dive_fill_tree(idx: int = 0):
            if idx > n - 1 or arr[idx] is None:
                return None
            return TreeNode(arr[idx], dive_fill_tree(2*idx + 1), dive_fill_tree(2*idx + 2))
        return dive_fill_tree()
    
    def arr_of_arr2tree(self, arr_of_arr: List[int]):
        return self.arr2tree([elem for arr in arr_of_arr for elem in arr])
        

    def tree2arr(self, cut_ending: bool = False):
        n = 2 ** self.get_depth() - 1
        arr = [None] * n
        def dive_get_tree(node: Type["TreeNode"] = self, idx: int = 0):
            if not node:
                return None
            arr[idx] = node.val
            dive_get_tree(node.left, 2*idx + 1)
            dive_get_tree(node.right, 2*idx + 2)
        dive_get_tree()
        return arr[:[i for i, x in enumerate(arr) if x][-1] + 1] if cut_ending else arr
    
    def tree2arr_of_arr(self, cut_ending: bool = False):
        lst = self.tree2arr(cut_ending)
        return [lst[int(2**(j)-1):int(2**(j+1)-1)] for j in range(ceil(log2(len(lst) + 1)))]

# arr = [-10,1,2,3,4]
# tree = TreeNode().arr2tree(arr)

# print('tree2arr\n', tree.tree2arr(True))
# print('tree2arr_of_arr\n', tree.tree2arr_of_arr(True))
# print('tree __str__\n', tree)
# print('get_depth\n', tree.get_depth())
# print('get_count\n', tree.get_count())
# print('get_sum\n', tree.get_sum())
# print('get_min\n', tree.get_min())
# print('get_max\n', tree.get_max())
        