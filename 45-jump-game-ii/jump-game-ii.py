class Solution:
    def jump(self, nums: List[int]) -> int:
        '''
        nums = [3,2,1,0,4]
                       
        '''
        p1 = len(nums)-1

        count = 0
        while p1 > 0:
            is_moved = False
            for p2 in range(0, p1):
                length = p1 - p2
                
                if nums[p2] >= length:
                    p1 = p2
                    count += 1
                    is_moved = True
                    break
                
        return count