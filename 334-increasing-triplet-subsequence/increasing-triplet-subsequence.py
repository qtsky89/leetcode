class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        '''
        maximum = -float('inf')
        second_maximum = -float('inf')


        nums = 20,100,10,12,5,13
                ^     

        maximum = 100
        second_maximum =  20

        '''

        minimum = float('inf')
        second_minimum = float('inf')

        for i in range(len(nums)):
            if nums[i] > second_minimum:
                return True
            elif nums[i] < minimum:
                minimum = nums[i]
            elif minimum < nums[i] < second_minimum:
                second_minimum = nums[i]
        
        return False


