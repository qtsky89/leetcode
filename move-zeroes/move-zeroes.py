class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] == 0 and nums[j] != 0:
                    nums[i], nums[j] = nums[j], nums[i]
                    break

        '''
        nums = [0 1 0 3 12]
                p1p2

               [1 0 0 3 12]
                  p1  p2

               [1 3 0 0 12]
                    p1  p2

               [1 3 12 0 0]
        '''

        
        
        


            
            
            