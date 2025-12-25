class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ''' 
        prices = [1, 2, 3, 0, 2]
        '''

        cache = {}
        def dfs(i: int, status: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, status) in cache:
                return cache[(i, status)]

            if status: # buy
                buy = dfs(i+1, False) - prices[i]
                cooldown = dfs(i+1, status)
                cache[(i, status)] = max(buy, cooldown)
            else: # sell
                sell = dfs(i+2, True) + prices[i]
                cooldown = dfs(i+1, status)
                cache[(i, status)] = max(sell, cooldown)
            
            return cache[(i, status)]

        return dfs(0, True)