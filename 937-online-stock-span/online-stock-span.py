'''
example1.        
    100 80 60 70 60 75 85 ...
     1   1  1  2  1  4 6

stack = [100, 1] [85, 6] 
'''


class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        total = 1
        while self.stack and self.stack[-1][0]  <= price:
            _, span = self.stack.pop()
            total += span
        
        self.stack.append([price, total])

        return total
        
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)