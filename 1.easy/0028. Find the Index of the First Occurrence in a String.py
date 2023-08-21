# Time Complexity:   O(n^2)
# Memory Complexity: O(1)

class Solution(object):
    def strStr(self, haystack: str, needle: str) -> int:
        # return haystack.find(needle)
        for i in range(0, len(haystack) - len(needle) + 1):
            if haystack[i] == needle[0]:
                for j in range(len(needle)):
                    if haystack[i + j] != needle[j]:
                        break
                    if j == len(needle) - 1:
                        return i
        return - 1

# print(Solution().strStr("sadbutsad", "sad"))