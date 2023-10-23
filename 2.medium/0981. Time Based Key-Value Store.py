# Memory Complexity of storage: O(n)

# SET Time Complexity:   O(1)
# SET Memory Complexity: O(1)

# GET Time Complexity:   O(log(n))
# GET Memory Complexity: O(1)

from collections import defaultdict
from typing import List, Tuple


class TimeMap:
    def __init__(self):
        self.memo = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.memo[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        def binary_search(arr: List[Tuple[int, str]], target: int):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid][0] > target:
                    right = mid - 1
                elif arr[mid][0] < target:
                    left = mid + 1
                else:
                    return mid
            return right

        tab = self.memo[key]
        index = binary_search(tab, timestamp)
        return tab[index][1] if index >= 0 else ""


# d = TimeMap()
# d.set("a", "a", 1)
# d.set("a", "b", 2)
# d.set("a", "c", 3)
# d.set("a", "d", 4)
# d.set("a", "e", 6)
# d.set("a", "f", 8)
# print(d.get("a", 7))
# print(d.get("b", 20))
