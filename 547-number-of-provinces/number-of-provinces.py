class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        '''
        n cities

       |  0   1   2
      -------------
      0 | 1   1   0
      1 | 1   1   0
      2 | 0   0   1


      0 - 1   2
        '''

        total = 0
        visited = set()
        def dfs(current: int):

            visited.add(current)

            for i in range(len(isConnected[current])):
                if (isConnected[current][i] == 1) and (i not in visited):
                    dfs(i)
                
        for i in range(len(isConnected)):
            if i not in visited:
                total += 1
                dfs(i)

        return total   
        
