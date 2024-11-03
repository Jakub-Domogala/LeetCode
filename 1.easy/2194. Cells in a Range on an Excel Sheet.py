from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        result = []
        for i in range(ord(s[0]), ord(s[3]) + 1):
            for j in range(int(s[1]), int(s[4])+1):
                result.append(chr(i) + str(j))
        return result

s = "A1:F1"
print(Solution().cellsInRange(s))
