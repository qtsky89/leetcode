class LinkedListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyHashSet:
    def __init__(self):
        self.capacity = 100
        self.array = [LinkedListNode(None) for _ in range(self.capacity)]
        
    # 1, 1001, 2001, 3001
    def hash_function(self, key: int) -> int:
        return key % self.capacity


    def add(self, key: int) -> None:
        index = self.hash_function(key)

        p = self.array[index]

        while p and p.next:
            if p.next.val == key:
                return
            p = p.next
        
        p.next = LinkedListNode(key)

    def remove(self, key: int) -> None:
        index = self.hash_function(key)

        p = self.array[index]
        while p and p.next:
            if p.next.val == key:
                p.next = p.next.next
                break
            p = p.next
        

    def contains(self, key: int) -> bool:
        index = self.hash_function(key)

        p = self.array[index]

        while p:
            if p.val == key:
                return True
            p = p.next
        
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)