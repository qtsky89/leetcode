class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
         1  3  5  7
        10 11 16 20
        23 30 34 60


        # solution1. brute force way

        # solution2. 16

        interation1.
            matrix[0][0] == target?

            target > matrix[0][0]
                matrix[0][1] matrix[1][0]
            
            1 -> 10 -> 11 -> 16
        '''
        
        q = deque([[0, 0]])
        
        while q:
            i, j = q.popleft()

            if matrix[i][j] == target:
                return True
            
            # TODO. check i+1
            if i+1 <= len(matrix)-1 and target >= matrix[i+1][j]:
                q.append([i+1, j])
            elif j+1 <= len(matrix[0])-1 and target >= matrix[i][j+1]:
                q.append([i, j+1])
        
        return False

