class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        '''
        1 1 2 3 3 4 4 8 8
                ^
        0 1 2 3 4 4 5 5 6 6

        mid = 4 mid+1 =5 

        nums[mid] == nums[mid+1] the target should be in the right
        nums[mid] != nums[mid+1] the target should be in the left

        if nums[mid] != nums[mid+1] and nums[mid] != nums[mid-1] => target
        '''

        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums)-1

        while l<=r:
            mid = (l+r) // 2

            # target
            if (mid==0 or nums[mid] != nums[mid-1]) and (mid==len(nums)-1 or nums[mid] != nums[mid+1]):
                return nums[mid]
            
            # right side is even
            if nums[mid] == nums[mid-1]:
                if (r-mid) % 2 == 0:
                    r = mid - 2
                else:
                    l = mid + 1
            elif nums[mid] == nums[mid+1]:
                if (mid-l) % 2 == 0:
                    l = mid + 2
                else:
                    r = mid - 1
                
                
                
             


