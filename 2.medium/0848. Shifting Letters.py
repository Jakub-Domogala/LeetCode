# Time Complexity:   O(n)
# Memory Complexity: O(n)


from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        alph_size = ord("z") - ord("a") + 1
        n = len(s)
        shifts[-1] = shifts[-1]%alph_size
        for i in range(n-2,-1,-1):
            shifts[i] = (shifts[i+1] + shifts[i])%alph_size
        result = ""
        for i in range(n):
            result += chr((ord(s[i]) + shifts[i] - ord("a")) % alph_size + ord("a"))
        return result

# s = "abc"
# shifts = [3,5,9]
# print(Solution().shiftingLetters(s, shifts), "rpl")
