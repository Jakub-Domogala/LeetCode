# Time Complexity:   O(n**2)
# Memory Complexity: O(n**2)


from typing import List
from collections import defaultdict

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        def make_counter_dict(nums1, nums2):
            dict = defaultdict(int)
            for n1 in nums1:
                for n2 in nums2:
                    dict[n1+n2] += 1
            return dict
        dict1 = make_counter_dict(nums1, nums2)
        dict2 = make_counter_dict(nums3, nums4)
        result = 0
        for num1, mul1 in dict1.items():
            result += dict2[-num1] * mul1
        return result


# nums1 = [1,2]
# nums2 = [-2,-1]
# nums3 = [-1,2]
# nums4 = [0,2]
# result = Solution().fourSumCount(nums1, nums2, nums3, nums4)
# print(result)

# nums1 = [0,1,-1]
# nums2 = [-1,1,0]
# nums3 = [0,0,1]
# nums4 = [-1,1,1]
# result = Solution().fourSumCount(nums1, nums2, nums3, nums4)
# print(result)
