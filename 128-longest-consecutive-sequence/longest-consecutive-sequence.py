class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''

        [100, 4, 200, 1, 3, 2]

        # step1 : make set
        set(nums)

        # step2: make hash_map
        {
            1 : 1
            100 : 1
            200 : 1
        }

        # step3. 
        '''
        # step1 : make set
        nums_set = set(nums)

        # step2: make hash_map
        hash_map = {}

        for i in range(len(nums)):
            # it meas, it's starting number
            if nums[i] - 1 not in nums_set:
                hash_map[nums[i]] = 1

        longest_num = 0
        for key in hash_map:
            i = key
            while True:
                if i + 1 in nums_set:
                    hash_map[key] += 1
                else:
                    break
                i += 1
            
            longest_num = max(longest_num, hash_map[key])
        
        return longest_num
        

                
        