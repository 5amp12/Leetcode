class StockSpanner:

    def __init__(self):
        self.stack = []  #[num, value]

    def next(self, price: int) -> int:
        value = 1
        while self.stack and price >= self.stack[-1][0]:
            value += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, value])
        print(self.stack)
        return value
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)