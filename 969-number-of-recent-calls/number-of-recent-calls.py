from collections import deque

class RecentCounter:
    def __init__(self):
        self._queue = deque()
                            
    #  t       1  100  3001 3002
    # return   1    2    3    3

    def ping(self, t: int) -> int:
        # queue's fist data is out of range
        while self._queue and (t -  3000) > self._queue[0]:
            self._queue.popleft()            
        self._queue.append(t)
        return len(self._queue)
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)