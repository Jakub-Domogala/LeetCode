# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i, e in enumerate(timeSeries):
            if i == 0:
                continue
            total += min(e - timeSeries[i-1], duration)
        return total + duration

# timeSeries = [1,4]
# duration = 2
# result = Solution().findPoisonedDuration(timeSeries, duration)
# print(result)
# timeSeries = [1,2]
# duration = 2
# result = Solution().findPoisonedDuration(timeSeries, duration)
# print(result)
