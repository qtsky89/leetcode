class Solution:
    # numRows = 1, output: [[1]]
    # numRows = 2, output: [[1], [1,1]]
    # numRows = 3, output: [[1], [1,1], [1,2,1]]
    # numRows = 4, output: [[1], [1,1], [1,2,1], [1,3,3,1] ...]
    
    def generate(self, numRows: int) -> List[List[int]]:
        ret = []
        for i in range(numRows):
            if i == 0:
                ret.append([1])
                continue
            
            last_element = ret[-1]
            
            tmp = last_element + [1]
            for j in range(1, len(tmp)-1):
                tmp[j] = last_element[j-1]+last_element[j]
            
            ret.append(tmp)
        return ret
                
            
            
            
            
        
        
        