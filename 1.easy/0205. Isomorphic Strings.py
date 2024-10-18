# Time Complexity:   O(n)
# Memory Complexity: O(1) Only 2xdict of size 256 at most


from collections import defaultdict


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
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

# s = "egg"
# t = "add"
# result = Solution().isIsomorphic(s, t)
# print(result, True)
# s = "foo"
# t = "bar"
# result = Solution().isIsomorphic(s, t)
# print(result, False)
# s = "paper"
# t = "title"
# result = Solution().isIsomorphic(s, t)
# print(result, True)
# s = "badc"
# t = "baba"
# result = Solution().isIsomorphic(s, t)
# print(result, True)
