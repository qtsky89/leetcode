class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
           0    1    2

        0  1    1    0

        1  1    1    0

        2  0    0    1


        0 <-> 1   2   return number 2

        '''

        count = 0
        visited = set()

        def visit(i: int):
            visited.add(i)

            # j is connected index
            for j in range(len(isConnected[i])):
                if j not in visited and isConnected[i][j] == 1:
                    visit(j)


        for li in isConnected:
            for i in range(len(li)):
                if i not in visited:
                    visit(i)
                    count += 1


        return count