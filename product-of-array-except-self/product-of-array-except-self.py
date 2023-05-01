class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        nums =  [1,2,3,4]
        
        nums1 =            1     [1,     1*2,   1*2*3]
        nums2 =           234    34      4]       1

        nums1 = [1, 1*2, 1*2*3, 1*2*3*4]
        nums2 = [1   234    34      4 ]

        result = [2*3*4, 1*3*4, 1*2*4, 1*2*3]
        '''

        # make nums1
        nums1 = [0] * (len(nums))
        for i in range(len(nums1)):
            if i == 0:
                nums1[0] = nums[0]
                continue
            
            nums1[i] = nums[i] * nums1[i-1]
        nums1.pop()
        nums1 = [1] + nums1
    

        # make nums2
        nums2 = [0] * (len(nums))
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                nums2[i] = nums[i]
                continue
            nums2[i] = nums2[i+1] * nums[i]
        nums2.pop(0)
        nums2 = nums2 + [1]

        ret = [0] * len(nums)
        for i in range(len(nums)):
            ret[i] = nums1[i] * nums2[i]
        
        return ret

        
        







        