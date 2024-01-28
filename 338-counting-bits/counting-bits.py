class Solution:
    def _get_bits(self, n: int) -> int:
        # n => 0 , 1 , 2 ...

        total = 0
        while n > 0:
            if n & 1:
                total += 1
            n = n >> 1
        return total

    def countBits(self, n: int) -> List[int]:
        '''
          [0, 1, 2]
           0  1  1 => 2

          [0, 1, 1, 2, 1, 2]
           0  1  1  1  1  1 => 5

        '''

        ret = [0] * (n+1)
        for i in range(n+1):
            ret[i] = self._get_bits(i)
        
        return ret
            
