# Time Complexity:   O(n)
# Memory Complexity: O(1)


class Solution:
    def hammingWeight(self, n: int) -> int:
        sum = 0
        while n != 0:
            sum += n%2
            n = n >> 1
        return sum


# n = 11
# result = Solution().hammingWeight(n)
# print(result)
