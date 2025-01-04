class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        nums = [1, 1, 1],  k = 2
                ^  ^
                   ^  ^ 
                           ret=2

        prefix_nums = [0, 1, 2, 3]
                       ^     ^
                           ^    ^


        
        nums = [1, 2, 3], k = 3
                ^  ^
                      ^^
                           ret=2
        

        prefix_nums = [0, 1, 3, 6] k = 3

        i=0, j=2
        i=2, j=3
            
        prefix_nums[j] - prefix_nums[i] = k



               nums = [1, -1, 0], k=0
                       ^   ^
                              ^^
         prefix_nums= [0, 1, 0, 0] k = 0
                       i     j

        '''

        prefix_nums = [0] * (len(nums))

        for i in range(0, len(nums)):
            prefix_nums[i] = (prefix_nums[i-1] if i-1 >= 0 else 0) + nums[i]
        
        prefix_nums.insert(0, 0)
       
        count = 0
        '''

        nums = [1, 2, 3], k = 3

        prefix_nums = [0, 1, 3, 6] 
                       ^     ^
                             ^  ^
        
        prefix_nums[j] - prefix_nums[i] = k       => find all combination of (i, j)
    
        '''
        hash_map = {}
        
        for i in range(len(prefix_nums)):
            if (prefix_nums[i] - k) in hash_map:
                count += hash_map[prefix_nums[i] - k]
            
            if prefix_nums[i] in hash_map:
                hash_map[prefix_nums[i]] += 1
            else:
                hash_map[prefix_nums[i]] = 1

        return count


        
        