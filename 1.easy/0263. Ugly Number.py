# Time Complexity:   O(logn)
# Memory Complexity: O(1)


class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 == 0:
            n //= 2
        for i in range(3, int(n**0.5) + 1, 2):
            while n % i == 0:
                if i > 5:
                    return False
                n //= i
        return n <= 5

# print(Solution().isUgly(6), True)
# print(Solution().isUgly(1), True)
# print(Solution().isUgly(14), False)
