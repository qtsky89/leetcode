class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        piles = [3, 6, 7, 11] h = 8
                 3  6  7  11  k = 1, fail, 27 hours             
                 2  3  4   6  k = 2, fail, 15 hours
                 1  2   3  4  k = 3, fail, 10 hours
                 1, 2, 2, 3   k = 4  success, 8 hours
        '''

        l, r = 1, max(piles)
        # 1 ... 11 find min k

        min_k = float('inf')
        while l <= r:
            mid = (l + r) // 2

            total = 0
            for pile in piles:
                total += (pile // mid) + (1 if pile % mid != 0 else 0)

            # one of right answer
            if total <= h:
                r = mid - 1
                min_k = min(min_k, mid)
            else:
                l = mid + 1

        return min_k
        

            