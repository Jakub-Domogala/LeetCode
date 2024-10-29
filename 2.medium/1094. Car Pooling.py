# Time Complexity:   O(nlogn)
# Memory Complexity: O(n)


from collections import defaultdict
from typing import List

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        changes = defaultdict(int)
        for e in trips:
            changes[e[1]] += e[0]
            changes[e[2]] -= e[0]
        lst = sorted(list(changes.items()))
        for e in lst:
            capacity -= e[1]
            if capacity < 0:
                return False
        return True


trips = [[2,1,5], [3,3,7]]
capacity = 4
result = Solution().carPooling(trips, capacity)
print(result)

trips = [[2,1,5],[3,3,7]]
capacity = 5
result = Solution().carPooling(trips, capacity)
print(result)
