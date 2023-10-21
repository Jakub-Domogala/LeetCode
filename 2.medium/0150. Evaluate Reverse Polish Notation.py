from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        def perform_calc(a, b, operator):
            if operator == "+":
                return a + b
            if operator == "-":
                return a - b
            if operator == "*":
                return a * b
            if operator == "/":
                return int(a / b)
            print("err")

        for t in tokens:
            if t in operators:
                b = stack.pop()
                a = stack.pop()
                # print("operation: ", a, t, b)
                stack.append(perform_calc(a, b, t))
            else:
                stack.append(int(t))
        return stack[0]


# tokens = ["2", "1", "+", "3", "*"]
# tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
# print(Solution().evalRPN(tokens))
