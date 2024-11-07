# Time Complexity:   O(n)
# Memory Complexity: O(n)
#
# Leetcode score runtime 100%, memory 68.21%
#
# Could be further improved by instead of using the groups array just scan the 0's on the go
# This would make memory complexity O(1) but could potentially make it run x2 slower (still O(n) runtime)
# cause of performing scan on each element 2 times, one for each side of the sliding window.


from typing import List

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def get_0_combinations(size):
            return int(((size+1)/2)*size if size > 0 else 0)
        groups = [1]
        prev = None
        for e in nums:
            if e == 0:
                groups[-1] += 1
            else:
                groups.append(1)
        result = 0
        if goal > 0:
            n = len(groups)
            il, ir = 0, goal
            while ir < n:
                result += groups[il] * groups[ir]
                il += 1
                ir += 1
        else:
            for e in groups:
                result += get_0_combinations(e-1)
        return result

# nums = [1,0,1,0,1]
# goal = 2
# print(Solution().numSubarraysWithSum(nums, goal))
# nums = [1,0,0,1,0,1,1]
# goal = 2
# print(Solution().numSubarraysWithSum(nums, goal))
