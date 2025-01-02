class HitCounter:
    def __init__(self):
        self.counter: dict[int, int] = {}
        
    def hit(self, timestamp: int) -> None:
        if timestamp in self.counter:
            self.counter[timestamp] += 1
        else:
            self.counter[timestamp] = 1
        

    def getHits(self, timestamp: int) -> int:
        total = 0
        for i in range(timestamp-299, timestamp+1):
            if i in self.counter:
                total += self.counter[i]
        
        return total
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)