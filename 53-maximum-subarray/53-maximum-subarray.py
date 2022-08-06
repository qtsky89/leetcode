class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        dp = nums[:]
        
        max_sum = -float('inf')
        for i in range(0, len(dp)):
            if i == 0:
                dp[i] = nums[i]
            else:
                dp[i] = max(dp[i-1] + nums[i], nums[i])
            max_sum = max(max_sum, dp[i])
        
        return max_sum
        
        
        