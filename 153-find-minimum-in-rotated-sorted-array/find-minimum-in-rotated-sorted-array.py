class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        i, j  = 0 , len(nums)-1

        while i <= j:
            mid = (i + j) //2

            '''
            if nums[mid] == target:
                    return mid
            '''

            if nums[i-1] > nums[i]:
                return nums[i]
            elif nums[j-1] > nums[j]:
                return nums[j]
            elif nums[mid-1] > nums[mid]:
                return nums[mid]
            
            if nums[i] < nums[mid]:
                i = mid + 1
            else:
                j = mid - 1
