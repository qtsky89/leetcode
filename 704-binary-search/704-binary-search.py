from bisect import bisect_right

class Solution:
    # nums = [-1,0,3,5,9,12] target = 9
    def search(self, nums: List[int], target: int) -> int:
        
        # target_index = 4
        target_index = bisect_right(nums, target)-1
        
        if nums[target_index] == target:
            return target_index
        else:
            return -1
        
        
        