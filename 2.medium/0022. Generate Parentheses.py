# Time Complexity:   O(2^n)
# Memory Complexity: O(2^n)
# Where 2^n is size of the solution

class Solution(object):
    def generateParenthesis(self, n):
        def go_next(c_open=0, c_close=0):
            if n == c_open == c_close:
                return [""]

            r1, r2 = [], []

            # add oppening if there are any left
            r1 = ["(" + s for s in go_next(c_open + 1, c_close)] if c_open < n else r1

            # add closing if it would be correct
            r2 = [")" + s for s in go_next(c_open, c_close + 1)] if c_open > c_close else r2
            
            return r1 + r2

        return go_next()


print(Solution().generateParenthesis(3))
