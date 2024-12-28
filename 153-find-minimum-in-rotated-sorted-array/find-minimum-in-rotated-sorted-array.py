class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        [1, 2, 3, 4, 5]
        [5, 1, 2, 3, 4] rotate 1
        [4, 5, 1, 2, 3] rotate 2
        [3, 4, 5, 1, 2] rotate 3
        [2, 3, 4, 5, 1] rotate 4
        [1, 2, 3, 4, 5] rotate 5


        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        [9, 10, 1, 2, 3, 4, 5, 6, 7, 8]

                   *
        [8, 9, 10, 1, 2, 3, 4, 5, 6, 7] n=3
                

        find this index (smallest nums[i] index)
        nums[i-1] > nums[i]
        '''

        if len(nums) == 1:
            return nums[0]

        l, r = 0, len(nums)-1

        while l<=r:
            mid = l + (r-l) // 2

            # find it!
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1
    
    '''
        time complexity: O(logN) space compexity: O(1)
    '''