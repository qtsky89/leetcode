class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        nums = 1  1  2  3  3  4  4  8  8
               -  -  -     m  +  +  +  +
                           4           8
               l  m  r

                     lmr               

        
        => nums[m-1] != nums[m] != nums[m+1]

        we need to keep searching odd number as possible
        '''

        l, r = 0, len(nums)-1

        while l<=r:
            m = l + (r-l) // 2

            if (m == 0 or nums[m-1] != nums[m]) and (m == len(nums)-1 or nums[m] != nums[m+1]):
                return nums[m]
            elif nums[m] == nums[m+1]:
                # odd number count
                if m % 2 != 0:
                    r = m - 1
                else:
                    l = m + 2
            elif nums[m] == nums[m-1]:
                if (len(nums)-1-m) % 2 != 0:
                    l = m + 1
                else:
                    r = m - 2
        

