class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0
        while len(columnTitle) > 0:
            result += ord(columnTitle[0]) - ord("A") + 1
            columnTitle = columnTitle[1:]
            result *= 26

print(Solution().titleToNumber("A"))
print(Solution().titleToNumber("AB"))
print(Solution().titleToNumber("ZY"))
