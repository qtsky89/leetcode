import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        https://www.youtube.com/watch?v=U2SozAs9RzA 

        piles = [3, 6, 7, 11]
                 ^
                 1  2   3   4 => 10 hours

        minimum number of k => 3
        h = 8

        k=1 make bigger

        k is in between 1 to max of pile
        '''

        l, r = 1, max(piles)
        k = 0
        while l <= r:
            m = (l + r) // 2

            eating_hour = 0
            for pile in piles:
                eating_hour += math.ceil(pile / m)

            if eating_hour <= h:
                k = m
                r = m-1
            else:
                l = m+1
        return k

            

            
        
            