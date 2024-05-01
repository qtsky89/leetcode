from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
        
        max_minute = 0

        while q:
            i, j, current_minute = q.popleft()

            max_minute = max(max_minute, current_minute)

            if i+1 <= len(grid)-1 and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                q.append([i+1, j, current_minute+1])
            
            if i-1>=0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                q.append([i-1, j, current_minute+1])
            
            if j+1 <= len(grid[0])-1 and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                q.append([i, j+1, current_minute+1])
            
            if j-1 >= 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                q.append([i, j-1, current_minute+1])
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        

        return max_minute