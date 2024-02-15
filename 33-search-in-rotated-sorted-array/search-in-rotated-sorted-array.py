class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        nums = [4, 5, 6, 7, 0, 1, 2] target = 0


        1. I need to find pivot index first
        2. divide into two array group
        3. search both of them using binary search

        example1. nums = [4, 5, 6, 7, 0, 1, 2] target = 0

        [4, 5, 6, 7] [0, 1, 2]
                     lmr

        nums[m] => 7                    target = 0   target < nums[m] and target < nums[l]
        nums[m] = > 1                   target = 0    target < nums[m] check left
        '''

        l, r = 0, len(nums)-1

        while l <= r:
            m = (l+r) // 2

            if target == nums[m]:
                return m
         
            # left is sorted
            if nums[l] <= nums[m]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
        
        
        
