# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        walking_sum = 0
        n = len(code)
        result = [0] * n
        if k == 0:
            return result
        for i in range(abs(k)):
            walking_sum += code[i]
        for i in range(n):
            if k > 0:
                result[i-1] = walking_sum
            else:
                result[(i-k)%n] = walking_sum
            walking_sum += code[(i+abs(k))%n] - code[i]
        return result

# code = [5,7,1,4]
# k = 3
# result = Solution().decrypt(code, k)
# print(result)

# code = [2,4,9,3]
# k = -2
# result = Solution().decrypt(code, k)
# print(result)
