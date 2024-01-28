class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        XOR

        X   Y   X XOR Y
        0   0     0      
        0   1     1
        1   0     1
        1   1     0

        '''

        ret = 0
        for n in nums:
            ret ^= n
        
        return ret