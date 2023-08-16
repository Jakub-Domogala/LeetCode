# Time Complexity:   O(log_10(n))
# Memory Complexity: O(log_10(n))

class Solution(object):
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        for i in range(len(x_str) // 2):
            if x_str[i] != x_str[-(i + 1)]:
                return False
        return True

# print(Solution().isPalindrome(121))
# print(Solution().isPalindrome(-121))