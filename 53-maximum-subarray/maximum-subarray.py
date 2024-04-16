class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        nums = -2 1 -3 4 -1 2 1 -5 4
                ^                       -2
                  ^                     -2+1 or 1 (V)
                     ^                   +1-3 (V) or -3

        dp[i] = nums[i] or dp[i-1] + nums[i]
        '''
        
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        return max(dp)

        