class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        piles = 3 6 7 11   h=8
                ^
      l k=1     3 6 7 11 => 27
        k=2     2 3 4 6  => 15
        k=3     1 2 3 4  => 10
        k=4     1 2 2 3  => 8          k=4

        k=6     1 1 2 2 => 6

     r  k=11    1 1 1 1  => 4

        mid => 6
        '''

        l, r = 1, max(piles)
        min_k = float('inf')

        while l<=r:
            print(l, r)
            mid = (l+r) // 2

            tmp = 0
            for pile in piles:
                tmp += math.ceil(pile/mid)
            
            if tmp <= h:
                min_k = min(min_k, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_k