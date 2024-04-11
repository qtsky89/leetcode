class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        s = 1 2 
            ^
        dp[i] = dp[i-1]
        
        '''

        dp = [0] * (len(s))

        dp[0] = 1 if s[0] != '0' else 0
        
        for i in range(1, len(s)):
            if int(s[i]) >= 1:
                dp[i] += dp[i-1]
            
            if 10 <= int(s[i-1:i+1]) <= 26:
                dp[i] += (dp[i-2] if i - 2 >= 0 else 1)

        return dp[-1]