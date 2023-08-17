# Time Complexity:   O(n * m)
# Memory Complexity: O(m)
# Where m is size of shortest word


from typing import List


class Solution(object):
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for position in range(min(list(map(lambda word: len(word), strs)))):
            for i in range(len(strs) - 1):
                if strs[i][position] != strs[i + 1][position]:
                    return result
            result += strs[0][position]
        return result


# # expected 'fl'
# print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
# # expected ''
# print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
