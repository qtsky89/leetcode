# class HitCounter:
#     def __init__(self):
#         self.counter: dict[int, int] = {}
        
#     def hit(self, timestamp: int) -> None:
#         if timestamp in self.counter:
#             self.counter[timestamp] += 1
#         else:
#             self.counter[timestamp] = 1
        

#     def getHits(self, timestamp: int) -> int:
#         total = 0
#         for i in range(timestamp-299, timestamp+1):
#             if i in self.counter:
#                 total += self.counter[i]
        
#         return total

from bisect import bisect_left

class HitCounter:
    def __init__(self):
        self.deque = deque()
    
    # 1, 2, 3, 4, 5, ... 300, 301
    def hit(self, timestamp: int) -> None:
        self.deque.append(timestamp)

        # deque[0] = 1, 301-300 => 1
        while self.deque and self.deque[0] <= timestamp - 300:
            self.deque.popleft()
            
    def getHits(self, timestamp: int) -> int:
        '''
        self.deque = [1, 2, 3, 303]
                                

        '''

        while self.deque and self.deque[0] <= timestamp - 300:
            self.deque.popleft()
    
        return len(self.deque)


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)