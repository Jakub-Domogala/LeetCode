# Time Complexity:   O(4^n)
# Memory Complexity: O(4^n)

from typing import List


class Solution(object):
    def letterCombinations(self, digits: str) -> List[str]:
        digits = [int(x) for x in digits]
        options = [None, None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def go_next(curr, i, digits, options):
            if i >= len(digits):
                return [curr] if len(curr) > 0 else []
            result = []
            for opt in options[digits[i]]:
                result += go_next(curr + opt, i + 1, digits, options)
            return result

        return go_next("", 0, digits, options)


print(Solution().letterCombinations("79"))
