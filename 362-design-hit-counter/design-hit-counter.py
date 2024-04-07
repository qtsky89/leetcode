class HitCounter:

    def __init__(self):
        self.counter = deque()

    def hit(self, timestamp: int) -> None:
        self.counter.append(timestamp)
        while self.counter and timestamp - self.counter[0] >= 300:
            self.counter.popleft()
        

    def getHits(self, timestamp: int) -> int:
        while self.counter and timestamp - self.counter[0] >= 300:
            self.counter.popleft()
        
        return len(self.counter)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)