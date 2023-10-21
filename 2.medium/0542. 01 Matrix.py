# Time Complexity:   O(n * m)
# Memory Complexity: O(n * m)
# Where n, m are dimension lengths

from collections import deque
from typing import List
from math import inf


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        lenX, lenY = len(mat[0]), len(mat)
        X, Y = range(lenX), range(lenY)
        que = deque()
        dist = [[inf for _ in X] for _ in Y]
        options = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_in_range(x, y):
            return 0 <= x < lenX and 0 <= y < lenY

        for x in X:
            for y in Y:
                if mat[y][x] == 0:
                    dist[y][x] = 0
                    que.append((x, y))

        while que:
            x, y = que.popleft()
            for ox, oy in options:
                nx, ny = x + ox, y + oy
                if is_in_range(nx, ny) and dist[ny][nx] > dist[y][x] + 1:
                    dist[ny][nx] = dist[y][x] + 1
                    que.append((nx, ny))

        return dist


# mat = [
#     [0, 0, 1, 0, 1, 1, 1, 0, 1, 1],
#     [1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
#     [1, 0, 1, 0, 1, 1, 1, 0, 1, 1],
#     [0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
#     [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
#     [0, 1, 0, 0, 0, 1, 0, 0, 1, 1],
#     [1, 1, 1, 0, 1, 1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1, 0, 1, 1, 1, 0],
# ]

# res = Solution().updateMatrix(mat)
# for row in res:
#     print(row)
