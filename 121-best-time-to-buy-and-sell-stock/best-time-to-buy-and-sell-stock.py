class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        example1.

        prices =     [ 7 1 5 3 6 4 ]
        max_values = [ 7 6 6 6 6 4 ]

        step1. let's make max_values in reverse order
        step2. let's find start increasing point
        step3. let's find the max differ
        '''

        # step1. let's make max_values in reverse order
        max_values = [0] * len(prices)
        max_values[-1] = prices[-1]
        for i in range(len(max_values)-2, -1, -1):
            max_values[i] = max(prices[i], max_values[i+1])
        
        # step2. let's find start increasing point
        max_diff = 0
        for i in range(len(prices)-1):
            max_diff = max(max_diff, max_values[i] - prices[i])
        
        return max_diff
            
        