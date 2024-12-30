class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        piles = 3, 6, 7, 11      h = 8


        k=1     3  6  7  11 => 27
        k=2     2  3  4  6  => 15
        k=3     1  2  3  4  => 10
        k=4     1  2   2  3 => 8 !!
        k=5     1  2   2  3 => 8
        k=6     1  1   2  3 => 7
        k=7     1  1   1  2 => 5
        k=8     1  1   1  2 => 5
        k=9     1   1  1  2 => 5
        k=10    1  1   1  1  => 5
        k=11     1 1   1  1 = > 4


        27 15 10  8  8 7 5 5 5 5   4
      k  1  2  3  4  5 6 7 8 9 10  11(max of pile)
                     ^
        '''

        l, r = 1, max(piles)

        while l <= r:
            mid = l + (r-l) // 2

            tmp = 0
            for p in piles:
                tmp += math.ceil(p/mid)

            if tmp > h:
                l = mid + 1
            else:
                r = mid - 1
        return l
                
            

        