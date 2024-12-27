class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]

        positions: 0   1   2   3   4   5   6   7   8   9   10  11  12
                   2           4       3           1       0

        
        => (10, 2) (8, 4) (0, 1) (5, 1) (3, 3)
        
        => (0, 1) (3, 3) (5, 1) (8, 4) (10, 2)
             12     3      7      1       1
                     ^          
        stack = [1, 7, 12] => #

        
        '''

        datas = []
        for p, s in zip(position, speed):
            datas.append((p, s))
        
        datas.sort()

        stack = []
        for i in range(len(datas)-1, -1, -1):
            time = (target - datas[i][0]) / datas[i][1]

            if not stack:
                stack.append(time)
                continue
            
            if time <= stack[-1]:
                continue
            else:
                stack.append(time)
            
        return len(stack)


