# Time Complexity:   O(n)
# Memory Complexity: O(1)

'''
Beats 99.63% in Runtime and 100% in Memory

The idea is that when we iterate over string, when we see locked char we do casual addition or subtraction
from the balance variable(same as in all of similar problems), when we see unlocked we always try to use closing
bracket(use openning only if balance becomes negative)
We keep buffer of available brackets that we can change.
'''

class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n % 2 == 1:
            return False

        balance = buffer = 0
        copen, cclose = "(", ")"
        cunlocked, clocked = "0", "1"
        for l, c in zip(locked, s):
            if l == clocked:
                balance += 1 if c == copen else -1
            else:
                balance -= 1
                buffer += 1
            if balance < 0:
                if buffer <= 0:
                    return False
                buffer -= 1
                balance += 2
        return balance == 0



# s = "()))"
# l = "1011"
# result = Solution().canBeValid(s, l)
# print(result, True)
# s = "()(())()))"
# l = "1100001111"
# result = Solution().canBeValid(s, l)
# print(result, True)
# s = "())(()(()(())()())(())((())(()())((())))))(((((((())(()))))("
# l = "100011110110011011010111100111011101111110000101001101001111"
# result = Solution().canBeValid(s, l)
# print(result, False)
