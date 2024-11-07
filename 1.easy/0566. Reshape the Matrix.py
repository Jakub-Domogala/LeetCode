# Time Complexity:   O(n)
# Memory Complexity: O(n)
#
# where n = old_r * old_c


from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        old_c, old_r = len(mat[0]), len(mat)
        return [[mat[(ri*c+ci)//old_c][(ri*c+ci)%old_c] for ci in range(c)] for ri in range(r)] if r*c == old_r*old_c else mat

# mat = [[1,2],[3,4],[5,6]]
# r = 2
# c = 3
# print(mat)
# print(Solution().matrixReshape(mat, r, c))
