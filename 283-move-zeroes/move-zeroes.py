class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        nums = 0 1 0 3 12
                 ^
               1 0 0 3 12
                     ^
               1 3 0 0 12
                   ^    ^
                1 3 12 0 0 
        ''' 

        i, j = 0, 0

        while i <= j <= len(nums)-1:
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]

                i += 1
                j += 1
            else:
                j += 1
        