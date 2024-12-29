class Solution:
    # def coinChange(self, coins: List[int], amount: int) -> int:
    #     '''
    #     count_map = {
    #         5 : 1
    #         2 : 1
    #         1 : 1
    #     }

    #     '''

    #     coins.sort(reverse=True)

    #     count_map = {}

    #     def dfs(current_sum: int, coin_count: int) -> None:
    #         if current_sum > amount:
    #             return

    #         if current_sum in count_map and count_map[current_sum] <= coin_count:
    #             return
            
    #         count_map[current_sum] = coin_count
                
    #         for coin in coins:
    #             dfs(current_sum+coin, coin_count+1)

    #     dfs(0, 0)

    #     return count_map[amount] if amount in count_map else -1
    
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        dp[11] = dp[6] + 1
        dp[6] = dp[5] + 1
        dp[5] = 1
        '''

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] = min(dp[i], dp[i-coin] + 1)
        
        return dp[-1] if dp[-1] != float('inf') else -1
        