class RandomizedSet:
    def __init__(self):
        self._hashmap = dict()
        self._list = list()

    def insert(self, val: int) -> bool:
        if val in self._hashmap:
            return False
        else:
            self._list.append(val)
            self._hashmap[val] = len(self._list)-1
            return True

    def remove(self, val: int) -> bool:
        if val in self._hashmap:
            index = self._hashmap[val]
            self._hashmap[self._list[-1]] = index
            self._list[-1], self._list[index] = self._list[index], self._list[-1]
            self._list.pop()
            del self._hashmap[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        rand_index = random.randint(0, len(self._list)-1)
        return self._list[rand_index]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()