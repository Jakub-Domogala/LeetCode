# Time Complexity:   O(log(n))
# Memory Complexity: O(1)

class Solution(object):
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        return right

# print(Solution().mySqrt(6)) # 2
# print(Solution().mySqrt(9)) # 3
# print(Solution().mySqrt(10)) # 3