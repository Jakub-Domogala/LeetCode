# Time Complexity:   O(nlogn)
# Memory Complexity: O(n)
#
# where n = rows*cols


from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        return sorted([[x, y] for x in range(rows) for y in range(cols)], key=lambda c: abs(c[0]-rCenter) + abs(c[1]-cCenter))

# rows = 1
# cols = 2
# rCenter = 0
# cCenter = 0
# print(Solution().allCellsDistOrder(rows, cols, rCenter, cCenter))

# rows = 2
# cols = 3
# rCenter = 1
# cCenter = 2
# print(Solution().allCellsDistOrder(rows, cols, rCenter, cCenter))
