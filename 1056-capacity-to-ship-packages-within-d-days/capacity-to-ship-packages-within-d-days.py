class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        capacity = start from max(weight)
                   end sum(weight)

        weight = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10     days = 5
                 
        capacity = 10 => (1, 2, 3, 4) (5) (6) (7) (8) (9) (10) => 7 days
                   11 => (1, 2, 3, 4) (5, 6), (7) (8) (9) (10) => 6 days
                   12 => (1, 2, 3, 4) (5, 6) (7) (8) (9) (10) => 6 days
                   13 => (1, 2, 3, 4) (5, 6) (7) (8) (9) (10) => 6 days
                   14 => (1, 2, 3, 4) (5, 6) (7) (8) (9) (10) => 6 days
                   15 => (1, 2, 3, 4) (5, 6) (7, 8) (9) (10) => 5 days
                          1  3  6  10  5  6   7  8  9    10
                          total = 9
                          tmp_day = 4
        '''

        l, r = max(weights), sum(weights)

        while l <= r:
            m = l + (r-l) // 2

            i = 0
            total = 0
            tmp_day = 1
            while i <= len(weights)-1:
                if total + weights[i] > m:
                    tmp_day += 1
                    total = 0
                total += weights[i]

                i += 1
            
            if tmp_day <= days:
                r = m - 1
            else:
                l = m + 1
        
        return l
         
                