# Time Complexity:   approx O(log(high) - log(low))
# Memory Complexity: approx O(log(high) - log(low))
# Both are pretty complex to calculate so I will leave it as it is

from typing import List
from math import log10, floor


class Solution(object):
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        if low > high or log10(low) > 9:
            return []
        high = min(high, 999999999)

        result = []
        previous_num = low
        num_len = floor(log10(low)) + 1
        dec2str = {x: str(x) for x in range(1, 10)}
        str2dec = {str(x): x for x in range(1, 10)}
        while previous_num <= high:
            if previous_num == low and len(result) == 0:
                number = str(low)[0]
            elif log10(previous_num) + 1 >= num_len:
                number = chr(ord(str(previous_num)[0]) + 1)
            else:
                number = "1"
            if str2dec[number[0]] + num_len > 10:
                num_len += 1
                number = "1"
            if num_len > 9:
                return result
            while len(number) < num_len:
                number += dec2str[str2dec[number[-1]] + 1]

            previous_num = int(number)
            if previous_num > high:
                return result
            if previous_num >= low:
                result.append(previous_num)
        return result


# print(Solution().sequentialDigits(234, 2314))
