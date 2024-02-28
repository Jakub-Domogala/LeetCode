# Time Complexity:   O(n)
# Memory Complexity: O(n)

from math import inf
from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        result = []
        for i, e in enumerate(intervals):
            if newInterval[1] < e[0]:
                return result + [newInterval] + intervals[i:]
            elif newInterval[0] > e[1]:
                result += [e]
            else:
                newInterval = [min(e[0], newInterval[0]), max(e[1], newInterval[1])]
        return result + [newInterval]


# intervals = [[1, 2], [4, 5], [6, 7], [9, 10], [12, 16]]
# newInterval = [3, 8]
# print(Solution().insert(intervals, newInterval))

# print()

# intervals = [[4, 5], [6, 8]]
# newInterval = [0, 3]
# print(Solution().insert(intervals, newInterval))

# print()

# intervals = [[4, 5], [6, 8], [10, 16]]
# newInterval = [8, 15]
# print(Solution().insert(intervals, newInterval))
