# Time Complexity:   O(n)
# Memory Complexity: O(1)


from typing import List

class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        cnt = 0
        n = len(words)
        while words[(startIndex+cnt)%n] != target and words[startIndex-cnt] != target:
            cnt += 1
            if cnt == n//2 + 1:
                return -1
        return cnt

# words = ["hello","i","am","leetcode","hello"]
# target = "hello"
# startIndex = 1
# result = Solution().closetTarget(words, target, startIndex)
# print(result)
