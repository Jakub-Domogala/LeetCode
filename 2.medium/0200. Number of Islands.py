# Time Complexity:   O(m * n)
# Memory Complexity: O(m * n)
# where m, n are dimension sizes of grid

from collections import deque
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        land = "1"
        lenY = len(grid)
        if lenY == 0:
            return 0
        lenX = len(grid[0])
        visited = [[False for _ in range(lenX)] for _ in range(lenY)]

        def is_in_range(x, y):
            return 0 <= x < lenX and 0 <= y < lenY

        def explore_island_bfs(x, y):
            options = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            que = deque()
            que.append((x, y))
            visited[y][x] = True
            while que:
                x, y = que.popleft()
                for ox, oy in options:
                    nx, ny = x + ox, y + oy
                    if (
                        is_in_range(nx, ny)
                        and not visited[ny][nx]
                        and grid[ny][nx] == land
                    ):
                        visited[ny][nx] = True
                        que.append((nx, ny))

        counter = 0
        for x in range(lenX):
            for y in range(lenY):
                if grid[y][x] == land and not visited[y][x]:
                    explore_island_bfs(x, y)
                    counter += 1
        return counter


# grid = [
#     ["1", "1", "1", "1", "0"],
#     ["1", "1", "0", "1", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "0", "0", "0"],
# ]
# grid = [
#     ["1", "1", "0", "0", "0"],
#     ["1", "1", "0", "0", "0"],
#     ["0", "0", "1", "0", "0"],
#     ["0", "0", "0", "1", "1"],
# ]
# print(Solution().numIslands(grid))
