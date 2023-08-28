# Time Complexity:   O(m + n)
# Memory Complexity: O(1)

from typing import List


class Solution(object):
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i1 = m - 1
        i2 = n - 1
        idx = m + n - 1
        while i1 >= 0 or i2 >= 0:
            if i2 == -1 or i1 > -1 and nums1[i1] >= nums2[i2]:
                nums1[idx] = nums1[i1]
                i1 -= 1
            else:
                nums1[idx] = nums2[i2]
                i2 -= 1
            idx -= 1
        
# a, b = [1,2,3,0,0,0], [2,5,6]
# Solution().merge(a, 3, b, 3)
# print(a)