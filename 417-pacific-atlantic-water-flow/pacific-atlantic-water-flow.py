from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific_set = set()
        atlantic_set = set()

        q = deque()
        # pacific
        for i in range(len(heights)):
            q.append((i, 0))
        
        for j in range(len(heights[0])):
            q.append((0, j))
        
        while q:
            i, j = q.popleft()
            
            pacific_set.add((i, j))

            if i+1 <= len(heights)-1 and heights[i][j] <= heights[i+1][j] and (i+1, j) not in pacific_set:
                q.append((i+1, j))
            if j+1 <= len(heights[0])-1 and heights[i][j] <= heights[i][j+1] and (i, j+1) not in pacific_set:
                q.append((i, j+1))
            if i-1 >= 0 and heights[i][j] <= heights[i-1][j] and (i-1, j) not in pacific_set:
                q.append((i-1, j))
            if j-1 >= 0 and heights[i][j] <= heights[i][j-1] and (i, j-1) not in pacific_set:
                q.append((i, j-1))
        
        
        q = deque()
        # atlantic
        for i in range(len(heights)):
            q.append((i, len(heights[0])-1))
        
        for j in range(len(heights[0])):
            q.append((len(heights)-1, j))
        
        while q:
            i, j = q.popleft()
            
            atlantic_set.add((i, j))

            if i+1 <= len(heights)-1 and heights[i][j] <= heights[i+1][j] and (i+1, j) not in atlantic_set:
                q.append((i+1, j))
            if j+1 <= len(heights[0])-1 and heights[i][j] <= heights[i][j+1] and (i, j+1) not in atlantic_set:
                q.append((i, j+1))
            if i-1 >= 0 and heights[i][j] <= heights[i-1][j] and (i-1, j) not in atlantic_set:
                q.append((i-1, j))
            if j-1 >= 0 and heights[i][j] <= heights[i][j-1] and (i, j-1) not in atlantic_set:
                q.append((i, j-1))

        ret_set = pacific_set & atlantic_set

        ret = []
        for t in ret_set:
            ret.append(list(t))
        return ret

        
        