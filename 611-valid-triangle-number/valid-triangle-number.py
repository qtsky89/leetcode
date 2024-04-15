class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        [2, 3, 4, 4 5]
         ^        ^ ^

        nums[i] + nums[j] > nums[k]
        '''

        count = 0

        nums.sort()

        for k in range(len(nums)-1, 1, -1):
            i = 0
            j = k-1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    count += (j-i)
                    j-=1
                else:
                    i += 1
        return count
                