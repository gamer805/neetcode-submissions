class MinStack:

    def __init__(self):
        self.stack = []
        self.minvals = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minvals) == 0:
            self.minvals.append(val)
        else:
            self.minvals.append(min(self.minvals[-1], val))



    def pop(self) -> None:
        self.stack.pop()
        self.minvals.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minvals[-1]
