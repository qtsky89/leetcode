class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        nums = [1, 1, 1] k = 2
                ^  ^
                   ^  ^
        nuns = [1, 2, 3] k = 3
                ^  ^
                      ^

        prefix_nums = [0, 1, 3, 6]
                       
        find i, j combination that 
        
        prefix_nums[j] - prefix_nums[i] = k
        '''

        prefix_nums = [0] * len(nums)

        for i in range(0, len(nums)):
            prefix_nums[i] += (prefix_nums[i-1] if i-1 >= 0 else 0) + nums[i]
        
        prefix_nums.insert(0, 0)

        # find i, j combination that  i <= j prefix_nums[j] - prefix_nums[i] = k

        #  prefix_nums = [0, 1, 3, 6] , k=3
                                   
          
        '''
            count = 1

            hash_map = {
                0 : 1
                1 : 1
                3 : 1
                6 : 1
            }
        '''
                    
        count = 0
        hash_map = {}
        for i in range(len(prefix_nums)):
            if prefix_nums[i] - k in hash_map:
                count += hash_map[prefix_nums[i] - k]

            if prefix_nums[i] not in hash_map:
                hash_map[prefix_nums[i]] = 1
            else:
                hash_map[prefix_nums[i]] += 1
        return count