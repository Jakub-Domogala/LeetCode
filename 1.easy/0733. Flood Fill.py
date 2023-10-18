from typing import List
from queue import Queue


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        def is_valid(a, b):
            return (
                0 <= a < len(image)
                and 0 <= b < len(image[0])
                and image[a][b] != color
                and image[a][b] == prev
            )

        options = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        que = []
        que.append((sr, sc, image[sr][sc]))
        image[sr][sc] = color
        while len(que) > 0:
            a, b, prev = que.pop(0)
            for opt in options:
                na, nb = a + opt[0], b + opt[1]
                if is_valid(na, nb):
                    que.append((na, nb, prev))
                    image[na][nb] = color
        return image


print(Solution().floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
