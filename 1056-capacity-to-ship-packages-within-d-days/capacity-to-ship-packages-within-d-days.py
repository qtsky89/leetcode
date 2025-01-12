class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        weights = [1, 2, 3, 4, 5] days = 2
                               ^
        
        capacity: 5 (1, 2) (3) (4) (5) => 5 days
                  6 (1, 2, 3) (4) (5) => 3 days
                  7 (1, 2, 3) (4) (5) => 3 days
                  8 (1, 2, 3) (4) (5) => 3 days
                  9 (1, 2, 3) (4, 5) =>  2 days
                  10 (1, 2, 3, 4) (5) => 2 days
                  11 (1, 2, 3, 4) (5) => 2 days
                  12 (1, 2, 3, 4) (5) => 2 days
                  13 (1, 2, 3, 4) (5) => 2 days
                  14 (1, 2, 3, 4) (5) => 2 days
                  15 (1, 2, 3, 4, 5) => 1 days
        
        capacity: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
                  l                                   r

        days    : 5, 3, 3, 3, 2,  2,  2,  2,  2,   2, 1
                  l               m                    r
                              
        '''

        l, r = max(weights), sum(weights)

        while l <= r:
            m = l + (r-l) // 2

            # calculate days
            current_sum = 0
            day = 1
            for weight in weights:
                if current_sum + weight <= m:
                    current_sum += weight
                else:
                    day += 1
                    current_sum = weight
            ###

            if day <= days:
                r = m - 1
            else:
                l = m + 1
        return l