from typing import List


def binary_search(arr: List[int], target: int):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1


# print(binary_search([1,2,3,4], 2))
