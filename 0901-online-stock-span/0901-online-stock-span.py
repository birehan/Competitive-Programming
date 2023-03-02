class StockSpanner:

    def __init__(self):
        self.stack = []
        self.index = 0
        
    def next(self, price: int) -> int:
        index = self.index
        while self.stack and self.stack[-1][0] <= price:
            index = self.stack.pop()[1]

        self.stack.append((price, index))
        self.index += 1
        return self.index - index
        
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)