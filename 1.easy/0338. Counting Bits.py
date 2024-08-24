# Time Complexity:   O(n)
# Memory Complexity: O(n)


from math import log2
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        D = [0] * (n + 1)
        [ D.__setitem__(i, 1 + D[i - 2**int(log2(i))]) for i in range(1, n + 1) ] # had to do a oneliner
        return D

    # def countBits(self, n: int) -> List[int]:
    #     D = [0] * (n + 1)
    #     for i in range(1,n+1):
    #         D[i] = 1 + D[i - 2**int(log2(i))]
    #     return D

# result = Solution().countBits(32)
# print(result)
