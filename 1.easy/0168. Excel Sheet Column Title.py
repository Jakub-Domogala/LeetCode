# Time Complexity:   O(log10(n))
# Memory Complexity: O(log10(n))


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber == 1:
            return "A"
        numeric_system = ord("Z") - ord("A") + 1
        result = ""
        columnNumber -= 1
        while columnNumber > 0:
            result = chr(columnNumber%numeric_system + ord("A")) + result
            columnNumber //= numeric_system
            columnNumber -= 1
        result = chr(columnNumber%numeric_system + ord("A")) + result if columnNumber == 0 else result
        return result

# for i in range(1,30):
#     print(Solution().convertToTitle(i))
