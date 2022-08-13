class Solution:
    def reverseBits(self, n: int) -> int:
        # {0: 0, 1: 0, ... 31: 0}
        hash_table = {i: 0 for i in range(32)}
        
        for i in range(32):
            if n & (2 ** i) == (2 ** i):
                hash_table[i] = 1
        
        
        ret = 0
        for key, value in hash_table.items():
            if value == 1:
                ret += 2 ** (31-key)
        
        return ret
        
                