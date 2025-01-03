class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        nums = [4, 1, 2, 2, 3, 0, 0, 2] val = 2
                l                 r

             => [0, 1, 3, 0, 4        ] in place, and return 5
        '''

        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                count += 1

        l, r = 0, len(nums)-1
        while l < r:
            while l < r and nums[l] != val:
                l += 1
            
            while l < r and nums[r] == val:
                r -= 1
            
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l+1, r-1
        
        return count
        