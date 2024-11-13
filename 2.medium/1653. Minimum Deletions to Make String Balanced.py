 # Time Complexity:   O(n)
 # Memory Complexity: O(n) could be made O(1)


from math import inf

class Solution:
    def minimumDeletions(self, s: str) -> int:
        if s.count("a") < s.count("b"):
            s = "".join(s.replace("b", "c").replace("a", "b").replace("c", "a")[::-1])

        top_a = -inf # -len(s)-1 would work too
        top_idx = None
        curr_val = 0
        for i in range(len(s)):
            if s[i] == "a":
                curr_val += 1
                if curr_val > top_a:
                    top_a = curr_val
                    top_idx = i
            else:
                curr_val -= 1
        if top_idx is None:
            return 0
        result = 0
        for i in range(top_idx):
            if s[i] == "b":
                result += 1
        for i in range(top_idx+1, len(s)):
            if s[i] == "a":
                result += 1
        return result



# s = "aababbab"
# print(Solution().minimumDeletions(s), 2)

# s = "bbaaaaaaaaabb"
# print(Solution().minimumDeletions(s), 2)

# s = "bbbbbbbaabbbbbaaabbbabbbbaabbbbbbaabbaaabaabbbaaaabaaababbbabbabbaaaabbbabbbbbaabbababbbaaaaaababaaababaabbabbbaaaabbbbbabbabaaaabbbaba"
# print(Solution().minimumDeletions(s), 60)
# print(s.count("a"), s.count("b"))
