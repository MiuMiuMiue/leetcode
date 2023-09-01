class MinStack:

    def __init__(self):
        self.minimum = None
        self.stack = []

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append((val, val))
            return
        
        self.stack.append((val, min(self.stack[-1][1], val)))

    def pop(self) -> None:
        return self.stack.pop()[0]

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]

if __name__ == "__main__":
    s = MinStack()
    s.push(0)
    s.push(1)
    s.push(0)
    print(s.getMin())
    s.pop()
    print(s.getMin())
    s.push(-1)
    print(s.getMin())

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()