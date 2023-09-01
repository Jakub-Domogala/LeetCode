# Time Complexity:   O(n)
# Memory Complexity: O(n)

import re


class Solution(object):
    def isPalindrome(self, s: str) -> bool:
        clean = re.sub(r"[^a-zA-Z0-9]", "", s).lower()
        return clean == clean[::-1]


# print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
