# Time Complexity:   O(n)
# Memory Complexity: O(1)


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        balance = buffer = used_buffer =  0
        copen, cclose, cany = "(", ")", "*"
        is_neutral = False
        for c in s:
            if c != cany:
                balance += 1 if c == copen else -1
            else:
                balance -= 1
                buffer += 1
            if balance < 0:
                if buffer <= 0:
                    return False
                if is_neutral:
                    buffer -= 1
                    is_neutral = False
                else:
                    is_neutral = True
                balance += 1
        return balance == 0

# s = "()"
# result = Solution().checkValidString(s)
# print(result, True)
# s = "(*)"
# result = Solution().checkValidString(s)
# print(result, True)
# s = "(*))"
# result = Solution().checkValidString(s)
# print(result, True)
# s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())"
# result = Solution().checkValidString(s)
# print(result, False)
