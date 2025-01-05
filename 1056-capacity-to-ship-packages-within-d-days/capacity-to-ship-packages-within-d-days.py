class Solution:
    def days(self, weights: list[int], capacity: int) -> int:
        '''
        weight = 1, 2, 3, 1, 1    4days

                (1, 2) (3) (1, 1)
        
                 


        capacity: 3 => 3days
        
        '''

        count = 1
        total = 0
        for i in range(len(weights)):
            if total + weights[i] > capacity:
                count += 1
                total = 0
            total += weights[i]
        
        return count
        

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        weight = 1, 2, 3, 4, 5, 6, 7, 8, 10

        find lowest capacity as possible

        capacity => min(weight), 11, 12, 13 ...      sum(weight)
                      ^                   m                ^
        '''

        l, r = max(weights), sum(weights)

        while l <= r:
            m = l + (r-l)//2
            
            tmp_day = self.days(weights, m)

            if tmp_day < days:
                r = m - 1
            elif tmp_day > days:
                l = m + 1
            else:
                r = m - 1
        
        return l

        