class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        '''
        nums =       [1 7  3  6  5  6]
        prefix_sum = [1 8 11 17 22 28]
        pivot_index = 0, left=> 0,  right => 28-1  => 27
                      1, left=> 1,  right => 28-8  => 20
                      2, left=> 8,  right => 28-11 => 17
                      3, left=> 11, right => 28-17 => 11
                      4, left=> 17, right => 28-22 => 6
                      5, left=> 22, right => 0
        '''

        prefix_sum = [0] * len(nums)
        for i in range(len(prefix_sum)):
            if i==0:
                prefix_sum[i] = nums[0]
            else:
                prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        for i in range(len(nums)):
            left_sum = prefix_sum[i-1] if i>0 else 0
            right_sum = prefix_sum[-1] - prefix_sum[i] if i <= len(nums)-2 else 0
            
            if left_sum == right_sum:
                return i
        return -1