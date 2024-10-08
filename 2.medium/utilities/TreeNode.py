from typing import Any, Type, List
from math import ceil, log2, inf


# Most functions in this class relate to an unordered tree, elements inside aren't sorted in any way, it is simplest representation of binary tree
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None) -> Type["TreeNode"]:
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        # TODO Empty Branches Are Still Drawn
        arrs = self.tree2arr_of_arr()
        n = len(arrs)
        level = 1
        result = ""
        for i in range(n - 1, -1, -1):
            result = (
                (
                    "\t" * (level // 2)
                    + ("-" * (level * 8) + "    " * (level * 2)) * (2 ** (i))
                    + "\n"
                )
                if i < n - 1
                else ""
            ) + result
            result = (
                "\t" * (level)
                + ("\t\t" * level).join(
                    [str(elem if elem is not None else "") for elem in arrs[i]]
                )
                + "\n"
                + result
            )
            level *= 2
        return result

    def get_max_depth(self) -> int:
        return (
            max(
                self.left.get_max_depth() if self.left else 0,
                self.right.get_max_depth() if self.right else 0,
            )
            + 1
        )

    def get_min_depth(self) -> int:
        return (
            min(
                self.left.get_min_depth() if self.left else 0,
                self.right.get_min_depth() if self.right else 0,
            )
            + 1
        )

    def get_count(self) -> int:
        return (
            (self.left.get_count() if self.left else 0)
            + (self.right.get_count() if self.right else 0)
            + 1
        )

    def get_min_val(self) -> int:
        return min(
            self.left.get_min_val() if self.left else inf,
            self.right.get_min_val() if self.right else inf,
            self.val,
        )

    def get_max_val(self) -> int:
        return max(
            self.left.get_max_val() if self.left else -inf,
            self.right.get_max_val() if self.right else -inf,
            self.val,
        )

    def get_sum(self) -> int:
        return (
            (self.left.get_sum() if self.left else 0)
            + (self.right.get_sum() if self.right else 0)
            + self.val
        )

    def arr2tree(self, arr: List[int]) -> Type["TreeNode"]:
        n = len(arr)

        def dive_fill_tree(idx: int = 0):
            if idx > n - 1 or arr[idx] is None:
                return None
            return TreeNode(
                arr[idx], dive_fill_tree(2 * idx + 1), dive_fill_tree(2 * idx + 2)
            )

        return dive_fill_tree()

    def arr_of_arr2tree(self, arr_of_arr: List[int]) -> Type["TreeNode"]:
        return self.arr2tree([elem for arr in arr_of_arr for elem in arr])

    def tree2arr(self, cut_ending: bool = False) -> List[int]:
        n = 2 ** self.get_max_depth() - 1
        arr = [None] * n

        def dive_get_tree(node: Type["TreeNode"] = self, idx: int = 0):
            if not node:
                return None
            arr[idx] = node.val
            dive_get_tree(node.left, 2 * idx + 1)
            dive_get_tree(node.right, 2 * idx + 2)

        dive_get_tree()
        return arr[: [i for i, x in enumerate(arr) if x][-1] + 1] if cut_ending else arr

    def tree2arr_of_arr(self, cut_ending: bool = False) -> List[List[int]]:
        lst = self.tree2arr(cut_ending)
        return [
            lst[int(2 ** (j) - 1) : int(2 ** (j + 1) - 1)]
            for j in range(ceil(log2(len(lst) + 1)))
        ]

    def isSymmetric(self):
        def dive(left, right):
            if not left and not right:
                return True
            if not left or not right or left.val != right.val:
                return False
            return dive(left.left, right.right) and dive(left.right, right.left)

        return dive(self.left, self.right)

    def isValidBST(self):
        def isValid(root=self, min_val=float("-infinity"), max_val=float("infinity")):
            if not root:
                return True
            return (
                min_val < root.val < max_val
                and isValid(root.left, min_val, root.val)
                and isValid(root.right, root.val, max_val)
            )

        return isValid()

    def preorderTravelsal(self):
        result = []
        def add_branch(node, result):
            if node is None:
                return
            result += [node.val]
            add_branch(node.left, result)
            add_branch(node.right, result)
        add_branch(self, result)
        return result

# arr = [1,2,2,3,4]
# tree = TreeNode().arr2tree(arr)

# print('preorderTravelsal\n', tree.preorderTravelsal())
# print('tree2arr\n', tree.tree2arr(True))
# print('tree2arr_of_arr\n', tree.tree2arr_of_arr(True))
# print('tree __str__\n', tree)
# print('get_max_depth\n', tree.get_max_depth())
# print('get_min_depth\n', tree.get_min_depth())
# print('get_count\n', tree.get_count())
# print('get_sum\n', tree.get_sum())
# print('get_min_val\n', tree.get_min_val())
# print('get_max_val\n', tree.get_max_val())
# print('isSymmetric\n', tree.isSymmetric())
# print('isValidBST\n', tree.isValidBST())
