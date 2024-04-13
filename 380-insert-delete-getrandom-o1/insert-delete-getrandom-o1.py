class RandomizedSet:
    def __init__(self):
        # 2, 3, 4
        self.list: list[int] = [] # [2, 4, 3]

        # {2: 0, 3: 2, 4: 1}
        self.dic: dict[int, int] = {}
        
    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        else:
            self.list.append(val)
            self.dic[val] = len(self.list)-1
            return True
            
    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        else:
            a_index = self.dic[val]

            self.dic[self.list[-1]] = a_index
            self.list[a_index], self.list[-1] = self.list[-1], self.list[a_index]

            del self.dic[val]
            self.list.pop()

            return True


    def getRandom(self) -> int:
        index = random.randint(0, len(self.list)-1)

        return self.list[index]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()