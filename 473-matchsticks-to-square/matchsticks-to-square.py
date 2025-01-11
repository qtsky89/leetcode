class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        sum_length = sum(matchsticks)

        if sum_length % 4 != 0:
            return False
        
        four_length = [0] * 4
    
        matchsticks.sort(reverse=True)

        def dfs(i: int) -> bool:
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if four_length[j] + matchsticks[i] <= (sum_length // 4):
                    four_length[j] += matchsticks[i]

                    if dfs(i+1) == True:
                        return True
                    
                    four_length[j] -= matchsticks[i]
            return False
        

        return dfs(0)