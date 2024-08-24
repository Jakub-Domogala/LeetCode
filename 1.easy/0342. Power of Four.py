from math import log


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return log(n, 4) == int(log(n, 4))


result = Solution().isPowerOfFour(17)
print(result)
