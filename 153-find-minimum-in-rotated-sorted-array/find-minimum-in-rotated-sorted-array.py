class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        0 1 2 3 4 5 6 7

        case0. 0 1 2 4 5 6 7 rotate 0 times
        case1. 7 0 1 2 4 5 6 rotate 1 times
        case2. 6 7 0 1 2 4 5 rotate 2 times
        case3. 5 6 7 0 1 2 4 rotate 3 times
        case4. 4 5 6 7 0 1 2 rotate 4 times
        case5. 2 4 5 6 7 0 1 rotate 5 times
        case5. 1 2 4 5 6 7 0 rotate 6 times
        case6. 0 1 2 4 5 6 7 rotate 7 times

        step1. [ 4, 5, 6, 7, 8, 9, 10, 0, 1, 2]
                 i           ^               j
                                i      ^     j

        if nums[i-1] > nums[i]:
            return i
        '''

        if len(nums) == 1:
            return nums[0]

        i, j = 0, len(nums) - 1

        while i <= j:
            mid = (i+j) // 2
            
            # TODO. deal with i-1 later
            # i is minimum
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[i-1] > nums[i]:
                return nums[i]
            elif nums[j-1] > nums[j]:
                return nums[j]
            
            if nums[i] < nums[mid]:
                i = mid + 1
            elif nums[mid] < nums[j]:
                j = mid - 1
                
        
                

        