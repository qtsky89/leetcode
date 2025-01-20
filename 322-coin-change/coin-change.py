class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        coin = 1

        dp[1] = dp[0] + 1
        dp[2] = dp[1] + 1
        ...


        coin = 5
        dp[5] = 1
        dp[6] = 2
        ...






        '''
    
        dp = [float('inf')] * (amount+1)
        dp[0] = 0
        for coin in coins:
            for i in range(coin, len(dp)):
                dp[i] = min(dp[i], dp[i-coin]+1)
        

        return dp[-1] if dp[-1] != float('inf') else -1