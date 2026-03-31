class MinStack:

    def __init__(self):
        self.st=[]
        self.min_stack=[]

    def push(self, val: int) -> None:
        self.st.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.st:
            val = self.st.pop()
            if val == self.min_stack[-1]:
                self.min_stack.pop()
    def top(self) -> int:
        return self.st[-1] if self.st else None
    def getMin(self) -> int:
        return self.min_stack[-1] if self.min_stack else None