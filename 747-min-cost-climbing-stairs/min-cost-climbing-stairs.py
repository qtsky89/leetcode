class Solution:


    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        cost = [1,100,1,1,1,100,1,1,100,1]

        10 root
        9
        8
        7
        6
        5
        4
        3
        2 1
        1 start
        0 start
        
        to get 2 index => min(1, 100)
        to get 3 index => dp(2) + 


        dp(3) = min (dp(2) + cost[2], dp(1) + cost[1])
        
        ...

        dp(n) = min(dp[n-1] + cost[n-1], dp[n-2] + cost[n-2])
        '''

            
        cache: dict[int, int] = {0: 0, 1: 0}

        def dp(n: int) -> int:
            if n not in cache:
                cache[n] = min(dp(n-1) + cost[n-1], dp(n-2) + cost[n-2])
            
            return cache[n]
        
        print(cache)
        
        return dp(len(cost))
        