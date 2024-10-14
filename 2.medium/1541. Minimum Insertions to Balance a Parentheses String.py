# Time Complexity:   O(n)
# Memory Complexity: O(1)

class Solution:
    def minInsertions(self, s: str) -> int:
        counter = maxi = second_closing = i = 0
        n = len(s)
        while i < n:
            if s[i] == ")":
                counter += 1
                maxi = max(maxi, counter)
                if i+1 < n and s[i+1] == ")":
                    i += 1
                else:
                    second_closing += 1
            else:
                counter -= 1
            i += 1
        return maxi + 2*(maxi - counter) + second_closing

# s = "(()))" # 1
# result = Solution().minInsertions(s)
# print(result, 1)

# s = "())" # 0
# result = Solution().minInsertions(s)
# print(result, 0)

# s = "))())("
# result = Solution().minInsertions(s)
# print(result, 3) #3

# s = "(((((("
# result = Solution().minInsertions(s)
# print(result, 12) #12

# s = ")))))))"
# result = Solution().minInsertions(s)
# print(result, 5) #5

# s = "(()))(()))()())))"
# result = Solution().minInsertions(s)
# print(result, 4) #4
