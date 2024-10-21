# Time Complexity:   O(n+m)
# Memory Complexity: O(n)
# n = len(s)
# m = len(pattern)


from collections import defaultdict

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_arr = s.split(" ")
        if len(s_arr) != len(pattern):
            return False
        translator = {}
        is_present = defaultdict(bool)
        for word, ch in zip(s_arr, pattern):
            if word not in translator:
                if is_present[ch]:
                    return False
                translator[word] = ch
                is_present[ch] = True
            elif translator[word] == ch:
                continue
            else:
                return False
        return True

# pattern = "abba"
# s = "dog cat cat dog"
# result = Solution().wordPattern(pattern, s)
# print(result)

# pattern = "abba"
# s = "dog cat cat fish"
# result = Solution().wordPattern(pattern, s)
# print(result)

# pattern = "aaaa"
# s = "dog cat cat dog"
# result = Solution().wordPattern(pattern, s)
# print(result)
