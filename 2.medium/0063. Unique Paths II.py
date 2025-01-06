from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[m-1][n-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp[m-1][n-1] = 1
        for idm in range(m-1, -1, -1):
            for idn in range(n-1, -1, -1):
                if (idm == m-1 and idn == n-1) or obstacleGrid[idm][idn] == 1:
                    continue
                if idm < m-1 and obstacleGrid[idm+1][idn] == 0:
                    dp[idm][idn] += dp[idm+1][idn]
                if idn < n-1 and obstacleGrid[idm][idn + 1] == 0:
                    dp[idm][idn] += dp[idm][idn + 1]
        return dp[0][0]

# obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# print(Solution().uniquePathsWithObstacles(obstacleGrid))
# obstacleGrid = [[0,1],[0,0]]
# print(Solution().uniquePathsWithObstacles(obstacleGrid))
# obstacleGrid = [[1]]
# print(Solution().uniquePathsWithObstacles(obstacleGrid))
