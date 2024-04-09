class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        '''
        2 3 6 18
               ^

        dp[2] = 1
        dp[3] = 1
        dp[6] = 1 + 2 = 3
        dp[18] = 1 + 6 => 7

        

        '''

        arr.sort()

        # key : arr[i], value: int
        dp = {n: 1 for n in arr}

        for i in range(1, len(arr)):
            j = 0
            k = i-1

            while j <= k:
                if arr[i] == arr[j] * arr[k]:
                    tmp = dp[arr[j]] * dp[arr[k]]

                    if arr[j] != arr[k]:
                        tmp *= 2
                    
                    dp[arr[i]] += tmp

                    j += 1
                    k -= 1
                elif arr[i] > arr[j] * arr[k]:
                    j += 1
                else:
                    k -= 1
                    
        return sum(dp.values()) % (10 ** 9 + 7)
        '''
        dp[2] = 1 = 1
        dp[4] = 1 + 1 = 2
        dp[5] = 1 = 1
        dp[10] = 1 + 2 = 3
        '''

            
            

        

        