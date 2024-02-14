class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        nums = [2, 3, 1, 1, 4]
                ^

        '''

        dp = [0] * len(nums)

        goal = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0

        

        