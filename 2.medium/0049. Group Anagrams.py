# Time Complexity:   O(n*mlogm)
# Memory Complexity: O(n*m)
# where n = len(strs), m = len(strs[i])


from typing import List
from collections import defaultdict


class Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]: O(n*m), O(n*m) but slower in leet code
    #     def get_idx(c):
    #         return ord(c) - ord("a")
    #     n = len(strs)
    #     counts = [[strs[i], [0 for j in range(ord("z")-ord("a") + 1)]] for i in range(n)]
    #     groups = defaultdict(list)
    #     for i, e in enumerate(strs):
    #         for c in e:
    #             counts[i][1][get_idx(c)] += 1
    #         groups[' '.join(map(str, counts[i][1]))].append(counts[i][0])
    #     return [val for _, val in groups.items()]

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            groups["".join(sorted(s))] += [s]
        return list(groups.values())


# strs = ["eat","tea","tan","ate","nat","bat"]
# result = Solution().groupAnagrams(strs)
# print(result)
