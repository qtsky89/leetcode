class Solution:
    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     '''
    #     nums = 10  9  2  5  3  7  101  18
    #            1   1  1  2  2  3   4   4



    #     '''

    #     ret = 0
    #     def dfs(current_index: int, sequence_length: int, current_max: int) -> None:
    #         nonlocal ret
    #         # Update the global max LIS length
    #         ret = max(ret, sequence_length)

    #         for i in range(current_index, len(nums)):
    #             if nums[i] > current_max:
    #                 dfs(i+1, sequence_length+1, nums[i])
            
    #     dfs(0, 0, -float('inf'))

    #     return ret

    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        nums = [10,9,2,5,3,7,101,18]
        dp                        1


        dp[7] = 1
        dp[6] => 1 or (dp[7]+1)
        dp[5] => 1 or (dp[6] + 1) or (dp[7] + 1)

        '''


        dp = [0] * len(nums)

        dp[-1] = 1

        for i in range(len(nums)-2, -1, -1):
            tmp = [1]

            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    tmp.append(dp[j] + 1)
            dp[i] = max(tmp)
        
        return max(dp)