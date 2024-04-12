
'''
n=1
    1 : 1
    2 : 1
    3 : 1 
    4 : 1
    5 : 1
    6 : 1
    7 : 1
    8 : 1
    9 : 1
    0 : 1

n=2
   61
   81
   
   new_dp[2] = dp[6] + dp[8]

    1 : 1
    2 : 1
    3 : 1 
    4 : 1
    5 : 1
    6 : 1
    7 : 1
    8 : 1
    9 : 1
    0 : 1

n  =3

    new_dp[2] = 
'''

class Solution:
    def knightDialer(self, n: int) -> int:
        state = [
            [4, 6],
            [8, 6],
            [7, 9],
            [4, 8],
            [0, 3, 9],
            [],
            [0, 1, 7],
            [2, 6],
            [1, 3],
            [2, 4]
        ]

        if n == 1:
            return 10
        
        dp = [1] * 10
        
        for i in range(1, n):
            new_dp = [0] * 10

            for i, li in enumerate(state):
                for val in li:
                    new_dp[i] += dp[val]
            
            dp = new_dp
        
        return sum(dp) % (10**9 + 7)

