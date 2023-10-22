# Time Complexity:   O(E + V)
# Memory Complexity: O(E + V)

from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # prepare graph edges representation
        neigh_graph = {index: [] for index in range(numCourses)}
        for pre in prerequisites:
            neigh_graph[pre[0]].append(pre[1])

        # check graph for cycles
        return not self.hasCycle(neigh_graph)

    def isCyclicUtil(self, v, graph, visited, recStack):
        visited[v] = True
        recStack[v] = True

        for neighbor in graph[v]:
            if visited[neighbor] == False:
                if self.isCyclicUtil(neighbor, graph, visited, recStack):
                    return True
            elif recStack[neighbor]:
                return True

        recStack[v] = False
        return False

    def hasCycle(self, graph):
        num_nodes = len(graph)
        visited = [False] * num_nodes
        recStack = [False] * num_nodes

        for i in range(num_nodes):
            if visited[i] == False:
                if self.isCyclicUtil(i, graph, visited, recStack):
                    return True

        return False


numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(Solution().canFinish(numCourses, prerequisites))
