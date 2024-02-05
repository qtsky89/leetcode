class Solution:
    def __init__(self):
        self._cache = {0:0, 1:0}

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        0   1   2  3
cost    10  15  20           => 15
                             => 10 + 20 ...
                             => 10 + 15 + 20 
       dp[0] => 0
       dp[1] => 0
       dp[2] => min(dp[0] + costs[0], dp[1] + costs[1])
       dp[3] => min(dp[1] + costs[1], dp[2] + costs[1])
       ...
       dp[n] => min(dp[n-2] + costs[n-2], dp[n-1] + costs[n-1])
        '''

        def dp(i : int) -> int:
            if i not in self._cache:
                self._cache[i] = min(dp(i-2) + cost[i-2], dp(i-1) + cost[i-1])
            return self._cache[i]
            
        return dp(len(cost))