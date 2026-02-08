class Solution:
    # dfs
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        cache = {}

        def dfs(i: int, current_total: int) -> int:
            if i == len(nums):
                if current_total == target:
                    return 1
                else:
                    return 0

            if (i, current_total) not in cache:           
                cache[(i, current_total)] = dfs(i+1, current_total + nums[i]) + dfs(i+1, current_total - nums[i])
            return cache[(i, current_total)]
        
        return dfs(0, 0)