class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        '''
        https://www.youtube.com/watch?v=Ua0GhsJSlWM
        
        text1, text2

        1. text1 = "a b c e d "
           text2 = "a   c e"


              a  c  e 
            a 1  
            b    0  0
            c    1
            e       1
            d

            1. text[i] == text[j] => dp[i][j] = dp[i+1][j+1] + 1
            2. text[i] != text[j] => dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        '''

        dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]