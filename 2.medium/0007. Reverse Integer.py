# Time Complexity:   O(1)
# Memory Complexity: O(1)

class Solution(object):
    def reverse(self, x: int) -> int:
        minus = False
        if x < 0:
            minus = True
            x = -x
        s = str(x)
        s = s[::-1]

        val = int(s) if not minus else -int(s)
        if -2**31 >= val or val >= 2**31 - 1:
            return 0
        return val


# print(Solution().reverse(-123))
