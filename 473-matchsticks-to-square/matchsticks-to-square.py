class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)

        sum_matchsticks = sum(matchsticks)

        if sum_matchsticks % 4 != 0:
            return False
        
        target = sum_matchsticks // 4
        
        # top, bottom, left, right
        buckets = [0] * 4

        ret = False
        def dfs(current_i: int) -> None:
            if current_i == len(matchsticks):
                nonlocal ret
                ret = True
                return
            
            for j in range(4):
                if buckets[j] + matchsticks[current_i] <= target:
                    buckets[j] += matchsticks[current_i]
                    dfs(current_i+1)
                    buckets[j] -= matchsticks[current_i]

                if buckets[j] == 0:
                    return
        
        dfs(0)

        return ret