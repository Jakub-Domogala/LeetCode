# Time Complexity:   O(n + len(trust))
# Memory Complexity: O(n)


from typing import List
from collections import defaultdict

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_to, trust_from = [0]*n, [0]*n
        for t in trust:
            trust_to[t[0]-1] += 1
            trust_from[t[1]-1] += 1
        trusted_by_all = None
        for i, e in enumerate(trust_from):
            if e == n-1 and trust_to[i] == 0:
                if trusted_by_all is not None:
                    return -1
                trusted_by_all = i + 1
        return -1 if trusted_by_all is None else trusted_by_all


# n = 2
# trust = [[1,2]]
# result = Solution().findJudge(n, trust)
# print(result)
# n = 3
# trust = [[1,3],[2,3]]
# result = Solution().findJudge(n, trust)
# print(result)
# n = 3
# trust = [[1,3],[2,3],[3,1]]
# result = Solution().findJudge(n, trust)
# print(result)
