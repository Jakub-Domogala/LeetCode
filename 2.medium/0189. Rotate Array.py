# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import List
from math import gcd

'''
Reason why gcd is needed here is to decide how many times looplike
procedure of moving numbers forward will be needed to cover whole array.

for example:
arr = [1,2,3,4]
k = 2
will have gcd = 2
so first loop will take care of elements 1 and 3, second procedure of elements 2, 4.
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        divisor = gcd(n, k)
        for i in range(divisor):
            last_num = nums[i]
            j = k
            while (i+j)%n != i:
                nums[(i+j)%n], last_num = last_num, nums[(i+j)%n]
                j += k
            nums[(i+j)%n], last_num = last_num, nums[(i+j)%n]


# arr = [1,2,3,4]
# k = 3
# Solution().rotate(arr, k)
# print(arr)
# arr = [1,2,3,4]
# k = 2
# Solution().rotate(arr, k)
# print(arr)
