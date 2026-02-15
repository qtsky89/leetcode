class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False


        prev_dp = [True for _  in range(len(s2)+1)]

        for i in range(len(s1)+1):
            dp = [False for _ in range(len(s2)+1)]
            if i == 0:
                dp[0] = True
            for j in range(len(s2)+1):
                if prev_dp[j] and i-1 >= 0 and s1[i-1] == s3[i+j-1]:
                    dp[j] = True
                elif j-1>=0 and dp[j-1]  and s2[j-1] == s3[i+j-1]:
                    dp[j] = True
            prev_dp = dp
            
        return dp[-1]