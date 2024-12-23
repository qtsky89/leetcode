class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        '''
        1, 10, 23, 72    target=3
        tb         
         ^


        val <= target
        '''

        t, b = 0, len(matrix)-1

        while t <= b:
            mid = (t+b) // 2

            if matrix[mid][0] <= target:
                t = mid + 1
            else:
                b = mid - 1

        # what we want    
        row = (t + b) // 2

        l, r = 0, len(matrix[0])-1

        while l <= r:
            mid = (l+r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid-1
            else:
                l = mid + 1
        
        return False