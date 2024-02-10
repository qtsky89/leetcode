class RandomizedSet:

    def __init__(self):
        self._list = []
        self._hash_map = {}

    def insert(self, val: int) -> bool:
        if val in self._hash_map:
            return False
        else:
            self._list.append(val)
            self._hash_map[val] = len(self._list) -1
            return True

    def remove(self, val: int) -> bool:
        if val in self._hash_map:
            index = self._hash_map[val]
            self._hash_map[self._list[-1]] = index
            self._list[len(self._list)-1], self._list[index] = self._list[index], self._list[len(self._list)-1]
            

            self._list.pop()
            del self._hash_map[val]

            return True
        else:
            return False
        
    def getRandom(self) -> int:
        return random.choice(self._list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()