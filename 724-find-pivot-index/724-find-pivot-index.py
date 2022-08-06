class Solution:
    # nums = [1,7,3,6,5,6]
    def pivotIndex(self, nums: List[int]) -> int:
        # accumulated_nums = [1,8,11,17,22,28]
        accumulated_nums = nums[:]
        for i in range(1, len(accumulated_nums)):
            accumulated_nums[i] += accumulated_nums[i-1]
        
        def summary(start_index: int, end_index: int) -> int:
            if end_index < 0:
                return 0
            
            return accumulated_nums[end_index] - (accumulated_nums[start_index-1] if start_index-1 >= 0 else 0)
        
        for i in range(len(nums)):
            if summary(0, i-1) == summary(i+1, len(nums)-1):
                return i
        
        return -1
        
        ''' brute force
        for i in range(0, len(nums)):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
            
        return -1'''
    
        
        