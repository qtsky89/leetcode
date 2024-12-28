class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''

        [4, 5, 6, 7, 8, 9, 10, 0, 1, 2, 3]          target=0
                            l     m      r                            


        if nums[l] <= target <= nums[m]:
            r = mid -1
        else:
            l = mid + 1
        

        '''

        l, r = 0, len(nums)-1

        while l<=r:
            mid = l + (r-l) // 2

            if nums[mid] == target:
                return mid
            
            # left one is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else: # right one is sorted
                if nums[mid] <= target <= nums[r]:
                    l = mid +1
                else:
                    r = mid -1

        return -1
