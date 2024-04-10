class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        '''
        lo=12, hi=15, k=2

        [12, 13, 14, 15]

        12 => 6 => 3 => 10 => 5 => 16 => 8 => 4 => 2 => 1 9 steps

        dp[12] = dp[6] + 1
        dp[6] = dp[3] + 1
        dp[3] = dp[10] + 1
            ...

        '''

        cache = {1: 1}

        def dp(n: int):
            if n in cache:
                return cache[n]
            
            # even
            if n % 2 == 0:
                cache[n] = dp(n/2) + 1
            else: # odd
                cache[n] = dp(n*3+1) + 1

            return cache[n]

        ret = [0] * (hi-lo+1)

        for i, n in enumerate(range(lo, hi+1)):
            ret[i] = [dp(n), n]
        
        ret.sort()
        return ret[k-1][1]

        
  