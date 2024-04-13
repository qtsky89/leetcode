class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        '''
        0 -> a, 10      10
          -> b, 20           
        
        1 -> a, 30      170
          -> b, 200
        
        2 -> a, 400      -370
          -> b, 50
        
        3 -> a, 30       -10
          -> b, 20


        plus means A prefer
        minus means B perfer

        => [400, 50] [30, 20] [10, 20] [30, 200]
              B                  A
        '''

        costs.sort(key=lambda x: x[1]-x[0])

        total = 0

        for i in range(len(costs)//2):
            total += costs[i][1]
        
        # 
        for i in range(len(costs)//2, len(costs)):
            total += costs[i][0]

        return total
