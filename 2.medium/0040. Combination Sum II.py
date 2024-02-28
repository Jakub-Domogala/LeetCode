# Time Complexity:   O(target)
# Memory Complexity: O(target)
# NOTE: Negative numbers are not considered in this solution

from typing import List


class Solution(object):
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def rec(candidates, sum=0):
            if sum == target:
                return [[]]
            if len(candidates) == 0 or sum + candidates[0] > target:
                return []
            result = []
            result += [
                [candidates[0]] + result
                for result in rec(candidates[1:], sum + candidates[0])
            ]
            result += rec([elem for elem in candidates if elem != candidates[0]], sum)
            return result

        return rec(sorted(candidates))


# print(Solution().combinationSum([10,1,2,7,6,1,5], 8))
