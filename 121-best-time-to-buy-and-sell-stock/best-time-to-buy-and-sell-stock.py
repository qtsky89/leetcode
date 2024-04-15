class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        prices = 7 1 5 3 6 4
                           ^4
                         ^6
                       ^6
                     ^6
                   ^6
                 ^7
                         
                 0  5 1 3   0 0

        '''

        max_price = 0
        max_profit = 0
        for i in range(len(prices)-1, -1, -1):
            max_price = max(max_price, prices[i])

            max_profit = max(max_profit, abs(max_price - prices[i]))
        return max_profit
            