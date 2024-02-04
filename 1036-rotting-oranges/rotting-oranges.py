class Solution:
    '''
    example1.

    time 0
    2 1 1 
    1 1 0
    0 1 1 

    time 1
    2 2 1
    2 1 0
    0 1 1

    time 2
    2 2 2
    2 2 0
    0 1 1

    time 3
    2 2 2
    2 2 0
    0 2 1

    time 4
    2 2 2
    2 2 0
    0 2 2

    step1. make queue and push all rotten orange's point in that queue
    step2. through while loop, if adjacent cell is 1 then I push that queue
    step3. I neet to check if fresh organge is stil left, in that case return -1
    step4. until there no left in the queue return the times
    '''
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # step1. make queue and push all rotten orange's point in that queue
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    q.append([i, j, 0])
        
        # step2. through while loop, if adjacent cell is 1 then I push that queue
        max_minute = 0
        while q:
            i, j, minute = q.popleft()

            max_minute = minute

            if i+1 <= len(grid)-1 and grid[i+1][j] == 1:
                grid[i+1][j] = 2
                q.append([i+1, j, minute+1])
            
            if j+1 <= len(grid[0])-1 and grid[i][j+1] == 1:
                grid[i][j+1] = 2
                q.append([i, j+1, minute+1])
            
            if i-1 >= 0 and grid[i-1][j] == 1:
                grid[i-1][j] = 2
                q.append([i-1, j, minute+1])
            
            if j-1 >= 0 and grid[i][j-1] == 1:
                grid[i][j-1] = 2
                q.append([i, j-1, minute+1])
        
        # step3. I neet to check if fresh organge is stil left, in that case return -1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1
        # step4. until there no left in the queue return the times
        return max_minute

            
            


