# Time Complexity:   O(nlog(n))
# Memory Complexity: O(k)
# where n is len(points). As sorted I count complexity of quicksort

from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # here we could write something like quicksort if don't wanna use sorted
        points = sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])
        return points[:k]


# points = [[3, 3], [5, -1], [-2, 4]]
# k = 2
# print(Solution().kClosest(points, k))
