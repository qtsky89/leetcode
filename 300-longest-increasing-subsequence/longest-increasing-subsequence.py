class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        nums = 10 9 2 5 3 7 101 18
                ^ ^ ^ ^ ^ ^  ^   ^
        dp      1 1 1 2 2 3  4   4


        if nums[i] > nums[i-1]:
            dp[i] = dp[i-1] + 1 
        '''

        dp = [1] * len(nums)

        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)