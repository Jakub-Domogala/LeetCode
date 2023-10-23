# Time Complexity:   O(n^2)
# Memory Complexity: O(n^2)

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        result = [[1]]
        for rowNum in range(1, numRows):
            result.append([1])
            for i in range(rowNum - 1):
                result[rowNum].append(result[rowNum - 1][i] + result[rowNum - 1][i + 1])
            result[rowNum].append(1)
        return result


print(Solution().generate(5))
