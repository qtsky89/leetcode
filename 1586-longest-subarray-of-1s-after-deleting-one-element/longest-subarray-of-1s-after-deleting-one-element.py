class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        example1. nums = [1, 1, 0, 1] => [1, 1, 1]
                                ^     => 3
        
        exmaple2. nums = [1, 1, 1, 1, 0, 1, 1, 0, 1 ] => 5
                          ^           ^
                             ^                 ^
                                         ^        ^
        example3. nums = [ 1, 1, 1 ] => 2  -> TODO. edgecase 
                                 ^  
        1. remove 0
        2. if that 0 can make longest 1's sub array prefer that 1
        3. remove 1
        '''

        p1, p2 = 0, 0
        
        coin = 1 # this coin can change 0 -> 1

        if nums[0] == 0:
            coin -=1
        
        ret = 0
        while p2 <= len(nums)-1:
            ret = max(ret, p2-p1+1)
            if p2 + 1 <= len(nums)-1 and nums[p2+1] == 0:
                coin -= 1
            while coin < 0: # I need my coin back
                if nums[p1] == 0:
                    coin += 1 
                p1 +=1
            p2 += 1
        return ret-1
        