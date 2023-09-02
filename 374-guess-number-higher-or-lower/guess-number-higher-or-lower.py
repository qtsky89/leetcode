# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        '''
        n = 10   pick = 3
        1 2 3 4 5 6 7 8 9 10
        
        1. 
            mid = 11 // 2 => 5
            
        '''

        first, end = 1, n
        while True:
            mid = (first + end) // 2
            
            res = guess(mid)

            if res == 0: # answer
                return mid
            elif res == -1: # guess is higher
                end = mid - 1
            else:  # guess is less
                first = mid+1
                