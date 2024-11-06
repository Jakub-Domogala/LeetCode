# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        rolling_max = 0
        result = 0
        for i, e in enumerate(arr):
            rolling_max = max(rolling_max, e)
            if rolling_max == i:
                result += 1
        return result

# class Solution: # time O(n), space O(n)
#     def maxChunksToSorted(self, arr: List[int]) -> int:
#         print()
#         n = len(arr)
#         pref = [0]*n
#         for i, e in enumerate(arr):
#             pref[min(i, e)] += 1
#             pref[max(i, e)] -= 1
#         result = 0
#         state = 0
#         for p in pref:
#             state += p
#             if state == 0:
#                 result += 1
#         return result



# arr = [4,3,2,1,0]
# result = Solution().maxChunksToSorted(arr)
# print("res:",result,"exp:",1)
# arr = [1,0,2,4,3,5]
# result = Solution().maxChunksToSorted(arr)
# print("res:",result,"exp:",4)
# arr = [1,2,0,3]
# result = Solution().maxChunksToSorted(arr)
# print("res:",result,"exp:",2)
# arr = [2,0,1]
# result = Solution().maxChunksToSorted(arr)
# print("res:",result,"exp:",1)
# arr = [1,4,3,6,0,7,8,2,5]
# result = Solution().maxChunksToSorted(arr)
# print("res:",result,"exp:",1)
# arr = [0,2,1]
# result = Solution().maxChunksToSorted(arr)
# print("res:",result,"exp:",2)
