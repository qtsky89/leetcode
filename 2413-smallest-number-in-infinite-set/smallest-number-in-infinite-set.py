from heapq import heapify, heappop, heappush

class SmallestInfiniteSet:
    def __init__(self):
        self._heapq = [i for i in range(1, 1001)]
        heapify(self._heapq)
        self._set = set([i for i in range(1, 1001)])
        
    def popSmallest(self) -> int:
        tmp = heappop(self._heapq)
        self._set.remove(tmp)
        return tmp
        
    def addBack(self, num: int) -> None:
        if num in self._set:
            return

        heappush(self._heapq, num)
        self._set.add(num)

        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)