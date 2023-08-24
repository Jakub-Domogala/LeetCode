# Time Complexity:   O(n^2)
# Memory Complexity: O(n^2)
# Where n is length of side (default 9 for standard 9x9 sudoku)

from collections import defaultdict
from typing import List, Dict


class Solution(object):
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        side_size = len(board)
        part_size = int(side_size**0.5)
        
        def memorize(nums: Dict[int, int], x: int, y: int) -> bool:
            value = -1 if board[x][y] == '.' else int(board[x][y])
            if value == -1:
                return True
            nums[value] += 1
            if value > 0 and nums[value] > 1:
                return False
            return True

        def check_square(x: int, y: int) -> bool:
            nums = defaultdict(int)
            for ix in range(x, x+part_size):
                for iy in range(y, y+part_size):
                    if not memorize(nums, ix, iy):
                        return False
            return True
                    
        def check_line_horizontal(y: int) -> bool:
            nums = defaultdict(int)
            for x in range(side_size):
                if not memorize(nums, x, y):
                    return False
            return True
                
        def check_line_vertical(x: int) -> bool:
            nums = defaultdict(int)
            for y in range(side_size):
                if not memorize(nums, x, y):
                    return False
            return True
        
        for i in range(side_size):
            if (
                not check_square(i//part_size * part_size, i%part_size * part_size) or
                not check_line_horizontal(i) or
                not check_line_vertical(i)
            ):
                return False
        return True
        
# good_board = [
#     ["5","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]]

# bad_board = [
#     ["8","3",".",".","7",".",".",".","."],
#     ["6",".",".","1","9","5",".",".","."],
#     [".","9","8",".",".",".",".","6","."],
#     ["8",".",".",".","6",".",".",".","3"],
#     ["4",".",".","8",".","3",".",".","1"],
#     ["7",".",".",".","2",".",".",".","6"],
#     [".","6",".",".",".",".","2","8","."],
#     [".",".",".","4","1","9",".",".","5"],
#     [".",".",".",".","8",".",".","7","9"]]
# print(Solution().isValidSudoku(bad_board))