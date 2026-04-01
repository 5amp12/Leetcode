class MyStack:

    def __init__(self):
       self.stack = [] 

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for i in range(len(self.stack)-1):
            self.stack.append(self.stack[0])
            self.stack.pop(0)
        return self.stack.pop(0)

    def top(self) -> int:
        top = self.stack[len(self.stack)-1]
        return top

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()