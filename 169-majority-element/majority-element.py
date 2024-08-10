class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        time complexity : O (N)
        space complexity : O (1)
        '''

        c = Counter(nums)

        for key in c:
            if c[key] > len(nums) // 2:
                return key