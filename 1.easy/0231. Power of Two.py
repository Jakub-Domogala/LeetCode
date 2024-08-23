# Time Complexity:   O(logn)
# Memory Complexity: O(1)


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        tester = 1
        while tester < n:
            tester <<= 1
        return tester == n

# n = 1
# result = Solution().isPowerOfTwo(n)
# print(result)
