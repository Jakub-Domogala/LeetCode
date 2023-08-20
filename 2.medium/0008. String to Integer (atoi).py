# Time Complexity:   O(n)
# Memory Complexity: O(c)

class Solution(object):
    def myAtoi(self, s: str) -> int:
        # 1
        s = s.lstrip()

        i = 0
        result = 0
        n = len(s)
        sign = 1
        if n == 0:
            return result
        
        # 2
        if s[i] == '+' or s[i] == '-':
            sign = -1 if s[i] == '-' else sign
            i += 1

        # 3 4
        while i < n and ord('0') <= ord(s[i]) <= ord('9'):
            result *= 10
            result += ord(s[i]) - ord('0')
            if abs(result) > 2**31:
                break
            i += 1
        
        # 5
        return max(-2**31, min(result * sign, 2**31 - 1))
        
# print(Solution().myAtoi('  -012 1'))

