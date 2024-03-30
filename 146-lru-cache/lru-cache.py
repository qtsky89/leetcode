
'''

    priority [1 2]

'''

class Node:
    def __init__(self, key: int | None, val: int | None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

'''
    LeastRecentlyUsed <-> Recently Used
      head                    tail
'''

class LRUCache:
    def __init__(self, capacity: int):
        # key: int, value: Node
        self.hash_map = {}
        self.capacity = capacity
        self.head = Node(None, None)
        self.tail = Node(None, None)

        self.head.next, self.tail.prev = self.tail, self.head
    
    def remove(self, node: Node) -> None:
        node.prev.next, node.next.prev = node.next, node.prev

    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1
        
        node = self.hash_map[key]

        # remove
        self.remove(node)

        # drag to the tail
        self.insert(node)

        return node.val
    
    def insert(self, node: Node) -> None:
        prev = self.tail.prev

        prev.next, node.prev = node, prev
        node.next, self.tail.prev = self.tail, node

    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            node = self.hash_map[key]
            self.remove(node)

            node = Node(key, value)
            self.insert(node)
            self.hash_map[key] = node
        else:
            node = Node(key, value)

            self.insert(node)
            self.hash_map[key] = node

            if len(self.hash_map) > self.capacity:
                del self.hash_map[self.head.next.key]
                self.remove(self.head.next)
                
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)