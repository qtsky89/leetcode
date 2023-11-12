class Solution:
    def __init__(self):
        self._hash_map = {0:0, 1:1, 2:1}

    def tribonacci(self, n: int) -> int:
        if n not in self._hash_map:
            self._hash_map[n] = self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
        return self._hash_map[n]
        