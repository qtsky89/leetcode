class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        nums = 1   3   0   0   12
                       ^        ^

        '''

        l, r = 0, 0
        while r <= len(nums)-1:
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1

            r += 1