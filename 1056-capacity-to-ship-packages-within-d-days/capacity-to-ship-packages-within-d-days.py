class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        weights = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10      days= 5
                                              ^

        capacity 10: (1, 2, 3, 4) (5) (6) (7) (8) (9) (10) => 7 days
        capacity 11: (1, 2, 3, 4) (5, 6) (7) (8) (9) (10) => 6 days
        capacity 12: (1, 2, 3, 4) (5, 6) (7) (8) (9) (10) => 6 days
        capacity 13: (1, 2, 3, 4) (5, 6) (7) (8) (9) (10) => 6 days
        capacity 14: (1, 2, 3, 4) (5, 6) (7) (8) (9) (10) => 6 days
        capacity 15: (1, 2, 3, 4, 5) (6, 7) (8) (9) (10) => 5 days
        

        capacity: 10 11 12 13 14 15

        days       7 6  6  6  6   5
                                  ^
        '''

        l, r = max(weights), sum(weights)

        while l <= r:
            m = l + (r-l) // 2

            # using this m capacity , let's convert to days
            current_sum = 0
            current_day = 1
            for weight in weights:
                if current_sum + weight > m:
                    current_sum = weight
                    current_day += 1
                else:
                    current_sum += weight
            
            if current_day == days:
                r = m - 1
            elif current_day > days:
                l = m + 1
            elif current_day < days:
                r = m - 1

        return l