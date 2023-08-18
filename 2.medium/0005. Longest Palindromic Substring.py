# Time Complexity:   O(n^2)
# Memory Complexity: O(n)

class Solution(object):
    def longestPalindrome(self, s: str) -> str:
        def expand_palindrome():
            nonlocal left, right, result, res_len
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > res_len:
                    result = s[left:right+1]
                    res_len = right - left + 1
                left -= 1
                right += 1
        result = ""
        res_len = 0
        for i in range(len(s)):
            left, right = i, i
            expand_palindrome()
            left, right = i, i + 1
            expand_palindrome()
        return result


# print(Solution().longestPalindrome("babad"))
