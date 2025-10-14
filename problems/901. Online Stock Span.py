class StockSpanner:

    def __init__(self):
        self.stack = []
        

    def next(self, price: int) -> int:
        c = 1

        stack = self.stack
        
        while stack and price >= stack[-1][0]:
            last_price, count = stack.pop()
            c += count
        
        stack.append(tuple([price,c]))

        return c
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

'''
(85, 6)
(75, 4)
(80, 1)
(100,1)

'''