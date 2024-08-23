# Time Complexity:   O(max(n**2, n*2**16))
# Memory Complexity: O(2**16)

from typing import List
from collections import defaultdict

class Solution:
    def countTriplets(self, nums: List[int]) -> int:
        '''
        This approach is better than bruteforce only because our constraints are len(nums) <= 1000, nums[i] < 2**16
        Bruteforce: n**3 = 1000 * 1000 * 1000 = 1_000_000_000
        This: n**2 + 2**16 * n = 1_000_000 + 65_536_000 = 66_536_000
        Calculating the complexity we think about 'n' much larger than 1000.
        '''
        a12 = defaultdict(int)
        result = 0
        for n1 in nums:
            for n2 in nums:
                a12[n1 & n2] += 1
        for n12, mul12 in a12.items():
            for n3 in nums:
                if n12 & n3 == 0:
                    result += mul12
        return result

nums = [2,1,3]
result = Solution().countTriplets(nums)
print(result)
