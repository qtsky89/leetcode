class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        nums = 2  3  1  1  4
                  ^        ^
               0  1  2  3  4   
                               
        '''

        count = 0
        # i = 4
        i = len(nums)-1
        while i > 0:
            count += 1
            # j 0 ~ 3
            for j in range(i):
                if nums[j] >= (i-j):
                    i = j
                    break
        return count
                