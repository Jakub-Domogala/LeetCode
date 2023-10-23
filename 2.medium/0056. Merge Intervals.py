# Time Complexity:   O(n)
# Memory Complexity: O(n)
# where n is len(intervals)

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[1])
        print(intervals)
        result = []
        curr_i = intervals[0]
        for i in intervals[1:]:
            if curr_i[1] < i[0]:
                result.append(curr_i)
                curr_i = i
            else:
                curr_i[1] = max(curr_i[1], i[1])
        result.append(curr_i)
        print(result)


# intervals = [[1, 4], [4, 5]]
# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# print(Solution().merge(intervals))
