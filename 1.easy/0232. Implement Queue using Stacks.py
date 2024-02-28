# Time Complexity:   O(1)
# Memory Complexity: O(n)
# as mentioned in the task complexity of n tasks is n even if one operation may take longer


class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        self.stack_in.append(x)

    def pop(self) -> int:
        if len(self.stack_out) == 0:
            self.prepare_stack_out()
        if len(self.stack_out) > 0:
            return self.stack_out.pop()
        return None

    def peek(self) -> int:
        if len(self.stack_out) == 0:
            self.prepare_stack_out()
        if len(self.stack_out) > 0:
            return self.stack_out[-1]
        return None

    def empty(self) -> bool:
        return len(self.stack_in) + len(self.stack_out) == 0

    def prepare_stack_out(self):
        while len(self.stack_in) > 0:
            self.stack_out.append(self.stack_in.pop())
