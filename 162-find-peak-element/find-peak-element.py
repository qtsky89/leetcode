class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        https://www.youtube.com/watch?v=kMzJy9es7Hc

        nums = [1, 2, 3, 1]

                      -V 
                   -
                -        -


        nums = [1, 2, 1, 3, 5, 6, 4]
                               -V
                            -
                                  -
                         -
                   -V    
                -     -

        
        binary search
        1. start_index, middle_index, end_index
               1           3             4
        2. check middle_index is peak
        3. else search right!
        '''

        if len(nums) == 1:
            return 0

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2

            # check middle is peak element
            if (m == 0 or nums[m-1] < nums[m]) and (m == len(nums)-1 or nums[m] > nums[m+1]):
                return m
            
            # it's not then, go right
            if nums[m] < nums[m+1]:
                l = m + 1
            else:
                r = m - 1

            
            
            

        