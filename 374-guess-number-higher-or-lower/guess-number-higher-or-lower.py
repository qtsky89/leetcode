# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        '''
        1. mid => (start + end) // 2
           n = 5 guess => -1
           6 ~ 10 16 // 2 => 8
           n = 8 guess => -1
           6 ~ 7
           ..   guess = > 0
        '''

        l, r = 1, n

        while l <= r:
            mid = (l + r) // 2

            tmp = guess(mid)

            if tmp == 1:
                l = mid+1
            elif tmp == -1:
                r = mid-1
            else:
                return mid