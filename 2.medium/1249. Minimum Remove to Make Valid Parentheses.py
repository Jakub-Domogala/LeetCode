# Time Complexity:   O(n)
# Memory Complexity: O(n)


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        counter = maxi = 0
        for i in s:
            counter += -1 if i == "(" else (1 if i ==")" else 0)
            maxi = max(maxi, counter)
        # remove [maxi] )'s from start to end
        # remove [maxi - counter] ('s from end to start
        return s.replace(")", "", maxi)[::-1].replace("(", "", maxi - counter)[::-1]

# s = "lee(t(c)o)de)"
# result = Solution().minRemoveToMakeValid(s)
# print(result)

# s = "a)b(c)d"
# result = Solution().minRemoveToMakeValid(s)
# print(result)

# s = "))(("
# result = Solution().minRemoveToMakeValid(s)
# print(result)

# s = "(a(b(c)d)"
# result = Solution().minRemoveToMakeValid(s)
# print(result)
