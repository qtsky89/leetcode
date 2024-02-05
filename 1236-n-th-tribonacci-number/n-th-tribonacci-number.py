class Solution:
    def __init__(self):
        self._cache = {0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        '''
        t(0) = 0
        t(1) = 1
        t(2) = 1

        t(n+3) = t(n) + t(n+1) + t(n+2)
        '''

        if n not in self._cache:
            self._cache[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self._cache[n]

        