class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        nums = [1, 1, 0, 1]
               ^^
        '''

        p1, p2 = 0, 0

        ret = 0
        count = 0
        
        is_deleted = False
        while p2 <= len(nums)-1:
            if nums[p2] == 1:
                p2 += 1
            else:
                if not is_deleted:
                    is_deleted = True
                    p2 += 1
                else:
                    if nums[p1] == 0:
                        is_deleted = False
                    p1 += 1

            count = max(count, p2-p1-1)
        return count
            