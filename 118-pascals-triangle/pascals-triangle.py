class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        '''
             [1]
             [1 1]
             [1 2 1]
             [1 3 3 1]
             [1 4 6 4 1]
             [1 5 10 10 5 1]
        '''
        ret = []

        # 0, 1, 2, 3, 4, 5
        for i in range(numRows):
            tmp = [1] * (i+1)

            for j in range(1, len(tmp)-1):
                if ret and j <= len(ret[-1])-1:
                    tmp[j] = ret[-1][j-1] + ret[-1][j]
            ret.append(tmp)
        return ret
                


            
            
            
            