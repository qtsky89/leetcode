class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        '''
        peak => if   nums[i-1]  < nums[i] > nums[i+1] 
                if   i==0   and nums[i] > nums[i+1]
                if   nums[i-1] <  nums[i] and i== len(nums)-1

        '''

        if len(nums) == 1:
            return 0

        l, r = 0, len(nums)-1

        while l <= r:
            i = (l + r) // 2

            left = nums[i-1] if i-1 >= 0 else -float('inf')
            right = nums[i+1] if i+1 <= len(nums)-1 else -float('inf')

            # let check is's peak
            if (left < nums[i] > right):
                return i
            # increasing
            elif nums[i] < right:
                l = i + 1
            else:
                r = i - 1
