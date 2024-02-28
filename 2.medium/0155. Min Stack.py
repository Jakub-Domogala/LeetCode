# Time Complexity:   O(1) for each function
# Memory Complexity: O(n) for n elements in stack

from math import inf


class MinStack:
    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        last_min = self.stack[-1][1] if len(self.stack) > 0 else inf
        self.stack.append((val, min(val, last_min)))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]


# s = MinStack()
# s.push(3)
# s.push(2)
# s.push(4)
# print(s.top())
# print(s.getMin())
# s.pop()
# print(s.top())
# print(s.getMin())
