# Time Complexity:   O(n^2)
# Memory Complexity: O(1)

from typing import List


class Solution(object):
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # flip along [n][0] - [0][n] line
        def flip_across():
            for i in range(n):
                for j in range(n - i - 1):
                    matrix[i][j], matrix[n - j - 1][n - i - 1] = (
                        matrix[n - j - 1][n - i - 1],
                        matrix[i][j],
                    )

        # flip along [n//2][0] - [n//2][n] line
        def flip_vertically():
            for i in range(n // 2):
                for j in range(n):
                    matrix[i][j], matrix[n - i - 1][j] = (
                        matrix[n - i - 1][j],
                        matrix[i][j],
                    )

        flip_across()
        flip_vertically()

    def pprint(self, matrix):
        for row in matrix:
            print(row)
        print()


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().pprint(matrix)
Solution().rotate(matrix)
Solution().pprint(matrix)
