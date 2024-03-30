'''
    id_key, value

    aaaaa   bbbbb    ccccc              eeeee
    
'''


class OrderedStream:
    def __init__(self, n: int):
        self._stream = {}
        self._completed = 0
        self._n = n

    def insert(self, id_key: int, value: str) -> List[str]:
        self._stream[id_key] = value

        start = self._completed

        i = self._completed
        while True:
            if i+1 in self._stream:
                i += 1
            else:
                break
        self._completed = i

        ret = []
        for i in range(start+1, self._completed+1):
            ret.append(self._stream[i])
        return ret


        
        
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)