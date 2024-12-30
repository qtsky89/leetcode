class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
               0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16  17  18
                                          ^

        nums = 1, 1, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10
               l                          m                            
               l           m           r
               l  m  r
                    lmr

        1. m is single element or not?

        2. left length is odd go left

        3. right length is odd go right
        '''

        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r-l)//2

            # TODO. boundary check
            if (m == 0 or nums[m-1] != nums[m]) and (m == len(nums)-1 or nums[m] != nums[m+1]):
                return nums[m]
            
            if nums[m] == nums[m-1]:
                if (len(nums)-1-m) % 2 == 0:
                    r = m - 2
                else:
                    l = m + 1
            else:
                if (m) %2 == 0:
                    l = m + 2
                else:
                    r = m - 1