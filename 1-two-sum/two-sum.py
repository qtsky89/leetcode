class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        nums = [2, 7, 11, 15], target = 9

        hash_map = {
            7 : 0
        }


        '''

        hash_map = {}
        for i in range(len(nums)):
            if nums[i] in hash_map:
                return [hash_map[nums[i]], i]
            else:
                hash_map[target-nums[i]] = i
        