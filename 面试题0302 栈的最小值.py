class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min = float("inf")


    def push(self, x: int) -> None:
        self.stack.append(x)
        if x < self.min:
            self.min = x

    def pop(self) -> None:
        if len(self.stack) > 0:
            self.stack.pop(-1)
        return

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min