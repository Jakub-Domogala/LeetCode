# Time Complexity:   O(n)
# Memory Complexity: O(1)

class Solution(object):
    def lengthOfLastWord(self, s: str) -> int:
        # return len(s.split()[-1]) # this has worse memory complexity O(n)
        n = len(s)
        index = n - 1
        while index >= 0 and s[index] == " ":
            index -= 1
        for i in range(index, -1, -1):
            if s[i] == " ":
                return index - i
        return index + 1

# print(Solution().lengthOfLastWord("   fly me   to   the moon  "))