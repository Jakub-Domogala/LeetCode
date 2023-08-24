# Time Complexity:   O(target)
# Memory Complexity: O(target)
# NOTE: Negative numbers are not considered in this solution

from typing import List


class Solution(object):
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def rec(candidates, sum = 0):
            if sum == target:
                return [[]]
            if len(candidates) == 0 or sum + candidates[0] > target:
                return []
            result = []
            result += [[candidates[0]] + result for result in rec(candidates, sum + candidates[0])]
            result += rec(candidates[1:], sum)
            return result
        return rec(sorted(candidates))
    
# print(Solution().combinationSum([2,3,5], 8))
            
