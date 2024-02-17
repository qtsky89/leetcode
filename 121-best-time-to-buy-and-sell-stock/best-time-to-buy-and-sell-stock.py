class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        prices =     [ 7, 1, 5, 3, 6, 4]

        max_prices = [ 7  6  6  6  6  4]
        '''

        max_prices = [0] * len(prices)
        max_prices[-1] = prices[-1]

        for i in range(len(max_prices)-2, -1, -1):
            max_prices[i] = max(max_prices[i+1], prices[i])
        
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, max_prices[i] - prices[i])
        
        print(max_prices)
        
        return max_profit
            