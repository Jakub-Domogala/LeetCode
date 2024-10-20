# Time Complexity:   O(n)
# Memory Complexity: O(n)


from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        def check_bucket(idx, offset = 0):
            nonlocal buckets_dict, nums, indexDiff, valueDiff
            return (nums[i]//valueDiff+offset in buckets_dict
                and i - buckets_dict[nums[i]//valueDiff+offset][1] <= indexDiff
                and abs(buckets_dict[nums[i]//valueDiff+offset][0]-nums[i]) <= valueDiff)

        if len(nums) < 2 or indexDiff == 0:
            return False

        buckets_dict = {}
        if valueDiff == 0:
            for i in range(len(nums)):
                if nums[i] in buckets_dict and i - buckets_dict[nums[i]] <= indexDiff:
                    return True
                buckets_dict[nums[i]] = i
            return False
        else:
            for i in range(len(nums)):
                if (check_bucket(i)
                    or check_bucket(i, 1)
                    or check_bucket(i, -1)):
                    return True
                buckets_dict[nums[i]//valueDiff] = [nums[i], i]

        return False


# class Solution:
#     def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
    # O(nlogn), O(n) solution, made me realise simplicity of the problem
#         def merge_by_val(A):
#             B = []
#             for e in A:
#                 if len(B) > 0 and B[-1][0] == e[0]:
#                     B[-1][1].append(e[1])
#                 else:
#                     B.append([e[0], [e[1]]])
#             return B

#         def binary_search_options(arr: List[int], target: int):
#             left, right = 0, len(arr) - 1
#             while left <= right:
#                 mid = (left + right) // 2
#                 if arr[mid] > target:
#                     right = mid - 1
#                 elif arr[mid] < target:
#                     left = mid + 1
#                 else:
#                     return mid, mid, mid
#             return (left if left < len(arr) else -1), -1, right

#         def binary_search_for_range(arr: List[int], target_min: int, target_max: int):
#             i_min = binary_search_options(arr, target_min)[0]
#             i_max = binary_search_options(arr, target_max)[2]
#             if i_min != -1 and i_max != -1 and i_min <= i_max:
#                 return i_min, i_max
#             return None


#         nums_with_index = [[x, i] for i, x in enumerate(nums)]
#         nums_with_index.sort(key=lambda x: x[1])
#         nums_with_index.sort(key=lambda x: x[0])
#         nums_with_index = merge_by_val(nums_with_index)
#         nums_no_index = [x for x, y in nums_with_index]

#         for i, num in enumerate(nums):
#             values = binary_search_for_range(nums_no_index, num-valueDiff, num+valueDiff)

#             if values is None:
#                 continue

#             for j in range(values[0], values[1]+1):
#                 indexes = binary_search_for_range(nums_with_index[j][1], i-indexDiff, i+indexDiff)
#                 if indexes is None:
#                     # print("did not find")
#                     continue
#                 for nei_i in range(indexes[0], indexes[1]+1):
#                     if nums_with_index[j][1][nei_i] == i:
#                         continue
#                     # print("result", nei_i, nums[nums_with_index[j][1][nei_i]])
#                     return True
#         # print(nums_with_index)
#         return False

# nums = [1,10,2,10,3,1]
# indexDiff = 1
# valueDiff = 2
# result = Solution().containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)
# print(result)

# nums = [1,5,9,1,5,9]
# indexDiff = 2
# valueDiff = 3
# result = Solution().containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)
# print(result)

# nums = [2,1,100,200,5]
# indexDiff = 3
# valueDiff = 3
# result = Solution().containsNearbyAlmostDuplicate(nums, indexDiff, valueDiff)
# print(result)
