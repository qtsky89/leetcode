class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        binary search can only work in sorted array

        nums = [4, 5, 6, 7, 0, 1, 2]
                l        m        r


                
        '''
        if len(nums) == 1:
            return nums[0]


        l, r = 0, len(nums)-1

        while l <= r:
            m = l + (r-l) // 2

            # smallest target
            if nums[m-1] > nums[m]:
                return nums[m]
            elif nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

        
                