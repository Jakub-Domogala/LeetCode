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


def binary_search_options(arr: List[int], target: int):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] > target:
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            return mid, mid, mid
    return (left if left < len(arr) else -1), -1, right


def binary_search_for_range(arr: List[int], target_min: int, target_max: int):
    i_min = binary_search_options(arr, target_min)[0]
    i_max = binary_search_options(arr, target_max)[2]
    if i_min != -1 and i_max != -1 and i_min <= i_max:
        return i_min, i_max
    return None


# def binary_search_for_range(arr: List[int], target_min: int, target_max: int):
#     i_min = binary_search_geq(arr, target_min)
#     i_max = binary_search_leq(arr, target_max)
#     if i_min != -1 and i_max != -1 and i_min <= i_max:
#         return i_min, i_max
#     return None


def binary_search_for_first_and_last_occurance(arr: List[int], target: int):
    def find_first():
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def find_last():
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1
        return right

    i_min = find_first()
    i_max = find_last()
    if i_min != -1 and i_max != -1 and i_min <= i_max:
        return i_min, i_max
    return -1, -1


print("=" * 10, "Meant for unique elements", "=" * 10)
print()
print("Binary Search")
print(binary_search([1, 2, 3, 4], 2), 1)
print(binary_search([1, 3, 4], -1), -1)
print()
print("Binary Search GEQ")
print(binary_search_geq([1, 3, 4, 5, 7, 8], 2), 1)
print(binary_search_geq([1, 3, 4, 5, 7, 8], 3), 1)
print(binary_search_geq([1, 3, 4, 5, 7, 8], 10), -1)
print(binary_search_geq([1, 3, 4, 5, 7, 8], -10), 0)
print()
print("Binary Search LEQ")
print(binary_search_leq([1, 3, 4, 5, 7, 8], 2), 0)
print(binary_search_leq([1, 3, 4, 5, 7, 8], 3), 1)
print(binary_search_leq([1, 3, 4, 5, 7, 8], 10), 5)
print(binary_search_leq([1, 3, 4, 5, 7, 8], -10), -1)
print()
print("Binary For Range")
print(binary_search_for_range([1, 3, 4, 5, 7, 8], 2, 5), [1, 3])
print(binary_search_for_range([1, 3, 4, 5, 7, 8], 3, 5), [1, 3])
print(binary_search_for_range([1, 3, 4, 5, 7, 8], 10, 12), None)
print(binary_search_for_range([1, 3, 4, 5, 7, 8], -10, 10), [0, 5])
print(binary_search_for_range([1, 3, 4, 5, 7, 8], 5, 5), [3, 3])
print(binary_search_for_range([1, 3, 4, 5, 7, 8], 6, 6), None)
print()
print("=" * 10, "Meant for non-unique elements", "=" * 10)
print("Binary For First and Last Occurance")
print(binary_search_for_first_and_last_occurance([1, 2, 2, 2, 4], 2), [1, 3])
print(binary_search_for_first_and_last_occurance([1, 2, 2, 2, 4], 1), [0, 0])
print(binary_search_for_first_and_last_occurance([1, 2, 2, 2, 4], 3), [-1, -1])
print(binary_search_for_first_and_last_occurance([1, 2, 2, 2, 4], 0), [-1, -1])
print(binary_search_for_first_and_last_occurance([1, 2, 2, 2, 4], 5), [-1, -1])
