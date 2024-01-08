from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        0. round
        2 1 1
        1 1 0
        0 1 1

        1. round
        2 2 1
        2 1 0
        0 1 1
        
        2. round
        2 2 2
        2 2 0
        0 1 1

        3. round
        2 2 2
        2 2 0
        0 2 1

        4. round
        2 2 2
        2 2 0
        0 2 2
        '''

        visited = set()
        q = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
        
        max_minute = 0
        while q:
            i, j, minute = q.popleft()
            if (i, j) in visited:
                continue
            else:
                visited.add((i, j))

            max_minute = max(max_minute, minute)
            
            if i+1 <= len(grid)-1 and grid[i+1][j] == 1:
                q.append([i+1, j, minute+1])
            if i-1 >= 0 and grid[i-1][j] == 1:
                q.append([i-1, j, minute+1])
            if j+1 <= len(grid[0])-1 and grid[i][j+1] ==1:
                q.append([i, j+1, minute+1])
            if j-1 >= 0 and grid[i][j-1] == 1:
                q.append([i, j-1, minute+1])
            
        # check visited count equal all orange
        orange_count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    orange_count += 1
        if orange_count != len(visited):
            return -1
        return max_minute
            
        