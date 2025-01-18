class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        nums = 1, 2, 3, 4, 5
        prefix_sum = 0, 1, 3, 6, 10, 15                     k=3 
                           i

                   we need to find i, j that prefix_sum[j] - prefix_sum[i] => k

                   how many count (i, j) have ?
        '''

        prefix_sum = [0] * len(nums)
        prefix_sum[0] = nums[0]

        for i in range(1, len(prefix_sum)):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        prefix_sum.insert(0, 0)

        count = 0
        hash_map: dict[int, int] = {}

        for i in range(len(prefix_sum)):
            if prefix_sum[i]-k in hash_map:
                count += hash_map[prefix_sum[i]-k]
            
            if prefix_sum[i] in hash_map:
                hash_map[prefix_sum[i]] += 1
            else:
                hash_map[prefix_sum[i]] = 1
        return count


        # we need to find i, j that i < j and prefix_sum[j] - prefix_sum[i] => k
        # for i in range(0, len(prefix_sum)-1):
        #     for j in range(i+1, len(prefix_sum)):
        #         if prefix_sum[j] - prefix_sum[i] == k:
        #             count += 1

        

        



