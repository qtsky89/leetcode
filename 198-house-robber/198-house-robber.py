class Solution:
        
    
    def rob(self, nums: List[int]) -> int:
        hash_map = {}
        def dp(i: int) -> int:
            if i in hash_map:
                return hash_map[i]
            
            if i == 0:
                hash_map[0] = nums[0]
            elif i == 1:
                hash_map[1] = max(nums[0], nums[1])
            else:
                hash_map[i] = max(dp(i-2) + nums[i], dp(i-1))
            
            return hash_map[i]
            
        return dp(len(nums)-1)