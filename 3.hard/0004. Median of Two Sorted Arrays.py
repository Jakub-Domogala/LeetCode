# Time Complexity:   O(log(n))
# Memory Complexity: O(1)
# Where n is summary length of arrays
from typing import List


class Solution(object):
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def get_values(arr: List[int], idx: int):
            p_val  = arr[idx] if idx >= 0 else float("-infinity")
            next_val = arr[idx + 1]  if idx + 1 < len(arr) else float("infinity")
            return p_val, next_val
        
        A, B = nums1, nums2
        n = len(nums1) + len(nums2)
        half_n = n // 2

        if len(A) > len(B):
            A, B = B, A

        l, r = 0, len(A) - 1

        while True:
            i = (l + r) // 2
            j = half_n - i - 2

            A_pivot_val, A_next_val = get_values(A, i)
            B_pivot_val, B_next_val = get_values(B, j)

            if A_pivot_val <= B_next_val and B_pivot_val <= A_next_val:
                if n % 2:
                    return min(A_next_val, B_next_val)
                return float(max(A_pivot_val, B_pivot_val) + min(A_next_val, B_next_val)) / 2
            elif A_pivot_val > B_next_val:
                r = i - 1
            else:
                l = i + 1

# res 5.5
# a = [2,4,5,6,7,8,9]
# b = [1,2,3,9,10]

# res 3
# a = [1,2]
# b = [3,4,5]
# print(Solution().findMedianSortedArrays(a, b))
