class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        example1.
            nums = 3 2 2 3
                   ^   ^
                   2 2 3 3


            nums = 2 2 return 2


        example2.
            nums = 0 1 2 2 3 0 4 2
                       ^       ^
                   0 1 4 2 3 0 2 2
                         ^   ^
                   0 1 4 0 3 2 2 2
        '''

        p1, p2 = 0, len(nums)-1

        # p1 should be pointing val
        # p2 should be not pointing val
        # switch
        # until p1 < p2

        while p1 < p2:
            while p1 < p2 and nums[p1] != val:
                p1 += 1
            
            while p1 < p2 and nums[p2] == val:
                p2 -= 1
            
            nums[p1], nums[p2] = nums[p2], nums[p1]
        
        count = 0
        for n in nums:
            if n == val:
                count += 1
        
        return len(nums) - count

        