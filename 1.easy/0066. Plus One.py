# Time Complexity:   O(n)
# Memory Complexity: O(1)

from typing import List


class Solution(object):
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        index = len(digits) - 1
        while index > 0 and digits[index] > 9:
            digits[index - 1], digits[index] = (
                digits[index - 1] + digits[index] // 10,
                digits[index] % 10,
            )
            index -= 1
        return (
            digits
            if digits[0] < 10
            else [digits[0] // 10] + [digits[0] % 10] + digits[1:]
        )


# arr = [9]
# print(Solution().plusOne(arr))
