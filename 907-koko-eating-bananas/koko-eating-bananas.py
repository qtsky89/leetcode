class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''

        piles = 3 6 7 11  h = 8

        k=1     3 6 7 11  => 27 hours
        k=2     2 3 4  6  => 15 hours
        k=3     1 2 3  4  => 10 hours
        k=4     1 2 2  3  => 8 hours
        k=5     1 2 2  3  => 8 hours

             27 15 10 8  8 
        k =  1  2  3  4  5 ... 11 

        '''

        l, r = 1, max(piles)

        while l <= r:
            m = l + (r-l) // 2

            tmp = 0
            for p in piles:
                tmp += math.ceil(p / m)
            
            if tmp == h:
                r = m - 1
            elif tmp > h:
                l = m + 1
            elif tmp < h:
                r = m - 1

        return l
        
        