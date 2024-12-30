class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        nums = 2
               X 

        nums = 3 2 1 0 4
                       X False

        '''

        i = len(nums)-1

        while i > 0:
            tmp = i
            for j in range(0, i):
                if nums[j] >= (i-j):
                    i = j
                    break
            if i == tmp:
                return False
        
        return True

            