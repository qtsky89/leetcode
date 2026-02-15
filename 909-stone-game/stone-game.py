class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''
        piles = [5, 3, 4, 5]
                 A  B  B  A 
                 A  B  A  B
        A => 10
        B => 7

        '''

        cache = {}

        def dfs(i: int, j: int) -> int:
            if i > j:
                return 0
            
            if (i, j) not in cache:
                is_allice_tern = (j-i) % 2 == 1

                if is_allice_tern:
                    cache[(i, j)] = max(piles[i] + dfs(i+1, j), piles[j] + dfs(i, j-1))
                else:
                    cache[(i, j)] = min(dfs(i+1, j), dfs(i, j-1))
            
            return cache[(i, j)]
        
        
        return dfs(0, len(piles)-1) > (sum(piles) // 2)