class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        ret = [-1, -1]

        # step1. find first index
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2

            # first index
            if nums[mid] == target and (mid == 0 or (mid-1 >= 0 and nums[mid-1] != nums[mid])):
                ret[0] = mid
                break
            elif nums[mid] == target:
                r = mid -1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        # step2. find second index
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (l + r) // 2

            # second index
            if nums[mid] == target and (mid == len(nums)-1 or (mid+1 <= len(nums)-1 and nums[mid+1] != nums[mid])):
                ret[1] = mid
                break
            elif nums[mid] == target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return ret