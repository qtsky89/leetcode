class DoubleLinkedListNode:
    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class DoubleLinkedList:
    def __init__(self) -> None:
        self.head = DoubleLinkedListNode(None, None)
        self.tail = DoubleLinkedListNode(None, None)

        self.head.next, self.tail.prev = self.tail, self.head
    
    def add_tail(self, new_node: DoubleLinkedListNode) -> None:
        self.tail.prev.next, new_node.prev, new_node.next, self.tail.prev = new_node, self.tail.prev, self.tail, new_node
        
    def delete_node(self, exist_node: DoubleLinkedListNode) -> None:
        exist_node.prev.next, exist_node.next.prev = exist_node.next, exist_node.prev


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache: dict[int, DoubleLinkedListNode] = {}
        self.list: DoubleLinkedList = DoubleLinkedList()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        exist_node = self.cache[key]

        self.list.delete_node(exist_node)
        self.list.add_tail(exist_node)

        return exist_node.val


    def put(self, key: int, value: int) -> None:
        # update (similar to get)
        if key in self.cache:
            exist_node = self.cache[key]

            exist_node.val = value

            self.list.delete_node(exist_node)
            self.list.add_tail(exist_node)
        else: # create
            new_node = DoubleLinkedListNode(key, value)
            self.cache[key] = new_node

            self.list.add_tail(new_node)

            # need to remove
            if len(self.cache) > self.capacity:
                target = self.list.head.next
                del self.cache[target.key]
                self.list.delete_node(target)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)