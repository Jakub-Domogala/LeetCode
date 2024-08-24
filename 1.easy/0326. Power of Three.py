from math import log


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return log(n, 3) == int(log(n, 3))


result = Solution().isPowerOfThree(26)
print(result)
