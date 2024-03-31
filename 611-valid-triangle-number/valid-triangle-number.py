class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        nums[i] + nums[j] > nums[k]

            [2, 2, 3, 4]
             ^        ^       
        '''

        nums.sort()

        ret = 0

        for k in range(len(nums)-1, 1, -1):
            i = 0
            j = k-1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    ret += (j-i)
                    j -= 1
                else:
                    i += 1
        return ret