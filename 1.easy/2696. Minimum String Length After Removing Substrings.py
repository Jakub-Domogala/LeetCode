# Time Complexity:   O(n)
# Memory Complexity: O(n)


class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        stack_size = 0
        for i in range(len(s)):
            if stack_size > 0 and ((s[i] == "B" and stack[-1] == "A") or (s[i] == "D" and stack[-1] == "C")):
                stack.pop()
                stack_size -= 1
            else:
                stack.append(s[i])
                stack_size += 1
        return stack_size

    # def minLength(self, s: str) -> int: # Bruteforce O(n^2)
    #     is_modified = True
    #     while is_modified:
    #         i = 0
    #         is_modified = False
    #         while i < len(s)-1:
    #             if (s[i] == "A" and s[i+1] == "B") or (s[i] == "C" and s[i+1] == "D"):
    #                 s = s[0:i] + s[i+2:len(s)]
    #                 is_modified = True
    #             else:
    #                 i += 1
    #     return len(s)

# s = "ABFCACDB"
# result = Solution().minLength(s)
# print(result)
