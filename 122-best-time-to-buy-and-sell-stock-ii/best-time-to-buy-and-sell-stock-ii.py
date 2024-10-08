class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        prices = 7 1 5 3 6 4
        '''

        profit_sum = 0

        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                profit_sum += prices[i] - prices[i-1]
        
        return profit_sum