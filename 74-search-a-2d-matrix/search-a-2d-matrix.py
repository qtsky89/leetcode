class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = [matrix[i][0]  for i in range(len(matrix))]

        base_row = 0

        i, j = 0, len(matrix)-1
        while i <= j:
            mid = (i+j) // 2

            if matrix[mid][0] == target:
                return True
            
            if (matrix[mid][0] < target and mid == len(matrix)-1) or (matrix[mid][0] < target < matrix[mid+1][0]):
                base_row = mid
                break
            
            if target > matrix[mid][0]:
                i = mid+1
            else:
                j = mid-1
        
        i, j = 0, len(matrix[0])-1
        while i <= j:
            mid = (i + j) // 2

            if matrix[base_row][mid] == target:
                return True
            elif target > matrix[base_row][mid]:
                i = mid + 1
            else:
                j = mid -1
        return False