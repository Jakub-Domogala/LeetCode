# Time Complexity:   O(n)
# Memory Complexity: O(1)
# where n is len(s)


class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * (ord("z") - ord("a") + 1)
        for i in range(len(s)):
            count[ord(s[i]) - ord("a")] += 1
            count[ord(t[i]) - ord("a")] -= 1
        return len([x for x in count if x != 0]) == 0


print(Solution().isAnagram("ale", "ela"))
