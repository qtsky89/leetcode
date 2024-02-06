class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        nums = [2, 7, 11, 15] target = 9

        # step1
        make hash map

        # step2
        if target-nums exist in hash_map return the index

        else insert to hash_map
        '''

        hash_map = {}

        for i in range(len(nums)):
            if target-nums[i] in hash_map:
                return [hash_map[target-nums[i]], i]
            else:
                hash_map[nums[i]] = i
        

        