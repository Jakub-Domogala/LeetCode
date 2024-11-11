# Time Complexity:   O(n)
# Memory Complexity: O(n)


from typing import List
from collections import defaultdict

class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        E, balance = defaultdict(list), defaultdict(int)
        balance = defaultdict(int)
        n = len(pairs)
        for x, y in pairs:
            E[x].append(y)
            balance[y] += 1
            balance[x] -= 1
        start = [x for x, y in balance.items() if y == -1]
        start = start[0] if len(start) > 0 else pairs[0][0]
        result = []
        def dfs_travel_all_edges(u):
            while E[u]:
                v = E[u].pop()
                dfs_travel_all_edges(v)
                result.append((u,v))
        dfs_travel_all_edges(start)
        return result[::-1]

# pairs = [[5,1],[4,5],[11,9],[9,4]]
# result = Solution().validArrangement(pairs)
# print("Pairs:  ",pairs)
# print("Result: ",result)
# pairs = [[1,3],[3,2],[2,1]]
# result = Solution().validArrangement(pairs)
# print("Pairs:  ",pairs)
# print("Result: ",result)
