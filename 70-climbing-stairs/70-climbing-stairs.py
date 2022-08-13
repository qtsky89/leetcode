hash_map = {}

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        
        if n not in hash_map:
            hash_map[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        
        return hash_map[n]
        
        