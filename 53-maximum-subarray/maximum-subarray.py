class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''

        nums = [ -2  1  -3  4  -1  2  1  -5  4 ]
        dp       -2                         

        dp[0] = -2
        dp[1] = dp[0] + nums[1] (because it's positive)
        dp[2] = if dp[1] > nums[2] => dp[2] + nums[] -3

        '''
        # dp = [0 0 0 0 0 0 0 0 0]
        dp = [0] * len(nums)

        dp[0] = nums[0]
        for i in range(1, len(dp)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        return max(dp)
        


