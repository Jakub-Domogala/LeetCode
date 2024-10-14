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

def binary_search_geq(arr: List[int], target: int):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
    return left if left < len(arr) else -1

def binary_search_leq(arr: List[int], target: int):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid
    return right

def binary_search_for_range(arr: List[int], target_min: int, target_max: int):
    i_min = binary_search_geq(arr, target_min)
    i_max = binary_search_leq(arr, target_max)
    if i_min != -1 and i_max != -1 and i_min <= i_max:
        return i_min, i_max
    return None

print(binary_search([1,2,3,4], 2), 1)
print(binary_search([1,3,4], -1), -1)
print()
print(binary_search_geq([1,3,4,5,7,8], 2), 1)
print(binary_search_geq([1,3,4,5,7,8], 3), 1)
print(binary_search_geq([1,3,4,5,7,8], 10), -1)
print(binary_search_geq([1,3,4,5,7,8], -10), 0)
print()
print(binary_search_leq([1,3,4,5,7,8], 2), 0)
print(binary_search_leq([1,3,4,5,7,8], 3), 1)
print(binary_search_leq([1,3,4,5,7,8], 10), 5)
print(binary_search_leq([1,3,4,5,7,8], -10), -1)
print()
print(binary_search_for_range([1,3,4,5,7,8], 2, 5), [1,3])
print(binary_search_for_range([1,3,4,5,7,8], 3, 5), [1,3])
print(binary_search_for_range([1,3,4,5,7,8], 10, 12), None)
print(binary_search_for_range([1,3,4,5,7,8], -10, 10), [0,5])
print(binary_search_for_range([1,3,4,5,7,8], 5, 5), [3,3])
print(binary_search_for_range([1,3,4,5,7,8], 6, 6), None)
