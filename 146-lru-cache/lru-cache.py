class DoubleLinkedListNode:
    def __init__(self, key: int = None, val: int = None, prev: 'DoubleLinkedListNode' = None, next: 'DoubleLinkedListNode' = None) -> None:
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self) -> None:
        self.front = DoubleLinkedListNode()
        self.back = DoubleLinkedListNode()

        self.front.next = self.back
        self.back.prev = self.front
    
    def add_back(self, target: DoubleLinkedListNode) -> None:
        self.back.prev.next, target.prev, target.next, self.back.prev  = target, self.back.prev, self.back, target
    
    def delete_target(self, target: DoubleLinkedListNode) -> None:
        target.prev.next, target.next.prev = target.next, target.prev

class LRUCache:
    def __init__(self, capacity: int):
        self._cache_map: dict[int, DoubleLinkedListNode] = {}
        self._priotize_list: DoubleLinkedList = DoubleLinkedList()
        self._capacity = capacity

    def get(self, key: int) -> int:
        if key not in self._cache_map:
            return -1
        
        target = self._cache_map[key]
        
        # remove
        self._priotize_list.delete_target(target)
        self._priotize_list.add_back(target)

        return target.val

    def put(self, key: int, value: int) -> None:
        # update
        if key in self._cache_map:
            target = self._cache_map[key]
            target.val = value
            target.prev.next, target.next.prev = target.next, target.prev
            self._priotize_list.add_back(target)
        else: # create
            target = DoubleLinkedListNode(key, value)
            self._priotize_list.add_back(target)
            self._cache_map[key] = target

            if len(self._cache_map) > self._capacity:
                # remove least recently used node
                target = self._priotize_list.front.next
                self._priotize_list.delete_target(target)

                del self._cache_map[target.key]
                
            
            

        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)