# Time Complexity:   O(n * m)
# Memory Complexity: O(n * m)

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        que = []
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        fresh_counter = 0
        options = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def is_in_range(x, y):
            return 0 <= x < n and 0 <= y < m

        # prepare first round of queue
        for y in range(m):
            for x in range(n):
                if grid[y][x] == 1:
                    fresh_counter += 1
                elif grid[y][x] == 2:
                    que.append((x, y))
        minutes_passed = 0
        que = [que]
        while fresh_counter > 0:
            if len(que[minutes_passed]) == 0:
                return -1
            que.append([])
            for x, y in que[minutes_passed]:
                if grid[y][x] == 2:
                    for ox, oy in options:
                        nx, ny = x + ox, y + oy
                        if is_in_range(nx, ny) and grid[ny][nx] == 1:
                            grid[ny][nx] = 2
                            que[minutes_passed + 1].append((nx, ny))
                            fresh_counter -= 1
            minutes_passed += 1
        return minutes_passed


# grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
# grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
# print(Solution().orangesRotting(grid))
