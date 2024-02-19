class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        '''
        grid = 3 2 1
               1 7 6
               2 7 7
        
        s = set(
        (3, 2, 1)
        (1, 7, 6)
        (2, 7, 7))

        (3, 1, 2) -> no
        (2, 7, 7) -> yes  count+=1
        (1, 6, 7) -> no
        
        return count
        '''

        visited = defaultdict(int)
        for i in range(len(grid)):
            visited[tuple(grid[i])] += 1

        count = 0
        for j in range(len(grid[0])):
            # 3, 2, 1
            tmp = []
            for i in range(len(grid)):
                tmp.append(grid[i][j])
            
            if tuple(tmp) in visited:
                count += visited[tuple(tmp)]
        return count