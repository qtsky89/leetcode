class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        temperatures = [73 74 75 71 69 72 76 73]
        answer          1   1  4  2  1  1  0  0
                        -
        
        stack = [0]
        '''

        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):          
            while stack and temperatures[stack[-1]] < temperatures[i]:
                # index = 0, i = 1
                index = stack.pop()
                answer[index] = i - index
            stack.append(i)
        
        return answer
                
                
            