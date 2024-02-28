# Time Complexity:   O(log(n))
# Memory Complexity: O(1)
# it is modified bin search


class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            if not isBadVersion(m):
                l = m + 1
            else:
                r = m - 1
        return l


bad_idx = 4
n = 5


def isBadVersion(x):
    return x >= bad_idx


print(Solution().firstBadVersion(5))
