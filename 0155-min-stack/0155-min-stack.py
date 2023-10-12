class MinStack:
    def __init__(self):
        self.stack = []
        self.dec_stack = []
        self.index = 0

    def push(self, val: int) -> None:
        self.stack.append((val, self.index))
        if not self.dec_stack or self.dec_stack[-1][0] > val:
            self.dec_stack.append((val, self.index))
        
        self.index += 1

    def pop(self) -> None:
        if self.stack[-1][1] == self.dec_stack[-1][1]:
            self.dec_stack.pop()
        self.stack.pop()
        
    def top(self) -> int:
        return self.stack[-1][0]
        
    def getMin(self) -> int:
        return self.dec_stack[-1][0]