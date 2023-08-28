from typing import Any, Type, List
from math import ceil, log2


class TreeNode(object):
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def get_depth(self):
        if self is None:
            return 0
        return max(self.left.get_depth() if self.left else 0, self.right.get_depth() if self.right else 0) + 1

    def arr2tree(self, arr: List[int]) -> Type["TreeNode"]:
        n = len(arr)
        def dive_fill_tree(idx: int = 0):
            if idx > n - 1:
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
        return arr[:next((i for i, x in reversed(list(enumerate(arr))) if x is not None), -1) + 1] if cut_ending else arr
    
    def tree2arr_of_arr(self, cut_ending: bool = False):
        lst = self.tree2arr(cut_ending)
        return [lst[int(2**(j)-1):int(2**(j+1)-1)] for j in range(ceil(log2(len(lst) + 1)))]

arr = [0,1,None,3]
tree = TreeNode().arr2tree(arr)
print(tree.left.left.val)
print(tree.get_depth())
print(tree.tree2arr(True))
s = tree.tree2arr_of_arr(False)
print()
for a in s:
    print(a)
        