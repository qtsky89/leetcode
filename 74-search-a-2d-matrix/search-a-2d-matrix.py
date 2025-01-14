class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix)-1

        while t <= b:
            m = t + (b-t) // 2

            if matrix[m][0] == target:
                return True
            elif matrix[m][0] < target:
                t = m + 1
            else:
                b = m - 1
        
        # t <= insert

        t = t - 1 if t - 1 >= 0 else t

        l, r = 0, len(matrix[0])-1

        while l <= r:
            m = l + (r-l) // 2

            if matrix[t][m] == target:
                return True
            elif matrix[t][m] < target:
                l = m + 1
            else:
                r = m - 1
            
        return False
