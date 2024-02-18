class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        nums = [2, 3, 1, 0, 4]
                            ^ False
        '''

        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        return goal == i
            