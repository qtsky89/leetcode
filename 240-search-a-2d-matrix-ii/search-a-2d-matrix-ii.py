from collections import deque

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        q = deque([(0, len(matrix[0])-1)])

        while q:
            i, j = q.popleft()

            if not (0 <= i <= len(matrix)-1 ) or not ( 0 <= j <= len(matrix[0])-1 ):
                break

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                q.append((i, j-1))
            elif matrix[i][j] < target:
                q.append((i+1, j))
        
        return False