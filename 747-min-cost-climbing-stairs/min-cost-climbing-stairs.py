class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        cost = [10, 15, 20]

        dp =   [10, 15, 30]
                     ^   ^

                     15

        time: O(N)
        space: O(N)

        '''

        dp = [0] * len(cost)

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, len(dp)):
            dp[i] = min(dp[i-2], dp[i-1]) + cost[i]

        return min(dp[-1], dp[-2])