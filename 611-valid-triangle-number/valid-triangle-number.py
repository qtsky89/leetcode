class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        '''
        [2, 3, 4, 4]
                  ^     [2, 4, 4]
                        [2, 3, 4]
                        [2, 3, 4]
                        [3, 4, 4]
        '''

        count = 0

        nums.sort()

        for k in range(len(nums)-1, 1, -1):
            i, j = 0, k-1

            while i < j:
                if nums[i] + nums[j] > nums[k]:
                   count += j - i
                   j -= 1
                else:
                    i += 1

       
        return count
                