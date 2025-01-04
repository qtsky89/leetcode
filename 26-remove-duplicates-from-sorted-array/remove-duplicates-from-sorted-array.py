class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        nums =  0, 1,  2, 3, 4, 2, 2, 3, 3, 4, 4
               i  i+1  j
                   i  i+1       j
                       i i+1          j   
                          i i+1             j
                             i                 j


        '''

        i, j = 0, 0

        while j <= len(nums)-1:
            while j <= len(nums)-1 and nums[i] == nums[j]:
                j += 1
            
            if j == len(nums):
                return i+1
            
            nums[i+1] = nums[j]
            i += 1