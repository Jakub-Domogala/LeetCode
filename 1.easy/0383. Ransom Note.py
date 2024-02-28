# Time Complexity:   O(n)
# Memory Complexity: O(1)
# where n is len(magazine)

from collections import defaultdict


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag = defaultdict(int)
        for letter in magazine:
            mag[letter] += 1

        for letter in ransomNote:
            if mag[letter] >= 1:
                mag[letter] -= 1
            else:
                return False
        return True
