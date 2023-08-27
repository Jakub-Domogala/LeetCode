class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        A, B = nums1, nums2
        n = len(nums1) + len(nums2)
        half = n // 2
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1
        while True:
            i = (l + r) // 2
            j = half - i - 2

            A_left  = A[i]      if i >= 0           else float("-infinity")
            B_left  = B[j]      if j >= 0           else float("-infinity")
            A_right = A[i + 1]  if i + 1 < len(A)   else float("infinity")
            B_right = B[j + 1]  if j + 1 < len(B)   else float("infinity")

            if A_left <= B_right and B_left <= A_right:
                print(A_left, A_right, B_left, B_right)
                if n % 2:
                    return min(A_right, B_right)
                return float(max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                r = i - 1
            else:
                l = i + 1


        

            


        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

# res 5

# 1,2,2,3,4,5,6,7,8,9,9,10
# a = [2,4,5,6,7,8,9]
# b = [1,2,3,9,10]
a = [1,2]
b = [3,4]
print(Solution().findMedianSortedArrays(a, b))
