'''
    s = SmallestInfiniteSet()

    print(s.popSmallest()) -> 1
    print(s.popSmallest()) -> 2
    print(s.popSmallest()) -> 3
    print(s.popSmallest()) -> 2
    print(s.popSmallest()) -> 4
    ...

    
'''


class SmallestInfiniteSet:
    def __init__(self):
        self._min_heap = [ i for i in range(1, 1001)]
        heapq.heapify(self._min_heap)
        self._set = set([ i for i in range(1, 1001)])
        
    def popSmallest(self) -> int:
        ret = heapq.heappop(self._min_heap)
        self._set.remove(ret)
        return ret
        

    def addBack(self, num: int) -> None:
        if num in self._set:
            return
        self._set.add(num)
        heapq.heappush(self._min_heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)