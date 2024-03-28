import heapq

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        '''
        [10, 20] [30, 200] [400, 50] [30, 20]


        [10, 170, -350, -10]

        => 10, 170 => A   10, 30
         -350, -10 => B    50, 20
        '''

        # [10, 20] [30, 200] [400, 50] [30, 20]
        costs.sort(key=lambda x:x[1]-x[0])

        # [400, 50] [30, 20] [10, 20] [30, 200]
        
        total = 0
        for i in range(len(costs)//2):
            total += costs[i][1] # take B
        
        for i in range(len(costs)//2, len(costs)):
            total += costs[i][0] # take A
        
        return total

        

        