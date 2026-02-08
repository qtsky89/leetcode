class Solution:

    # dfs solution
    # def change(self, amount: int, coins: List[int]) -> int:
    #     # amount = 5, coins = [1, 2, 5]

    #     cache = {}

    #     def dfs(i: int, current_total: int) -> int:
    #         if current_total == amount:
    #             return 1
    #         if (i == len(coins)):
    #             return 0
    #         if current_total > amount:
    #             return 0

    #         if (i, current_total) in cache:
    #             return cache[(i, current_total)]           
            
    #         cache[(i, current_total)] = dfs(i, current_total + coins[i]) + dfs(i+1, current_total)

    #         return cache[(i, current_total)]
        

    #     return dfs(0, 0)

    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[(1 if j == 0 else 0) for j in range(amount+1)] for i in range(len(coins))]


        for i in range(len(coins)-1, -1, -1):
            for j in range(1, amount+1):
                ret = 0

                if i+1 <= len(coins)-1 :
                    ret += dp[i+1][j]
                
                if j-coins[i] >= 0:
                    ret += dp[i][j-coins[i]]
                
                dp[i][j] = ret
        
        return dp[0][-1]
        



        