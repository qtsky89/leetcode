class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        piles = [3, 6, 7, 11] h = 8
                 
        k = 1   3 + 6 + 7 + 11 = 27 hours, koko will be arrested
        k = 2   2 + 3 + 4 + 6  = 15 hours,  koko will be arrested
        k = 3   1 + 2 + 3 + 4 = 12 hours, koko will be arrested
        k = 4   1 + 2 + 2 + 3 = 8 hours, koko will not be arrested ! yey!
        k = larget piles   1 + 1 + 1 + 1 = 4 hours

        
        1. every interation we cacluate the hours
        2. hours == h return k // TODO. add some edge case
        3. hours > h k = l + 1
        4. hours < h k = r-1
        '''

        l, r = 1, max(piles)

        k = 1
        while l <= r:
            m = (l + r) // 2

            hours = 0
            for pile in piles:
                hours += math.ceil(pile / m)
            
            if hours <= h:
                k = m
                r = m - 1
            else:
                l = m + 1
        return k