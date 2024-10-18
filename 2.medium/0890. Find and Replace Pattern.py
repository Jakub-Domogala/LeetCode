# Time Complexity:   O(n*m) n=len(words), m=len(pattern)
# Memory Complexity: O(1)


from collections import defaultdict
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def is_isomorphic(s: str, t: str) -> bool:
            translator = {}
            is_present = defaultdict(bool)
            for c1, c2 in zip(s, t):
                if c1 not in translator:
                    if is_present[c2]:
                        return False
                    translator[c1] = c2
                    is_present[c2] = True
                elif translator[c1] == c2:
                    continue
                else:
                    return False
            return True

        result = []
        for w in words:
            if is_isomorphic(w, pattern):
                result.append(w)
        return result

words = ["abc","deq","mee","aqq","dkd","ccc"]
pattern = "abb"
result = Solution().findAndReplacePattern(words, pattern)
print(result)
