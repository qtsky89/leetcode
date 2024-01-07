from collections import deque

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        '''
        + + +
        * . .
        + + +
        '''

        q = deque([(entrance[0], entrance[1], 0)])

        visited = set()
        while q:
            x, y, count = q.popleft()
            if (x,y) in visited:
                continue
            else:
                visited.add((x, y))

            # exit
            if count != 0 and (x == 0 or y == 0 or x == len(maze)-1 or y == len(maze[0])-1):
                return count
            
            if x + 1 <= len(maze)-1 and maze[x+1][y] != '+' and (x+1, y) not in visited:
                q.append((x+1, y, count+1))
            
            if x - 1 >= 0 and maze[x-1][y] != '+' and (x-1, y) not in visited:
                q.append((x-1, y, count+1))
            
            if y + 1 <= len(maze[0])-1 and maze[x][y+1] != '+' and (x, y+1) not in visited:
                q.append((x, y+1, count+1))
            
            if y - 1 >= 0 and maze[x][y-1] != '+' and (x, y-1) not in visited:
                q.append((x, y-1, count+1))
            
        return -1
                

        