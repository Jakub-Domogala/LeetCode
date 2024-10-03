# Time Complexity:   O(n)
# Memory Complexity: O(n)


from typing import Optional
from utilities.TreeNode import TreeNode
from random import randint

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def randomized_select(A, p, r, i):
            if p == r:
                return A[p]
            q = randomized_partition(A, p, r)
            k = q - p + 1
            if i == k:
                return A[q]
            elif i < k:
                return randomized_select(A, p, q - 1, i)
            else:
                return randomized_select(A, q + 1, r, i - k)

        def randomized_partition(A, p, r):
            i = p if p == r else randint(p, r)

            A[r], A[i] = A[i], A[r]
            return partition(A, p, r)

        def partition(A, p, r):
            x = A[r]
            i = p - 1
            for j in range(p, r):
                if A[j] > x:
                    i += 1
                    A[i], A[j] = A[j], A[i]
            A[i+1], A[r] = A[r], A[i + 1]
            return i + 1


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
        return -1 if len(sums) < k else randomized_select(sums, 0, len(sums) - 1, k)

# arr = [1,2,None,3]
# tree = TreeNode().arr2tree(arr)
# print(tree)
# result = Solution().kthLargestLevelSum(tree, 1)
# print(result)
