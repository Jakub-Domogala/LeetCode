# Time Complexity:   O(n)
# Memory Complexity: O(n)


from math import gcd
from statistics import median
from typing import List

'''
This solution could be improved when it comes to memory complexity
by not cerating new copy of arrays(and handling it in place instead) to find each median and instead use
randomized_select with implementation of step and offset factor

This is a bit overkill so at this point I will not add it here
but it would make mem complexity O(1) while preserving O(n) runtime.
'''

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        n = len(arr)
        buckets_div = gcd(n, k)
        res = 0
        for i in range(buckets_div):
            sub_arr = arr[i::buckets_div]
            med = median(sub_arr)
            res += sum([abs(med - num) for num in sub_arr])
        return int(res)


arr = [1,4,1,3]
k = 2
result = Solution().makeSubKSumEqual(arr, k)
print(result)
