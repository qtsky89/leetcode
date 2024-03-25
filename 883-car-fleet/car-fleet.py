class Solution:
    def carFleet(self, target: int, positions: List[int], speeds: List[int]) -> int:
        '''
        position, speed

        target = 12

        position = [10, 8, 0, 5, 3]
        speed      [ 2, 4, 1, 1, 3]
                   

                                                     
            i=0    [0, 1] [3, 3] [5, 1] [8, 4]    [10, 2] 
                                        12-8/4=>1 12-10/2 => 1
            i=1    [1, 1] [6, 3] [6, 1] [12,4] [12, 2] => ret = 1
            i=2    [2, 1] [7, 1]
            i=3    [3, 1] [8, 1]
            i=4    [4, 1] [9, 1]
            i=5    [5, 1] [10,1]
            i=6    [6, 1] [11,1]
            i=7    [7, 1] [12,1] ret = 1
        '''

        datas = []
        for position, speed in zip(positions, speeds):
            datas.append([position, speed, (target-position)/speed])

        datas.sort(key= lambda x:[x[0], -x[1]])

        stack = []
        
        for i in range(len(datas)):
            if not stack:
                stack.append(datas[i])
                continue
            
            # collision happen
            while stack and stack[-1][2] <= datas[i][2]:
                stack.pop()

            stack.append(datas[i])
        
        return len(stack)
            

        

