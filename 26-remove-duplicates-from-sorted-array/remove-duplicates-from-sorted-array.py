class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:       
        w, r = 0, 0

        last = -float('inf')
        while r <= len(nums)-1:
            if nums[r] != last:
                nums[w] = nums[r]
                last = nums[r]
                r += 1
                w += 1
            else:
                r += 1
        return w
        
        
        