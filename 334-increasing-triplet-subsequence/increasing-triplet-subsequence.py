class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        nums = 20,100,10,12,5,13
               ^

        num_i = float('inf')
        num_j = float('inf')

        
        '''

        num_i, num_j = float('inf'), float('inf')

        for k in range(len(nums)):
            if nums[k] <= num_i:
                num_i = nums[k]
            elif nums[k] <= num_j:
                num_j = nums[k]
            else:
                return True                

        return False


