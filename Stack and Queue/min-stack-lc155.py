# page 22
class MinStack:

    def __init__(self):
        self.stack = []
        self.minUntilStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minUntilStack and val > self.minUntilStack[-1]:
            self.minUntilStack.append(self.minUntilStack[-1])
        else:
            self.minUntilStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minUntilStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minUntilStack[-1]
