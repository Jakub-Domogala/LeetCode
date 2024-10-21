from typing import List

class SummaryRanges:

    def __init__(self):
        self.s_list = []

    def addNum(self, value: int) -> None:
        # Time Complexity:   O(logn)
        # Memory Complexity: O(1)

        def binary_search_geq(arr: List[int], target: int):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return mid
            return left

        idx = binary_search_geq(self.s_list, value) if len(self.s_list) > 0 else 0
        # print(len(self.s_list), idx)
        if idx < len(self.s_list) and self.s_list[idx] == value:
            return
        self.s_list.insert(idx, value)

    def getIntervals(self) -> List[List[int]]:
        # Time Complexity:   O(n)
        # Memory Complexity: O(n)

        n = len(self.s_list)
        print(self.s_list)
        if n == 0:
            return []
        result = [[self.s_list[0], self.s_list[0]]]
        for i in range(1, n):
            if self.s_list[i] - 1 == result[-1][1]:
                result[-1][1] = self.s_list[i]
            else:
                result.append([self.s_list[i], self.s_list[i]])
        return result


# summaryRanges = SummaryRanges();
# summaryRanges.addNum(1);      # arr = [1]
# print(summaryRanges.getIntervals()); # return [[1, 1]]
# summaryRanges.addNum(3);      # arr = [1, 3]
# print(summaryRanges.getIntervals()); # return [[1, 1], [3, 3]]
# summaryRanges.addNum(7);      # arr = [1, 3, 7]
# print(summaryRanges.getIntervals()); # return [[1, 1], [3, 3], [7, 7]]
# summaryRanges.addNum(2);      # arr = [1, 2, 3, 7]
# print(summaryRanges.getIntervals()); # return [[1, 3], [7, 7]]
# summaryRanges.addNum(6);      # arr = [1, 2, 3, 6, 7]
# print(summaryRanges.getIntervals()); # return [[1, 3], [6, 7]]
