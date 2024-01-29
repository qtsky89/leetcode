'''

100 80 60 70 60 75  85 ...

1   1   1  2  1  4  6


stack
100 85  
1    6  
'''

# brute force
class StockSpanner:
    def __init__(self):
        self._stack = []

    def next(self, price: int) -> int:
        total = 1
        while self._stack and self._stack[-1][0] <= price:
            stacked_price, count =  self._stack.pop()
            total += count
        
        self._stack.append([price, total])
        return total
        
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)