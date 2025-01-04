class LinkedListNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    def __init__(self):
        self.capacity = 100
        self.array = [LinkedListNode(None, None) for _ in range(self.capacity)]   


    # 1, 1001, 2001, 3001
    def hash_function(self, key: int) -> int:
        return key % self.capacity


    def put(self, key: int, value: int) -> None:
        index = self.hash_function(key)

        p = self.array[index]

        while p and p.next:
            # update
            if p.next.key == key:
                p.next.val = value
                return
            p = p.next
        
        # create
        p.next = LinkedListNode(key, value)

    def get(self, key: int) -> int:
        index = self.hash_function(key)

        p = self.array[index]

        while p and p.next:
            if p.next.key == key:
                return p.next.val
            p = p.next
        
        return -1


    def remove(self, key: int) -> None:
        index = self.hash_function(key)

        p = self.array[index]
        while p and p.next:
            if p.next.key == key:
                p.next = p.next.next
                break
            p = p.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)