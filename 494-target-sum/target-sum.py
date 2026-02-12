class Solution:
    # dfs with cache memoization
    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
    #     cache = {}

    #     def dfs(i: int, current_total: int) -> int:
    #         if i == len(nums):
    #             if current_total == target:
    #                 return 1
    #             else:
    #                 return 0

    #         if (i, current_total) not in cache:           
    #             cache[(i, current_total)] = dfs(i+1, current_total + nums[i]) + dfs(i+1, current_total - nums[i])
    #         return cache[(i, current_total)]
        
    #     return dfs(0, 0)
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = [defaultdict(int) for _ in range(len(nums)+1)]

        dp[0][0] = 1 # (e element, currnt sum is 0) => 1 way
        
        for i in range(len(nums)):
            for cur_sum, count in dp[i].items():
                dp[i+1][cur_sum + nums[i]] += count
                dp[i+1][cur_sum - nums[i]] += count
        

        return dp[-1][target]


        