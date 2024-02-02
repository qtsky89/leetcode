class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        nums   = [1, 2, 3, 4]
                  ^        ^
                  1  2  6
                    24  12 4
                        
        output = [24, 12, 8, 6]
        '''

        leftProduct = [0] * len(nums)
        leftProduct[0] = nums[0]
        for i in range(1, len(nums)):
            leftProduct[i] = nums[i] * leftProduct[i-1]

        rightProduct = [0] * len(nums)
        rightProduct[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            rightProduct[i] = nums[i] * rightProduct[i+1]
        
        ret = [0] * len(nums)

        for i in range(len(ret)):
            if i == 0:
                ret[i] = rightProduct[i+1]
            elif i-1 >= 0 and i+1 <= len(nums)-1:
                ret[i] = leftProduct[i-1] * rightProduct[i+1]
            elif i == len(nums)-1:
                ret[i] = leftProduct[i-1]
        return ret

        