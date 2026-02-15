class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        '''
        piles = 2, 7, 9, 4, 4
        '''

        cache = {}
        # return alice's max total value
        def dfs(is_alice: bool, i: int, M: int) -> int:
            if i >= len(piles):
                return 0
            
            if (is_alice, i, M) not in cache:
                ret = 0 if is_alice else float('inf')
                
                for j in range(i, min(i+2*M, len(piles))):
                    X = j-i+1
                    next_M = max(M, X)

                    if is_alice:
                        ret = max(ret, sum(piles[i:j+1]) + dfs(not is_alice, j+1, next_M))
                    else:
                        ret = min(ret, dfs(not is_alice, j+1, next_M))
                
                cache[(is_alice, i, M)] = ret
                
            
            return cache[(is_alice, i, M)]
        

        return dfs(True, 0, 1)