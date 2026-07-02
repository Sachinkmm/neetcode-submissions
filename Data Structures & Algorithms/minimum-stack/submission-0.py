class MinStack:

    def __init__(self):
        self.st = []
        self.mini = 0

    def push(self, val: int) -> None:
        if not self.st:
            self.mini = val
        elif self.mini > val:
            nmini = val
            val = 2 * val - self.mini
            self.mini = nmini
        self.st.append(val)

    def pop(self) -> None:
        if self.st[-1] < self.mini:
            self.mini = 2 * self.mini - self.st[-1]
        self.st.pop()

    def top(self) -> int:
        if self.st[-1] < self.mini:
            return self.mini
        return self.st[-1]

    def getMin(self) -> int:
        return self.mini
