from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_ocean = set()

        q = deque()

        for i in range(len(heights)):
            q.append((i, 0))
        for j in range(len(heights[0])):
            q.append((0, j))
        
        while q:
            i, j = q.popleft()
            pacific_ocean.add((i, j))

            if i+1 <= len(heights)-1 and heights[i][j] <= heights[i+1][j] and (i+1, j) not in pacific_ocean:
                q.append((i+1, j))
            if j+1 <= len(heights[0])-1 and heights[i][j] <= heights[i][j+1]  and (i, j+1) not in pacific_ocean:
                q.append((i, j+1))
            if i-1 >= 0 and heights[i][j] <= heights[i-1][j]  and (i-1, j) not in pacific_ocean:
                q.append((i-1, j))
            if j-1 >= 0 and heights[i][j] <= heights[i][j-1]  and (i, j-1) not in pacific_ocean:
                q.append((i, j-1))
        
        atlantic_ocean = set()

        q = deque()
        for i in range(len(heights)):
            q.append((i, len(heights[0])-1))
        
        for j in range(len(heights[0])):
            q.append((len(heights)-1 ,j))
            
        
        while q:
            i, j = q.popleft()
            atlantic_ocean.add((i, j))

            if i+1 <= len(heights)-1 and heights[i][j] <= heights[i+1][j]  and (i+1, j) not in atlantic_ocean:
                q.append((i+1, j))
            if j+1 <= len(heights[0])-1 and heights[i][j] <= heights[i][j+1] and (i, j+1) not in atlantic_ocean:
                q.append((i, j+1))
            if i-1 >= 0 and heights[i][j] <= heights[i-1][j] and (i-1, j) not in atlantic_ocean:
                q.append((i-1, j))
            if j-1 >= 0 and heights[i][j] <= heights[i][j-1] and (i, j-1) not in atlantic_ocean:
                q.append((i, j-1))
        
        tmp = pacific_ocean & atlantic_ocean

        ret = []
        for t in tmp:
            ret.append(list(t))
        
        return ret