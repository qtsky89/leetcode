class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''

        nums = [0,1,1,1,0,1,1,0,1]
               ^^
        '''

        p1, p2 = 0, 0

        k = 1
        count = 0
        while p2 <= len(nums)-1:
            if nums[p2] == 0:
                if k > 0:
                    k -= 1
                    p2 += 1
                else:
                    if nums[p1] == 0:
                        k += 1
                    p1 += 1    
            else:
                p2 += 1
        
            count = max(count, p2-p1-1)

        return count
