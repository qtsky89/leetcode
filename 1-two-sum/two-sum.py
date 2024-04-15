class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        {
            2 : 0

        }

        nums [2, 7, 11, 15]  target = 9
              ^
                 ^
                 return [0, 1]
        '''

        hash_map = {}

        for i in range(len(nums)):
            if target - nums[i] in hash_map:
                return [hash_map[target-nums[i]], i]
            else:
                hash_map[nums[i]] = i
        

        