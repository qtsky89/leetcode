class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        nums = 2 1 5 0 4 6
                     i j 
        
        nums[i] = 0
        nums[j] = 4
        nums[k] = 6





        '''

        num_i, num_j = float('inf'), float('inf')

        for i in range(len(nums)):
            if nums[i] <= num_i:
                num_i = min(num_i, nums[i])
            elif nums[i] <= num_j:
                num_j = min(num_j, nums[i])
            else:
                return True
        return False

        