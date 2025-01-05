class Solution:
    def mySqrt(self, x: int) -> int:
        '''
        x = 8

        1, 2, 3, 4, 5, 6, 7, 8
           ^
        1  4  9  16 25 36 49 64



        '''

        l, r = 1, x

        while l <= r:
            m = l + (r - l) // 2

            tmp = m*m

            if tmp == x:
                return m
            elif tmp < x:
                l = m + 1
            else:
                r = m - 1

        return (l+r) // 2

        