class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0

        tmp_count = 0
        # nums = [1 1 0 1 1 1]
        for i in range(len(nums)):
            if nums[i] == 1:
                tmp_count += 1
                max_count = max(max_count, tmp_count)
            else:
                tmp_count = 0
        
        return max_count