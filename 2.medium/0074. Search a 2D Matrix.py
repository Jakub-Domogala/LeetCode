# Time Complexity:   O(log(n) + log(m)) == O(log(n*m))
# Memory Complexity: O(1)
# these complexities would be correct if not the fact I am
# creating new arr of length 'm', because I was too lazy to implement 2 separate
# binary search functions for searching rows and cols

from typing import List


class Solution(object):
    def searchMatrix(self, matrix: List[List[int]], target: int):
        def binary_search_less_or_eq(arr: List[int], target: int = target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] > target:
                    right = mid - 1
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    return mid, True
            return right, False

        row_idx, is_found = binary_search_less_or_eq([row[0] for row in matrix])
        if is_found:
            return True
        col_idx, is_found = binary_search_less_or_eq(matrix[row_idx])
        # if is_found:
        #     print(f"Number found in row={row_idx}, col={col_idx}")
        return is_found


# matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
# print(Solution().searchMatrix(matrix, 3))
