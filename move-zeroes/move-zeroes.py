class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_count = 0
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i+=1
            else:
                zero_count += 1
        
        if zero_count != 0:
            nums[-zero_count:] = [0] * zero_count
        
        

        