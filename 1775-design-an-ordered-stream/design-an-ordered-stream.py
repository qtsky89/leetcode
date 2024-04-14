class OrderedStream:
    def __init__(self, n: int):
        self.array = [''] * n
        self.p = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        start_index = self.p
        self.array[idKey-1] = value
        
        while self.p <= len(self.array)-1 and self.array[self.p] != '':
            self.p+=1
        
        return self.array[start_index:self.p]
            


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)