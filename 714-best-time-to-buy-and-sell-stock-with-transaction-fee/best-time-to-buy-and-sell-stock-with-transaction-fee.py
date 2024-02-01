# damn hard, I watched the solutions
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        '''
        hold[i] = max(hold[i-1], free[i-1] - prices[i])

        1  3  2  8  4  9

hold    1  1
free    0  0

        '''

        free, hold = [0] * len(prices), [0] * len(prices)

        hold[0] = -prices[0]

        for i in range(1, len(prices)):
            hold[i] = max( hold[i-1], free[i-1] - prices[i])
            free[i] = max (free[i-1], hold[i-1] + prices[i] - fee)
        return free[-1]