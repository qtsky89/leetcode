class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ret = [0] * len(nums)
        
        ret[0] = nums[0]
        for i in range(1, len(ret)):
            ret[i] = ret[i-1] + nums[i]
        
        return ret
        