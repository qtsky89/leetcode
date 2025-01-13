class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        '''
        matchsticks = [1, 1, 2, 2, 2]

        sum(matchsticks) =  8

        if 8 % 4 != 0:
            return False

        '''

        matchsticks.sort(reverse=True)

        sum_matchsticks = sum(matchsticks)

        if sum_matchsticks % 4 != 0:
            return False

        target = sum_matchsticks // 4

        # top, bottom, left, right
        current_stick = [0] * 4

        '''
        matchsticks = [1, 1, 2, 2, 2]
                       ^
        '''

        def dfs(i: int) -> bool:
            if i == len(matchsticks):
                return True
            
            for j in range(4):
                if current_stick[j] + matchsticks[i] <= target:
                    current_stick[j] += matchsticks[i]
                    if dfs(i+1):
                        return True
                    current_stick[j] -= matchsticks[i]
            return False
        return dfs(0)

        