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
        self._stocks = []

    def next(self, price: int) -> int:
        self._stocks.append(price)

        for i in range(len(self._stocks)-1, -1, -1):
            if self._stocks[i] > price:
                return (len(self._stocks)-1 -i)
        
        return len(self._stocks)


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)