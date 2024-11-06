from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        all_edges = [[] for _ in range(n)]
        for e in edges:
            all_edges[e[0]].append(e[1])
            all_edges[e[1]].append(e[0])
        def dfs_find(E, source, dest):
            def dive(curr, dest):
                nonlocal visited, E
                if curr == dest:
                    return True
                visited[curr] = True
                for nei in E[curr]:
                    if not visited[nei]:
                        if dive(nei, dest):
                            return True
                return False
            visited = [False] * len(E)
            return dive(source, destination)
        return dfs_find(all_edges, source, destination)


n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(Solution().validPath(n, edges, source, destination), True)
n = 4
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 3
print(Solution().validPath(n, edges, source, destination), True)
