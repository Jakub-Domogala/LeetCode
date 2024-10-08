
# Time Complexity:   O(n)
# Memory Complexity: O(1)

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        counter = maxi = 0
        for i in s:
            counter += -1 if i == "(" else 1
            maxi = max(maxi, counter)
        return maxi + maxi - counter


# s = "())"
# result = Solution().minAddToMakeValid(s)
# print(result) # 1

# s = "((("
# result = Solution().minAddToMakeValid(s)
# print(result) # 3

# s = "()))(("
# result = Solution().minAddToMakeValid(s)
# print(result) # 4

# s = "())"
# result = Solution().minAddToMakeValid(s)
# print(result) # 1
