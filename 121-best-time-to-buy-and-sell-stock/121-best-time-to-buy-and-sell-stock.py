

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
            elif prices[i] - smallest > max_profit:
                max_profit = prices[i] - smallest
        
        return max_profit
        
    
    '''
from heapq import heapify, heappop
    def maxProfit(self, prices: List[int]) -> int:
        heap = [-prices[i] for i in range(len(prices))]
        
        # heap
        heapify(heap)
        
        max_profit = 0
        for i in range(len(prices)):
            max_after = -heap[0]
            diff = max_after - prices[i]
            max_profit = max(max_profit, diff)
            
            heap.remove(-prices[i])
            heapify(heap)
        return max_profit'''