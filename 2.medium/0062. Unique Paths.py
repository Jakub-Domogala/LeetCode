# Time Complexity:   O(n + m)
# Memory Complexity: O(1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    # combinatorial approach
        def factorial(n):
            result = 1
            while n > 1:
                result *= n
                n -= 1
            return result
            return
        return int(factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1)))

    # def uniquePaths(self, m: int, n: int) -> int:
    # # dp approach
    #     dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    #     dp[m-1][n-1] = 1
    #     for idm in range(m-1, -1, -1):
    #         for idn in range(n-1, -1, -1):
    #             if idm == m-1 and idn == n-1:
    #                 continue
    #             dp[idm][idn] = dp[idm+1][idn] + dp[idm][idn + 1]
    #     return dp[0][0]



# m = 3
# n = 7
# print(Solution().uniquePaths(m, n))

# m = 3
# n = 2
# print(Solution().uniquePaths(m, n))

# m = 100
# n = 100
# print(Solution().uniquePaths(m, n))
