class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        '''
        example1. 
            1, 2, 3, 7


        Let's pick Alice point of view

        If she wants to win, she need to maximize her value and minimize the bob's value
        '''

        cache = {}
        # cache[i] > current_total : ignore that path

        # maximze alice's value, minimze bob's value
        def dfs(i: int, is_alice: bool) -> int:
            if i == len(stoneValue):
                return 0
            
            if (i, is_alice) not in cache:
                ret = -float('inf') if is_alice else float('inf')
                if is_alice:
                    for j in range(i, min(i+3, len(stoneValue))):
                        ret = max(ret, sum(stoneValue[i:j+1]) + dfs(j+1, not is_alice))
                else:
                    for j in range(i, min(i+3, len(stoneValue))):
                        ret = min(ret, dfs(j+1, not is_alice))
                cache[(i, is_alice)] = ret
            
            return cache[(i, is_alice)]

        alice_max = dfs(0, True)

        total = sum(stoneValue)
        if alice_max == total - alice_max:
            return 'Tie'
        elif alice_max > total - alice_max:
            return 'Alice'
        else:
            return 'Bob'
        
        
        