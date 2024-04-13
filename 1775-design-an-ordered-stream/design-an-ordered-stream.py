class OrderedStream:
    def __init__(self, n: int):
        self.stream = [''] * n
        self.p = 0
        
    def insert(self, idKey: int, value: str) -> List[str]:
        self.stream[idKey-1] = value

        start_index = self.p
        while self.p <= len(self.stream)-1 and self.stream[self.p] != '':
            self.p += 1
        
        return self.stream[start_index:self.p]
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)