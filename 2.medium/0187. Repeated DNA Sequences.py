from typing import List
from collections import defaultdict


class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        sequence_count = defaultdict(int)
        for i in range(len(s) - 9):
            sequence = s[i:i+10]
            sequence_count[sequence] += 1
        return [seq for seq, count in sequence_count.items() if count > 1]
        # return [seq for seq, count in sequence_count.items() if count > 0]

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
result = Solution().findRepeatedDnaSequences(s)
print(result)
