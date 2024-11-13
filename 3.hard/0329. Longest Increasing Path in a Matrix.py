from typing import List
# from queue import PriorityQueue

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        moves = [(0,1),(1,0),(0,-1),(-1,0)]
        rows, cols = len(matrix), len(matrix[0])
        dp =[[0] * cols for i in range(rows)]
        def dfs(vx, vy):
            if not dp[vx][vy]:
                dp[vx][vy] = 1 + max(
                    [dfs(vx + mx, vy + my)
                        if (
                            0 <= vx+mx < rows
                            and 0 <= vy+my < cols
                            and matrix[vx][vy] > matrix[vx+mx][vy+my])
                        else 0 for mx, my in moves]
                    )
            return dp[vx][vy]
        _ = [dfs(x, y) for x in range(rows) for y in range(cols)]
        return max(max(x) for x in dp)
    # def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # def find_longest_inc_path_from(start): # dijkstra approach, same complexity but much more constant overhang
        #     moves = [(0,1),(1,0),(0,-1),(-1,0)]
        #     def is_valid_next(nx, ny):
        #         return 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0])
        #     def has_smaller_nei(v):
        #         vx, vy = v
        #         for mx, my in moves:
        #             nx, ny = vx + mx, vy + my
        #             if is_valid_next(nx, ny) and matrix[vx][vy] > matrix[nx][ny]:
        #                 return True
        #         return False
        #     if has_smaller_nei(start):
        #         return 0
        #     d = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        #     q = PriorityQueue() # (-dist, matrix[v], v)
        #     q.put((-1, matrix[start[0]][start[1]], start))
        #     top_length = 1
        #     while not q.empty():
        #         curr_d, _, v = q.get()
        #         curr_d = -curr_d
        #         vx, vy = v
        #         for mx, my in moves:
        #             nx, ny = vx + mx, vy + my
        #             if is_valid_next(nx, ny) and matrix[vx][vy] < matrix[nx][ny] and curr_d + 1 > d[nx][ny]:
        #                 d[nx][ny] = curr_d + 1
        #                 q.put((-curr_d-1, matrix[nx][ny], (nx, ny)))
        #                 top_length = max(top_length, curr_d + 1)
        #     return top_length
        # return max([find_longest_inc_path_from((x,y)) for x in range(len(matrix)) for y in range(len(matrix[0]))])

matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(Solution().longestIncreasingPath(matrix), 4)
matrix = [[13,6,16,6,16,4],[9,13,5,13,7,11],[11,7,9,17,0,7],[7,8,5,14,11,8],[14,2,8,7,9,5],[1,15,3,11,11,6]]
print(Solution().longestIncreasingPath(matrix), 6)
