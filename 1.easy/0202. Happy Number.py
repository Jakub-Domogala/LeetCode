from collections import defaultdict

class Solution:
    def isHappy(self, n: int) -> bool:
        check = defaultdict(bool)
        def sum_square_parts(n):
            result = 0
            while n != 0:
                result += (n%10)**2
                n //= 10
            return result
        while n != 1:
            n = sum_square_parts(n)
            if check[n] :
                return False
            check[n] = True
        return True



n = 19
result = Solution().isHappy(n)
print(result, True)
n = 2
result = Solution().isHappy(n)
print(result, False)
