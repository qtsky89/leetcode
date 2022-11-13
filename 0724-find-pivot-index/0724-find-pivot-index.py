class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left, right = [0] * len(nums), [0] * len(nums)
        
        left[0] = nums[0]
        for i in range(1, len(left)):
            left[i] = left[i-1] + nums[i]
        
        right[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            right[i] = right[i+1] + nums[i]
        
                
        for i in range(len(nums)):
            left_sum = left[i] - nums[i]
            right_sum = right[i] - nums[i]
            
            if left_sum == right_sum:
                return i
        
        return -1
            
        