class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        nums = [1, 2, 3, 1]
                ^     ^      4
                   ^     ^   3
                ^        ^   2
        
        nums = [2, 7, 9, 3, 1]
                ^     ^     ^

        dp[0] = 1
        dp[1] = 2

        dp[n] = max(dp[n-1], dp[n-2] + nums[n])

        dp[2] = 1+3 or 2 => 4
        dp[3] = 2 + 1 or 4 => 4
        '''

        # manage edge case
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        dp = [0] * len(nums)
        dp[0], dp[1] = nums[0], nums[1]
        
        for i in range(2, len(nums)):
            tmp = [dp[i-1], dp[i-2] + nums[i]]
            if i-3 >= 0:
                tmp.append(dp[i-3] + nums[i])
            dp[i] = max(tmp)
        
        return dp[-1]