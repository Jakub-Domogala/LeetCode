# Time Complexity:   O(n)
# Memory Complexity: O(n)


from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [original[mi:mi+n] for mi in range(0,m*n,n)] if m*n == len(original) else []

# original = [1,2,3]
# m = 1
# n = 3
# print(Solution().construct2DArray(original, m, n))
# original = [1,2,3]
# m = 3
# n = 1
# print(Solution().construct2DArray(original, m, n))
