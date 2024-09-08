from random import randint

class RandomizedSet:
    def __init__(self):
        self._dic = {}
        self._list = []

    def insert(self, val: int) -> bool:
        if val in self._dic:
            return False
        else:
            self._list.append(val)
            self._dic[val] = len(self._list)-1
            return True

    def remove(self, val: int) -> bool:
        if val not in self._dic:
            return False

        index = self._dic[val]
        last_index = len(self._list)-1
        last_val = self._list[-1]
        self._dic[last_val] = index

        self._list[index], self._list[last_index] = self._list[last_index], self._list[index]
        self._list.pop()

        del self._dic[val]
        

        return True

    def getRandom(self) -> int:
        index = randint(0, len(self._list)-1)

        return self._list[index]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()