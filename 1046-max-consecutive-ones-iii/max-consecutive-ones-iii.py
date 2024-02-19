class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        nums = [ 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0 ], k = 2
                 ^        ^                         k = 1
                 ^           ^                      k = 0
                             ^  ^                   k = 0
                                ^              ^

                                (p2 - p1 + 1)
        '''
        
        p1, p2 =  0, 0
        if nums[0] == 0:
            k -= 1
        max_length = 0
        while p2 <= len(nums)-1:
            while k < 0:
                if nums[p1] == 0:
                    k += 1
                p1 += 1

            if p2+1 <=len(nums)-1:
                if nums[p2+1] == 1:
                    pass
                else:
                    k -= 1

            max_length = max(max_length, p2-p1+1)

            p2 += 1
        return max_length
            

            