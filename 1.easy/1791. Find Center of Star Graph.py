# Time Complexity:   O(1)
# Memory Complexity: O(1)


from typing import List
from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return edges[0][0] if edges[0][0] in edges[1] else edges[0][1]

    # def findCenter(self, edges: List[List[int]]) -> int: # time O(n), mem O(n). Approach where we count middle as vert with most connections
    #     E = defaultdict(list)
    #     for a, b in edges:
    #         E[a].append(b)
    #         E[b].append(a)
    #     most_con_id = None
    #     con_count = 0
    #     for v in E.keys():
    #         if len(E[v]) > con_count:
    #             most_con_id = v
    #             con_count = len(E[v])
    #     return most_con_id

edges = [[1,2],[2,3],[4,2]]
print(Solution().findCenter(edges))
