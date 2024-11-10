# Time Complexity:   O(n)
# Memory Complexity: O(n)


from typing import List

class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        stack = []
        for e in arr:
            if not stack or stack[-1] <= e:
                stack.append(e)
            else:
                cmax = stack[-1]
                while stack and stack[-1] > e:
                    cmax = max(cmax, stack.pop())
                stack.append(cmax)
        return len(stack)



    # def maxChunksToSorted(self, arr: List[int]) -> int: # time O(nlogn), mem O(n)
        # def maxChunksToSortedI(arr):
        #     rolling_max = 0
        #     result = 0
        #     for i, e in enumerate(arr):
        #         rolling_max = max(rolling_max, e)
        #         if rolling_max == i:
        #             result += 1
        #     return result
        # with_idx = [[i, e] for i,e in enumerate(arr)]
        # sorted_final_idx = sorted(with_idx, key=lambda x: x[1])
        # unsorted_final_idx = [None] * len(arr)
        # for idx, ie in enumerate(sorted_final_idx):
        #     i, e = ie
        #     unsorted_final_idx[i] = idx
        # return maxChunksToSortedI(unsorted_final_idx)


# arr = [2,1,3,4,4]
# result = Solution().maxChunksToSorted(arr)
# print(result, 4)
