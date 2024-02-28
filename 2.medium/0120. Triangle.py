from math import inf
from typing import List


def print_triangle(tri):
    size = len(tri)
    for i, row in enumerate(tri):
        print(" " * 2 * (size - i), end="")
        for elem in row:
            print("{:^3}".format(elem), "", end="")
        print()


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        results = [[inf for _ in row] for row in triangle]
        results[0][0] = triangle[0][0]

        for i in range(len(triangle) - 1):
            for j in range(len(triangle[i])):
                for other in range(2):
                    results[i + 1][j + other] = min(
                        results[i + 1][j + other],
                        results[i][j] + triangle[i + 1][j + other],
                    )

        # print("Input triangle")
        # print_triangle(triangle)
        # print()
        # print("Best Paths")
        # print_triangle(results)

        return min(results[-1])


triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
print(Solution().minimumTotal(triangle))
