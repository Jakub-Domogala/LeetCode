# Time Complexity:   O(n) with cache
# Memory Complexity: O(n) with cache

# Time Complexity:   O(2^n) without cache
# Memory Complexity: O(1) without cache


class Solution(object):
    # not cached version
    # def climbStairs(self, n: int) -> int:
    #     if n <= 1:
    #         return 1
    #     return self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs(self, n: int) -> int:
        memorize = [None] * (n + 1)
        def fib_memorized(to_go = n):
            if memorize[to_go]:
                return memorize[to_go]
            if to_go <= 1:
                return 1
            memorize[to_go] = fib_memorized(to_go-1) + fib_memorized(to_go-2)
            return memorize[to_go]
        return fib_memorized()
        

# print(Solution().climbStairs(50))