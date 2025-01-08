class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        example2.
            n = 3, trust[[1, 3], [2, 3]]

            be_trust_count {
                1 : 0
                2 : 0
                3 : 3 <=
            }
            be_trust_count always should be n

            trust_count {
                1: 1
                2: 1
                3: 0 <= 
            }
            trust_count always should be 0
        '''
        be_trust_count = {i:0 for i in range(1, n+1)}
        trust_count = {i:0 for i in range(1, n+1)}

        for a, b in trust:
            trust_count[a] += 1
            be_trust_count[b] += 1
        

        for i in range(1, n+1):
            if be_trust_count[i] == n-1 and trust_count[i] == 0:
                return i
        
        return -1
