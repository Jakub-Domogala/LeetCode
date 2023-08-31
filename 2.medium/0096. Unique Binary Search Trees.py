# Time Complexity:   O(n)
# Memory Complexity: O(n)

class Solution(object):
    def numTrees(self, n: int) -> int:
        memo = [None] * (n + 1)
        memo[0], memo[1] = 1, 1
        def calc_tree(n: int) -> int:
            if memo[n]:
                return memo[n]
            count = 0
            n -= 1
            for i in range(n+1):
                count += calc_tree(n-i) * calc_tree(i)
            memo[n+1] = count
            return count
        return calc_tree(n)


# print(Solution().numTrees(19))