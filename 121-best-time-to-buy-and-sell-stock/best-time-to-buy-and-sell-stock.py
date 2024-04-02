class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ret = [0] * len(prices)

        max_profit = 0
        max_val = -float('inf')
        for i in range(len(prices)-1, -1, -1):
            max_val = max(max_val, prices[i])

            max_profit = max(max_profit, max_val - prices[i])
        
        return max_profit
            