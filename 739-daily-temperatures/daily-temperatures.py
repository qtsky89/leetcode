class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        temperatures = [ 73 74 75 71 69 72 76 73 ]
                          0  1  2  3  4  5  6  7

        stack        = [ 75 71 72


        ret = [0 0 0 0 0 0 0 0]

        '''

        ret = [0] * len(temperatures)

        stack = []
        
        i = 0 
        while i <= len(temperatures)-1:
            if not stack or temperatures[stack[-1]] > temperatures[i]:
                stack.append(i)
                i+=1
                continue
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                ret[index] = i - index
            
            stack.append(i)
            
            i+=1
        
        return ret
            
            
