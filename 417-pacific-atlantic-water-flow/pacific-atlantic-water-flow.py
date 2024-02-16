from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''

        '''

        pacific_set = set()
        atlantic_set = set()
        
        # pacific ocean
        q = deque()
        for j in range(len(heights[0])):
            q.append((0, j))
        
        for i in range(len(heights)):
            q.append((i, 0))
        
        pacific_visited = set()
        while q:
            i, j = q.popleft()
            pacific_visited.add((i, j))

            if i + 1 <= len(heights)-1 and (i+1, j) not in pacific_visited and heights[i+1][j] >= heights[i][j]:
                q.append((i+1, j))
            
            if j + 1 <= len(heights[0])-1 and (i, j+1) not in pacific_visited and heights[i][j+1] >= heights[i][j]:
                q.append((i, j+1))
            
            if i - 1 >= 0 and (i-1, j) not in pacific_visited and heights[i-1][j] >= heights[i][j]:
                q.append((i-1, j))
            
            if j - 1 >= 0 and (i, j-1) not in pacific_visited and heights[i][j-1] >= heights[i][j]:
                q.append((i, j-1))
        
        # atlantic ocean
        q = deque()
        for j in range(len(heights[0])):
            q.append((len(heights)-1, j))
        
        for i in range(len(heights)):
            q.append((i, len(heights[0])-1))
        
        atlantic_visited = set()
        while q:
            i, j = q.popleft()
            atlantic_visited.add((i, j))

            if i - 1 >= 0 and (i-1, j) not in atlantic_visited and heights[i-1][j] >= heights[i][j]:
                q.append((i-1, j))
            
            if j - 1 >= 0 and (i, j-1) not in atlantic_visited and heights[i][j-1] >= heights[i][j]:
                q.append((i, j-1))

            if i + 1 <= len(heights)-1 and (i+1, j) not in atlantic_visited and heights[i+1][j] >= heights[i][j]:
                q.append((i+1, j))
            
            if j + 1 <= len(heights[0])-1 and (i, j+1) not in atlantic_visited and heights[i][j+1] >= heights[i][j]:
                q.append((i, j+1))
        
        return (pacific_visited & atlantic_visited)

            
