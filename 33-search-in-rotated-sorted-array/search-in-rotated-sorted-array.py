class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        nums = 4 5 6 7 0 1 2
               ^     ^     ^   target = 0
        '''

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                return mid
            
            # left is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid -1
                else:
                    l = mid + 1
            else: # right is sorted
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1