from bisect import bisect_right
class Solution:
    # nums = [1,3,5,6] target=5
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        # target_index = 3
        target_index = bisect_right(nums, target)
        
        if target_index-1 >= 0 and nums[target_index-1] == target:
            return target_index-1
        else:
            return target_index
        
        
        