# Time Complexity:   O(amount * coins)
# Memory Complexity: O(amount)

from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins = sorted(coins)

        # dynamic[amount] how many coins do you need for given amount
        dynamic = [inf for i in range(amount + 1)]
        dynamic[0] = 0
        for i in range(1, len(dynamic)):
            for value in coins:
                if i - value >= 0:
                    dynamic[i] = min(dynamic[i - value] + 1, dynamic[i])
        return dynamic[amount] if dynamic[amount] != inf else -1


# coins = [1, 2, 5]
# amount = 11
# print(Solution().coinChange(coins, amount))
