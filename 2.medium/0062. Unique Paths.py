# Time Complexity:   O(n + m)
# Memory Complexity: O(1)


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def factorial(n):
            result = 1
            while n > 1:
                result *= n
                n -= 1
            return result
            return
        return int(factorial(m + n - 2) / (factorial(m - 1) * factorial(n - 1)))


# m = 3
# n = 7
# print(Solution().uniquePaths(m, n))

# m = 3
# n = 2
# print(Solution().uniquePaths(m, n))

# m = 100
# n = 100
# print(Solution().uniquePaths(m, n))
