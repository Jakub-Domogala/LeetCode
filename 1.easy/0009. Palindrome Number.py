# Time Complexity:   O(log_10(n))
# Memory Complexity: O(log_10(n))


from math import log10, floor

class Solution(object):
    # def isPalindrome(self, x: int) -> bool: # this is just a challenge to not use string
    #     if x < 0:
    #         return False
    #     if x == 0:
    #         return True
    #     n = floor(log10(x)+1)
    #     p = 0
    #     print(n)
    #     for i in range (n//2):
    #         if (x//(10**p))%10 != (x//(10**(n-1-p)))%10:
    #             return False
    #         p += 1
    #     return True
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        for i in range(len(x_str) // 2):
            if x_str[i] != x_str[-(i + 1)]:
                return False
        return True


# print(Solution().isPalindrome(121))
# print(Solution().isPalindrome(1000021))
# print(Solution().isPalindrome(12345654322))
# print(Solution().isPalindrome(-121))
