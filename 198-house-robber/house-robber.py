class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        nums(money) = [1   2   3   1]
                       ^

        dp[0] = 1
        dp[1] = 2
        dp[2] = max( dp[0] + nums[2], dp[1])
        dp[3] = max( dp[1] + nums[3], dp[2]  )
            ...

        return dp[n-1]
        '''

        dp = [0] * len(nums)
        if len(dp) == 1:
            return nums[0]
        elif len(dp) == 2 :
            return max(nums[0], nums[1])
        
        dp[0], dp[1] = nums[0], nums[1]
        
        for i in range(2, len(dp)):            
            if i >= 3:
                dp[i] = max(dp[i-3] + nums[i], dp[i-2] + nums[i], dp[i-1])
            else:
                dp[i] = max(dp[i-2] + nums[i], dp[i-1])

        
        return dp[-1]