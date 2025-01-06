# Time Complexity:   O(m*n)
# Memory Complexity: O(m*n)
# Where grid is of size m x n

from math import inf
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[inf for _ in range(n)] for _ in range(m)]
        dp[m-1][n-1] = grid[m-1][n-1]
        for idm in range(m-1, -1, -1):
            for idn in range(n-1, -1, -1):
                if (idm == m-1 and idn == n-1):
                    continue
                if idm < m-1:
                    dp[idm][idn] = dp[idm+1][idn] + grid[idm][idn]
                if idn < n-1:
                    dp[idm][idn] = min(dp[idm][idn + 1] + grid[idm][idn], dp[idm][idn])
        return dp[0][0]

# grid = [[1,3,1],[1,5,1],[4,2,1]]
# print(Solution().minPathSum(grid))
# grid = [[1,2,3],[4,5,6]]
# print(Solution().minPathSum(grid))
