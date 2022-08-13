class Solution:
    hash_map = {0:0, 1:1}
    def fib(self, n: int) -> int:
        if n in self.hash_map:
            return self.hash_map[n]
        
        self.hash_map[n] = self.hash_map[n-1] + self.hash_map[n-2]
        return self.hash_map[n]