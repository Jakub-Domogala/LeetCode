# Time Complexity:   O(n)
# Memory Complexity: O(n)


class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ""
        n = len(s)
        if n%2 == 0:
            for i in range(0,len(s),2):
                result += s[i] + chr(ord(s[i]) + int(s[i+1]))
        else:
            for i in range(0,len(s)-1,2):
                result += s[i] + chr(ord(s[i]) + int(s[i+1]))
            result += s[-1]
        return result

# s = "a1c1e1"
# print(Solution().replaceDigits(s), "abcdef")
