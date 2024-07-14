class MinStack:

    def __init__(self):
        self.items = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.items.append(val)
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.items:
            popped = self.items.pop()
            if self.minStack and popped == self.minStack[-1]:
                self.minStack.pop()
        
    def top(self) -> int:
        if self.items:
            return self.items[-1]
        return -1

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return -1

        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
