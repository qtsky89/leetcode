class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        '''
        example1.

        + + . +
        . . * +
        + + + .

        step1. using queue put the entrace and visited (set)
        step2. push queue (if possible) up donw left right
        step3. while loop, if hit the exit, then return that count value
        '''

        # step1. using queue put the entrace and visited (set)
        q = deque([[entrance[0], entrance[1], 0]])

        visited = set()
        while q:
            i, j,  count = q.popleft()

            if (i, j) in visited:
                continue
            else:
                visited.add((i, j))

            # check if we reach the exit?
            if [i, j] != entrance and (i==0 or i == len(maze)-1 or j==0 or j == len(maze[0])-1):
                return count
            
            # down
            if (i+1, j) not in visited and  i + 1 <= len(maze)-1 and maze[i+1][j] == '.':
                q.append([i+1, j, count+1])
            
            # right
            if (i, j+1) not in visited and j+1 <= len(maze[0]) -1 and maze[i][j+1] == '.':
                q.append([i, j+1,  count+1])
            
            # up
            if (i-1, j) not in visited and i-1 >= 0 and maze[i-1][j] == '.':
                q.append([i-1, j,  count+1])
            
            # left
            if (i, j-1) not in visited and j-1 >=0 and maze[i][j-1] == '.':
                q.append([i, j-1,  count+1])
        return -1






                
