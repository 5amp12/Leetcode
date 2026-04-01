class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.revStack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if len(self.revStack2) == 0:
            for i in range(len(self.stack1)):
                self.revStack2.append(self.stack1.pop(len(self.stack1)-1))
        return self.revStack2.pop(len(self.revStack2)-1)

    def peek(self) -> int:
        if len(self.revStack2) == 0:
            for i in range(len(self.stack1)):
                self.revStack2.append(self.stack1.pop(len(self.stack1)-1))
        return self.revStack2[len(self.revStack2)-1]

    def empty(self) -> bool:
        if self.revStack2 == [] and self.stack1 == []:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()