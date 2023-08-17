# Time Complexity:   O(n)
# Memory Complexity: O(n)

class Solution(object):
    def isValid(self, s: str) -> bool:
        oppenings = ('(', '[', '{')
        closings = (')', ']', '}')

        stack = []
        for e in s:
            if e in oppenings:
                stack.append(e)
            elif e in closings and len(stack) > 0 and stack[-1] in oppenings and closings.index(e) == oppenings.index(stack[-1]):
                stack.pop()
            else:
                return False
        return not stack


# print(Solution().isValid('[][][()])'))
