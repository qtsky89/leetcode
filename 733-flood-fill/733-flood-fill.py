class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # new_color = 2
        original_color = image[sr][sc]
        
        def dfs(i: int, j: int, visited: set):
            image[i][j] = color
            visited.add((i, j))
            
            if i+1 <= len(image)-1 and image[i+1][j] == original_color and (i+1, j) not in visited:
                dfs(i+1, j, visited)
            
            if i-1 >= 0 and image[i-1][j] == original_color  and (i-1, j) not in visited:
                dfs(i-1, j, visited)
            
            if j+1 <= len(image[0])-1 and image[i][j+1] == original_color  and (i, j+1) not in visited:
                dfs(i, j+1, visited)
            
            if j-1 >= 0 and image[i][j-1] == original_color  and (i, j-1) not in visited:
                dfs(i, j-1, visited)
            
        dfs(sr,sc, set())
        
        return image
        
        