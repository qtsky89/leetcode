class RandomizedSet:
    def __init__(self):
        self._set = set()

    def insert(self, val: int) -> bool:
        if val in self._set:
            return False
        else:
            self._set.add(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self._set:
            self._set.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        li = list(self._set)

        rand_index = random.randint(0, len(li)-1)

        return li[rand_index]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()