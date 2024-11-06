# Time Complexity:   O(nlogn)
# Memory Complexity: O(n)

from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def sbits(n):
            return bin(n).count("1")
        return [y for x,y in sorted([[sbits(x), x] for x in arr])]

# arr = [0,1,2,3,4,5,6,7,8]
# print(Solution().sortByBits(arr), [1,2,4,8,3,5,6,7])
# arr = [1024,512,256,128,64,32,16,8,4,2,1]
# print(Solution().sortByBits(arr))
