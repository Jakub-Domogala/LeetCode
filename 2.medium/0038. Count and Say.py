# Time Complexity:   O(n^2 * 2^n)
# Memory Complexity: O(2^n)

from itertools import groupby


class Solution(object):
    def countAndSay(self, n: int) -> str:
        result = "1"
        for _ in range(n - 1):
            result = "".join(
                [
                    str(len(g)) + str(g[0])
                    for g in ["".join(g) for _, g in groupby(result)]
                ]
            )
        return result


# print(Solution().countAndSay(4))
