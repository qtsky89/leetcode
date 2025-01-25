class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        '''
        stones = [2, 7, 4, 1, 8, 1]

        23 => 12
        

        12

        23 - 24

        

        '''

        sum_stones = sum(stones)
        target = math.ceil(sum_stones / 2)

        dp = {}
        def dfs(i: int, current_sum: int) -> int:
            if (i, current_sum) not in dp:
                if current_sum >= target or i == len(stones):
                    dp[(i, current_sum)] = abs(sum_stones - 2 * current_sum)
                else:
                    dp[(i, current_sum)] = min(dfs(i+1, current_sum + stones[i]), dfs(i+1, current_sum))
            
            return dp[(i, current_sum)]

        
        return dfs(0, 0)