# Time Complexity:   O(n^2)
# Memory Complexity: O(n)

from collections import deque
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rowIndex += 1
        result = deque()
        result.append([1])
        for rowNum in range(1, rowIndex):
            result.append([1])
            for i in range(rowNum - 1):
                result[1].append(result[0][i] + result[0][i + 1])
            result[1].append(1)
            result.popleft()
        return result[0]


# result = Solution().getRow(33)
# print(result)
