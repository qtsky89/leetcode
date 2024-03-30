class OrderedStream:
    def __init__(self, n: int):
        self._stream = [''] * n
        self._p = 0
    def insert(self, id_key: int, value: str) -> List[str]:
        self._stream[id_key-1] = value

        start_index = self._p
        while self._p <= len(self._stream)-1 and self._stream[self._p] != "":
            self._p += 1
        end_index = self._p

        return self._stream[start_index:end_index]
# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)