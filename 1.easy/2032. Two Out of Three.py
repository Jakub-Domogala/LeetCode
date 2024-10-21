# Time Complexity:   O(n)
# Memory Complexity: O(n)


from typing import List

class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # return [e for e in list(set(nums1 + nums2 + nums3)) if sum([1 if e in s else 0 for s in [set(nums1), set(nums2), set(nums3)]]) >= 2]
        s1,s2,s3 = set(nums1),set(nums2),set(nums3)
        return list(s1&s2|s2&s3|s1&s3)


# nums1 = [1,1,3,2]
# nums2 = [2,3]
# nums3 = [3]
# result = Solution().twoOutOfThree(nums1, nums2, nums3)
# print(result)
