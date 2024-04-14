'''
    dict =  {
        2: 'google',
        3: 'bloomberg'
    }

    list = [3, 2]
               ^
'''

class LRUCache:
    def __init__(self, capacity: int):
        self.dict: dict[int, int] = {}
        self.deque: deque[int] = deque()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        
        value = self.dict[key]
        
        self.deque.remove(key)
        self.deque.append(key)

        return value

    def put(self, key: int, value: int) -> None:
        # update
        if key in self.dict:
            self.dict[key] = value
            self.deque.remove(key)
            self.deque.append(key)
        else:
            # create
            self.dict[key] = value
            self.deque.append(key)
            if len(self.deque) > self.capacity:
                k = self.deque.popleft()
                del self.dict[k]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)