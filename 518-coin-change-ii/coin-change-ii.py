class Solution:

    # dfs solution
    def change(self, amount: int, coins: List[int]) -> int:
        # amount = 5, coins = [1, 2, 5]

        cache = {}

        def dfs(i: int, current_total: int) -> int:
            if current_total == amount:
                return 1
            if (i == len(coins)):
                return 0
            if current_total > amount:
                return 0

            if (i, current_total) in cache:
                return cache[(i, current_total)]           
            
            cache[(i, current_total)] = dfs(i, current_total + coins[i]) + dfs(i+1, current_total)

            return cache[(i, current_total)]
        

        return dfs(0, 0)

        