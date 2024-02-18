class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

        dp =   [-2, ]

        dp[i] = dp[i-1] + nums[i] or nums[i]

        return max dp[i]
        
        '''

        dp = [0] * len(nums)

        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] + nums[i], nums[i])
        
        print(dp)

        return max(dp)