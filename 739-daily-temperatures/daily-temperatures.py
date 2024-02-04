class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        temperatures = [ 73 74 75 71 69 72 76 73 ]
                         1   1  4  2  1  1  0  0

        ret = [1, 1, 4  2 1  1      ]
               0  1  2  3 4  5 6  7
        '''

        stack = []
        ret = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()

                ret[index] = i - index
            
            stack.append(i)

        return ret
            
            